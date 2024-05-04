from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['emotion_detection_db']
chat_collection = db['chat_logs']
reply_collection = db['messages_reply']

# happy_messages = [
#     {"user_input": "I'm feeling great today!", "chatbot_response": "That's wonderful to hear!"},
#     {"user_input": "I just got some good news!", "chatbot_response": "Congratulations! That's fantastic!"},
#     {"user_input": "Today is a beautiful day!", "chatbot_response": "It sure is! Enjoy every moment of it!"},
#     {"user_input": "I love spending time with my friends!", "chatbot_response": "Friendship is priceless!"},
#     {"user_input": "I'm excited about the upcoming event!", "chatbot_response": "It's going to be amazing!"},
# ]

# sad_messages = [
#     {"user_input": "I'm feeling down today.", "chatbot_response": "I'm sorry to hear that. Is there anything I can do to help?"},
#     {"user_input": "I received some bad news.", "chatbot_response": "I'm here for you. Feel free to talk about it."},
#     {"user_input": "I miss my loved ones.", "chatbot_response": "It's okay to miss them. They are always in your heart."},
#     {"user_input": "I'm struggling with something.", "chatbot_response": "Remember, you're not alone. We'll get through this together."},
#     {"user_input": "I'm feeling overwhelmed.", "chatbot_response": "Take a deep breath. You can handle this."},
# ]

# neutral_messages = [
#     {"user_input": "Hello!", "chatbot_response": "Hi there! How can I assist you today?"},
#     {"user_input": "What's the weather like today?", "chatbot_response": "Let me check... It looks like it's sunny outside!"},
#     {"user_input": "How was your day?", "chatbot_response": "It was good, thank you for asking! How about yours?"},
#     {"user_input": "Do you have any plans for the weekend?", "chatbot_response": "Not yet, but I'm open to suggestions!"},
#     {"user_input": "What time is it?", "chatbot_response": "It's currently [current time]."},
# ]

# Insert sample messages into MongoDB collection
# reply_collection.insert_many(happy_messages + sad_messages + neutral_messages)


# Sample data for messages_reply collection
# sample_data = [
#     {"emotion": "happy", "message": "That's wonderful to hear!"},
#     {"emotion": "happy", "message": "It's great to see you happy!"},
#     {"emotion": "happy", "message": "Congratulations! That's fantastic!"},
#     {"emotion": "sad", "message": "I'm sorry to hear that. Is there anything I can do to help?"},
#     {"emotion": "sad", "message": "Remember, it's okay to feel sad sometimes. I'm here to listen."},
#     {"emotion": "sad", "message": "Take a deep breath. You can handle this."},
#     {"emotion": "neutral", "message": "Hi there! How can I assist you today?"},
#     {"emotion": "neutral", "message": "It was good, thank you for asking! How about yours?"},
#     {"emotion": "neutral", "message": "Let me check... It looks like it's sunny outside!"},
#     # Add more sample messages as needed
# ]

happy_samples = [
    {"emotion": "happy", "message": "That's wonderful to hear!"},
    {"emotion": "happy", "message": "It's great to see you happy!"},
    {"emotion": "happy", "message": "Congratulations! That's fantastic!"},
    {"emotion": "happy", "message": "You deserve all the happiness in the world!"},
    {"emotion": "happy", "message": "Wishing you endless joy and laughter!"},
    {"emotion": "happy", "message": "Your happiness lights up the room!"},
    {"emotion": "happy", "message": "You make every day brighter with your smile!"},
    {"emotion": "happy", "message": "Hooray! Today is a day for celebration!"},
    {"emotion": "happy", "message": "Feeling happy? Spread the joy to everyone around you!"},
    {"emotion": "happy", "message": "Keep shining bright like a diamond!"},
    {"emotion": "happy", "message": "Every moment with you is a reason to smile!"},
    {"emotion": "happy", "message": "Your positive energy is contagious!"},
    {"emotion": "happy", "message": "Sending you a virtual high-five for all your accomplishments!"},
    {"emotion": "happy", "message": "Let your happiness be the soundtrack of your life!"},
    {"emotion": "happy", "message": "Life is better when you're laughing!"},
    {"emotion": "happy", "message": "Cheers to happiness, laughter, and love!"},
    {"emotion": "happy", "message": "Dance like nobody's watching! It's time to celebrate your happiness!"},
    {"emotion": "happy", "message": "You're the sunshine on a cloudy day!"},
    {"emotion": "happy", "message": "Here's to finding joy in the little things!"},
    {"emotion": "happy", "message": "Today is a perfect day to be happy!"},
]

sad_samples = [
    {"emotion": "sad", "message": "I'm sorry to hear that. Is there anything I can do to help?"},
    {"emotion": "sad", "message": "Remember, it's okay to feel sad sometimes. I'm here to listen."},
    {"emotion": "sad", "message": "Take a deep breath. You can handle this."},
    {"emotion": "sad", "message": "Sending you hugs and support during this difficult time."},
    {"emotion": "sad", "message": "It's okay to not be okay. We'll get through this together."},
    {"emotion": "sad", "message": "Sometimes, it's okay to cry. Let it out and then let's find a way forward."},
    {"emotion": "sad", "message": "Feeling sad is a part of being human. You're not alone in this."},
    {"emotion": "sad", "message": "I'm here for you, no matter how tough things may seem."},
    {"emotion": "sad", "message": "Life can be tough sometimes, but you're tougher. Hang in there."},
    {"emotion": "sad", "message": "Tomorrow is a new day, filled with new opportunities. Don't lose hope."},
    {"emotion": "sad", "message": "It's okay to take a break and take care of yourself. You deserve it."},
    {"emotion": "sad", "message": "Every storm runs out of rain. Hold on, better days are coming."},
    {"emotion": "sad", "message": "You're stronger than you think. You've overcome challenges before, and you'll overcome this one too."},
    {"emotion": "sad", "message": "You're not alone. Reach out to someone you trust and talk about how you're feeling."},
    {"emotion": "sad", "message": "Even on the darkest days, there's a glimmer of hope. Hold on to that hope."},
    {"emotion": "sad", "message": "It's okay to not have all the answers right now. Take things one step at a time."},
    {"emotion": "sad", "message": "You're not defined by your lowest moments. You're defined by how you rise from them."},
    {"emotion": "sad", "message": "I believe in you. You're capable of overcoming this sadness and finding happiness again."},
    {"emotion": "sad", "message": "Allow yourself to feel what you're feeling. It's a step towards healing."},
    {"emotion": "sad", "message": "Your feelings are valid, and it's okay to express them."},
]

