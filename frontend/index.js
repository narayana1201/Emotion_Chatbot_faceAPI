'use strict';
const MODEL_URL = '/models';
const faceReg = document.querySelector(".FR-div");
const faceCanvas = document.querySelector(".FR-canvas");
const startBtn = document.querySelector(".FR-start");
startBtn.addEventListener("click", faceRegcognition);
const chats = document.querySelector(".FR-chat");
const send = document.querySelector(".sendBtn");
const inputDiv = document.querySelector(".chat-input");
const emotionDiv = document.querySelector(".FR-data");
const stopBtn = document.querySelector(".FR-stop");
let Expression = "happy";
let mediaStream;
let IsMic = false;


// ****************************************************************face regcognition**********************************************************//

async function faceRegcognition() {
    await faceapi.loadSsdMobilenetv1Model(MODEL_URL);
    await faceapi.loadFaceLandmarkModel(MODEL_URL);
    await faceapi.loadFaceRecognitionModel(MODEL_URL);
    await faceapi.loadFaceExpressionModel(MODEL_URL);
    console.log("called");
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
    faceReg.srcObject = mediaStream;
}

faceReg.addEventListener("play", async () => {

    async function detectAndUpdateEmotion() {
        try {
            const detection = await faceapi.detectAllFaces(faceReg).withFaceLandmarks().withFaceExpressions();
            console.log(detection);

            const size = { width: faceReg.videoWidth, height: faceReg.videoHeight };
            faceapi.matchDimensions(faceCanvas, size);
            const resizedDectect = faceapi.resizeResults(detection, size);

            detection.forEach(face => {
                const expressions = face.expressions;
                Expression = Object.keys(expressions).reduce((a, b) => expressions[a] > expressions[b] ? a : b);
                console.log("Emotion:", Expression);
                emotionDiv.value = Expression;
            });

            faceCanvas.getContext('2d').clearRect(0, 0, faceCanvas.width, faceCanvas.height);
            faceapi.draw.drawDetections(faceCanvas, resizedDectect);
            faceapi.draw.drawFaceExpressions(faceCanvas, resizedDectect);
        } catch (error) {
            console.error("Error:", error);
        }
    }
    await detectAndUpdateEmotion();
    setInterval(detectAndUpdateEmotion, 30000);

});

function end() {
    location.reload();
}

stopBtn.addEventListener("click", end)

// *******************************************************************************chat***********************************************************//

const createChat = (message, className) => {
    const newChat = document.createElement("li");
    newChat.classList.add(className);
    newChat.innerHTML = `<p>${message}</p>`;
    return newChat;
}

const handleChat = async (exp) => {
    const data = inputDiv.value.trim();
    if (data != '') {
        chats.appendChild(createChat(data, "sent"));
        chats.scrollTo(0, chats.scrollHeight);
        inputDiv.value = '';
        await Handler(exp, data);
    };
}

const handleVoice = async (exp, msg) => {
    if (msg != '') {
        chats.appendChild(createChat(msg, "sent"));
        chats.scrollTo(0, chats.scrollHeight);
        await Handler(exp, msg);
    };
}

function chatReply(reply) {
    const replyChat = chats.appendChild(createChat(reply, "received"));
    console.log(replyChat);
    chats.scrollTo(0, chats.scrollHeight);
}

const handleInput = () => {
    if (Expression) {
        handleChat(Expression);
    }
    else {
        alert("no expression found");
    }
}

send.addEventListener("click", handleInput);

// *****************************************************text to speech***************************************************************//

function speak(detail) {
    const utterance = new SpeechSynthesisUtterance(detail);
    const voices = speechSynthesis.getVoices();
    utterance.voice = voices[0];
    speechSynthesis.speak(utterance);
}

// ******************************************************speech to text***************************************************************//

const recognition = new webkitSpeechRecognition() || new SpeechRecognition();

const speech = document.querySelector('.speech-recognition');

speech.addEventListener("click", toggleMic);

recognition.lang = 'en-US';

let RecognizedTranscript;

recognition.onresult = async function (event) {
    console.log(event);
    RecognizedTranscript = event.results[0][0].transcript;
    console.log('Transcript:', RecognizedTranscript);
    if (Expression) {
        handleVoice(Expression, RecognizedTranscript);
    }
};

recognition.onend = function () {
    speech.src = 'assets/micoff.svg';
    console.log("Recognition stopped");
    RecognizedTranscript = '';
}

recognition.onerror = function (event) {
    if (event.error === 'no-speech') {
        console.log("no speech");
    }
    else {
        console.error('Speech recognition error:', event.error);
    }
};

function startRecognition() {
    recognition.start();
    console.log("startRecognition called");
}

function stopRecognition() {
    recognition.stop();
    console.log("stopRecognition called");
}


function toggleMic() {
    IsMic = !IsMic;
    if (IsMic) {
        speech.src = 'assets/mic.svg';
        startRecognition();
    } else {
        speech.src = 'assets/micoff.svg';
        stopRecognition();
    }
}

// **********************************************************************API**********************************************************************//

async function Handler(exp, data) {
    stopRecognition();

    try {
        const text = await Apicall(exp, data);
        console.log(text);

        if (text) {
            speak(text);
            chatReply(text);
        } else {
            alert("no reply")
        }
    } catch (error) {
        console.error('Error talking to AI:', error);
        alert("Server is not connected.");
    }
}

//api
async function Apicall(exp, data) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "message": data, "emotion": exp }),
        });

        if (!response.ok) {
            console.error('Server responded with error:', response.status);
            throw new Error('Server responded with error:', response.status);
        }

        const Resdata = await response.json();
        console.log(Resdata);
        return Resdata.message;
    } catch (error) {
        console.error('Error occurred during API call:', error);
        throw error;
    }
}