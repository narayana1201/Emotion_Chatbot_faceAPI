from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import datetime
from pymongo import MongoClient
import spacy
import random

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['emotion_detection_db']
chat_collection = db['chat_logs']
reply_collection = db['messages_reply']

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to retrieve sample messages for the specified emotion from MongoDB
def get_emotion_messages(emotion):
    query = {"emotion": emotion}
    messages = list(reply_collection.find(query))
    return messages

# # Function to process user messages and generate chatbot responses
# def process_message(message, emotion):
#     # Check if the message is a greeting
#     greetings = ["hi", "hello", "hey", "greetings"]
#     if message.lower() in greetings:
#         if emotion.lower() == "happy":
#             return "Hi there! It's great to see you're feeling happy today!"
#         elif emotion.lower() == "sad":
#             return "Hi. What happened? Why are you looking sad?"
#         elif emotion.lower() == "angry":
#             return "Hey, calm down. What's bothering you?"
#         elif emotion.lower() == "neutral":
#             return "Hello! How can I assist you today?"

#     # If it's not a greeting, proceed to find the best reply from the database
#     # Use spaCy to understand user input and generate response
#     doc = nlp(message)
    
#     # Initialize variables for highest similarity and associated emotion
#     max_similarity = 0
#     best_message = None
    
#     # Retrieve sample messages for the specified emotion from MongoDB
#     emotion_messages = get_emotion_messages(emotion)
#     if not emotion_messages:
#         raise HTTPException(status_code=404, detail=f"No messages found for emotion '{emotion}'")
    
#     # Iterate through emotion messages and calculate similarity
#     for emotion_doc in emotion_messages:
#         emotion_message = emotion_doc["message"]
#         emotion_vector = nlp(emotion_message).vector
#         similarity = doc.similarity(nlp(emotion_message))
#         if similarity > max_similarity:
#             max_similarity = similarity
#             best_message = emotion_message
    
#     if best_message is None:
#         raise HTTPException(status_code=404, detail=f"No suitable message found for emotion '{emotion}'")
    
#     return best_message


# Define the doctors_data list with doctor details
doctors_data = [
    {
        "name": "Dr. Govindaraj",
        "specialty": "General Physician",
        "location": "Chennai",
        "address": "Anna Nagar, Chennai",
        "phone_number": "(212) 555-1234",
        "website": "www.apollo.com"
    },
    {
        "name": "Dr. S Jayaraman",
        "specialty": "Neurology",
        "location": "Chennai, Tamil Nadu",
        "address": "Apollo First Med Hospitals, 154, Poonamallee High Rd, New Bupathy Nagar, Kilpauk, Chennai, Tamil Nadu 600010",
        "phone_number": "08046961837",
        "website": "https://www.apollo247.com/doctors/dr-S-Jayaraman-74cf3b53-a2de-4c41-a8f6-c25d49f31017"
    },
    {
        "name": "Dr. Subramaniyan Raja",
        "specialty": "Eye Specialist",
        "location": "Chennai",
        "address": "366M+6QR Diabetic Clinic Sstower, Nungambakkam, Chennai, Tamil Nadu 600034",
        "phone_number": "01414931241",
        "website": "unknown"
    },
    {
        "name": "Dr. Gautham",
        "specialty": "Thyroid Specialist",
        "location": "Chennai",
        "address": "4/68, Pachaiappas College Hostel Rd, near Ega Theatre, Dasspuram, Chetpet, Chennai, Tamil Nadu 600031",
        "phone_number": "09566133660",
        "website": "https://docgautham.com/"
    },
]

# Function to process user messages and generate chatbot responses
def process_message(message, emotion):
    # Check if the message is a greeting
    greetings = ["hi", "hello", "hey", "greetings"]
    if message.lower() in greetings:
        if emotion.lower() == "happy":
            return "Hi there! It's great to see you're feeling happy today!"
        elif emotion.lower() == "sad":
            return "Hi. What happened? Why are you looking sad?"
        elif emotion.lower() == "angry":
            return "Hey, calm down. What's bothering you?"
        elif emotion.lower() == "neutral":
            return "Hello! How can I assist you today?"

    # If it's not a greeting, check if the message is related to hospitals or doctors
    if "hospital" in message.lower() or "doctor" in message.lower():
        # Select a random doctor's data from the list
        doctor_data = random.choice(doctors_data)
        return f"Here is the information for {doctor_data['name']}: Specialty: {doctor_data['specialty']}, Location: {doctor_data['location']}, Address: {doctor_data['address']}, Phone Number: {doctor_data['phone_number']}, Website: {doctor_data['website']}"

    # If the message is not related to hospitals or doctors, proceed to find the best reply from the database
    # Use spaCy to understand user input and generate response
    doc = nlp(message)
    
    # Initialize variables for highest similarity and associated emotion
    max_similarity = 0
    best_message = None
    
    # Retrieve sample messages for the specified emotion from MongoDB
    emotion_messages = get_emotion_messages(emotion)
    if not emotion_messages:
        raise HTTPException(status_code=404, detail=f"No messages found for emotion '{emotion}'")
    
    # Iterate through emotion messages and calculate similarity
    for emotion_doc in emotion_messages:
        emotion_message = emotion_doc["message"]
        emotion_vector = nlp(emotion_message).vector
        similarity = doc.similarity(nlp(emotion_message))
        if similarity > max_similarity:
            max_similarity = similarity
            best_message = emotion_message
    
    if best_message is None:
        raise HTTPException(status_code=404, detail=f"No suitable message found for emotion '{emotion}'")
    
    return best_message


# WebSocket route for real-time communication
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Process user messages and send responses
        emotion, message = data.split(":")
        response = process_message(message, emotion)
        await websocket.send_text(response)

# # API route to receive user input message and generate chatbot response
# @app.post("/chat")
# async def chat_response(message: str, emotion: str):
#     # Process user message and generate chatbot response
#     response = process_message(message, emotion)
#     return JSONResponse(content={"message": response}, status_code=200)

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    message: str
    emotion: str

# Modify the endpoint to use the Pydantic model
# @app.post("/chat")
# async def chat_response(request_body: ChatRequest):
#     # Process user message and generate chatbot response
#     response = process_message(request_body.message, request_body.emotion)
#     return JSONResponse(content={"message": response}, status_code=200)

@app.post("/chat")
async def chat_response(request_body: ChatRequest):
    # Process user message and generate chatbot response
    response = process_message(request_body.message, request_body.emotion)
    # Store user input and chatbot response in MongoDB
    chat_log = {
        "timestamp": datetime.datetime.utcnow(),
        "user_message": request_body.message,
        "emotion": request_body.emotion,
        "chatbot_response": response
    }
    chat_collection.insert_one(chat_log)
    return JSONResponse(content={"message": response}, status_code=200)

# Other API routes for managing user data, chat logs, etc.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
