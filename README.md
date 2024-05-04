# Emotion_Chatbot_faceAPI
Chatbot Based on user's Emotion and input message. It will talk back using NLP Spacy.

# Working Of Emotion ChatBot
The Emotion Chatbot is a web-based chat application leveraging FaceAPI.js, a facial deep learning model, to discern the user's emotional state based on facial expressions. Upon receiving user input messages, it retrieves predefined responses for each emotion stored in MongoDB. Utilizing both the detected emotion and the user's input from the frontend, the data is transmitted to the backend implemented in Python, employing the Spacy NLP package. 

In the backend, the system processes the input to find semantic similarity with stored messages in the database corresponding to the detected emotion. Subsequently, it retrieves the most relevant message to the user's input message and emotional context. Additionally, the implementation integrates modules for Speech-to-Text and Text-to-Speech functionalities, enabling users to interact with the Chatbot via voice input and auditory output. This comprehensive approach facilitates a seamless and intuitive interaction experience for users.

# Pre Install Softwares
1. Python 3.12
2. Node
3. Mongodb

# Installation Stpes:
1. clone github project.
2. Install Requirements using ' pip install -r requirements.txt
3. Install spacy en_core_web_sm 
4. Run : python main.py
**Backend will be started**

**Any Doubts:** narayananhm123@gmail.com