neutral_samples = [
    {"emotion": "neutral", "message": "Hi there! How can I assist you today?"},
    {"emotion": "neutral", "message": "It was good, thank you for asking! How about yours?"},
    {"emotion": "neutral", "message": "Let me check... It looks like it's sunny outside!"},
    {"emotion": "neutral", "message": "Not much, just hanging out. How about you?"},
    {"emotion": "neutral", "message": "That's interesting. Tell me more about it."},
    {"emotion": "neutral", "message": "I'm here to help. What can I do for you today?"},
    {"emotion": "neutral", "message": "Let's tackle this together. What's on your mind?"},
    {"emotion": "neutral", "message": "Did you have a chance to relax today?"},
    {"emotion": "neutral", "message": "Looks like it's going to be a busy day ahead. How can I assist you?"},
    {"emotion": "neutral", "message": "Just taking it easy today. How about you?"},
    {"emotion": "neutral", "message": "Feeling neither here nor there? That's okay, we all have those days."},
    {"emotion": "neutral", "message": "Sometimes, it's nice to just take a break and enjoy the moment."},
    {"emotion": "neutral", "message": "Let's focus on the present moment. What's on your mind right now?"},
    {"emotion": "neutral", "message": "Life is full of surprises. Let's see what today brings."},
    {"emotion": "neutral", "message": "I'm here whenever you need someone to talk to. What's on your mind?"},
    {"emotion": "neutral", "message": "Every day is a new opportunity. What are you looking forward to today?"},
    {"emotion": "neutral", "message": "Just checking in. How are you doing today?"},
    {"emotion": "neutral", "message": "Let's make today a great day! What's your plan for the day?"},
    {"emotion": "neutral", "message": "It's a pleasure to chat with you. What's on your mind?"},
    {"emotion": "neutral", "message": "Feeling balanced and centered today? Let's keep that energy going!"},
]


angry_samples = [
    {"emotion": "angry", "message": "I can't believe this happened again!"},
    {"emotion": "angry", "message": "This is absolutely infuriating!"},
    {"emotion": "angry", "message": "I'm so fed up with this nonsense!"},
    {"emotion": "angry", "message": "Why does this always happen to me?"},
    {"emotion": "angry", "message": "I've had enough of your excuses!"},
    {"emotion": "angry", "message": "I'm furious about this situation!"},
    {"emotion": "angry", "message": "I'm so angry I could scream!"},
    {"emotion": "angry", "message": "This is unacceptable behavior!"},
    {"emotion": "angry", "message": "I can't contain my anger any longer!"},
    {"emotion": "angry", "message": "I'm seething with rage right now!"},
    # Add more angry samples here
]

disgust_samples = [
    {"emotion": "disgust", "message": "I'm utterly repulsed by this."},
    {"emotion": "disgust", "message": "This is so gross, I can't even look at it."},
    {"emotion": "disgust", "message": "I feel sick to my stomach."},
    {"emotion": "disgust", "message": "I can't believe anyone would do something so vile."},
    {"emotion": "disgust", "message": "This is beyond disgusting."},
    {"emotion": "disgust", "message": "I'm revolted by what I just saw."},
    {"emotion": "disgust", "message": "This makes me want to gag."},
    {"emotion": "disgust", "message": "I can't even begin to describe how disgusted I am."},
    {"emotion": "disgust", "message": "I can't stand the sight of it."},
    {"emotion": "disgust", "message": "This is nauseating."},
    # Add more disgust samples here
]

surprised_samples = [
    {"emotion": "surprised", "message": "I can't believe it!"},
    {"emotion": "surprised", "message": "Well, that's unexpected!"},
    {"emotion": "surprised", "message": "I'm completely taken aback!"},
    {"emotion": "surprised", "message": "I never saw that coming!"},
    {"emotion": "surprised", "message": "What a surprise!"},
    {"emotion": "surprised", "message": "That's a shocker!"},
    {"emotion": "surprised", "message": "I'm genuinely surprised by this."},
    {"emotion": "surprised", "message": "This is quite the revelation!"},
    {"emotion": "surprised", "message": "I'm amazed by what just happened!"},
    {"emotion": "surprised", "message": "Color me surprised!"},
    # Add more surprised samples here
]

# Combine all samples
all_samples = happy_samples + angry_samples + disgust_samples + surprised_samples


# Insert sample data into the messages_reply collection
# reply_collection.insert_many(all_samples)

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['emotion_detection_db']
doctor_collection = db['doctors']

# Sample doctor details
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

# Insert sample doctor details into the database
# doctor_collection.insert_many(doctors_data)

# print("Sample doctor details inserted into the database.")



