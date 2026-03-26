/**
 * app.js - WebSocket client for real-time chat
 */

// DOM Elements
const loginScreen = document.getElementById('login-screen');
const chatScreen = document.getElementById('chat-screen');
const joinForm = document.getElementById('join-form');
const usernameInput = document.getElementById('username-input');
const displayName = document.getElementById('display-name');
const btnLeave = document.getElementById('btn-leave');

const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const messagesContainer = document.getElementById('messages-container');

// State
let ws = null;
let currentUsername = "";

// Event Listeners
joinForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = usernameInput.value.trim();
    if (username) {
        connectToChat(username);
    }
});

messageForm.addEventListener('submit', (e) => {
    e.preventDefault();
    sendMessage();
});

btnLeave.addEventListener('click', () => {
    if (ws) {
        ws.close();
    }
    showScreen('login');
});

// WebSocket Functions
function connectToChat(username) {
    currentUsername = username;
    
    // Connect to FastAPI WebSocket backend
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `ws://127.0.0.1:8000/ws/chat/${encodeURIComponent(username)}`;
    
    ws = new WebSocket(wsUrl);

    ws.onopen = () => {
        displayName.textContent = username;
        showScreen('chat');
        messagesContainer.innerHTML = ''; // clear initial messages
        messageInput.focus();
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        displayMessage(data);
    };

    ws.onclose = () => {
        showScreen('login');
        alert("Disconnected from chat server.");
    };

    ws.onerror = (error) => {
        console.error("WebSocket Error: ", error);
        alert("Connection error. Is the FastAPI server running?");
    };
}

function sendMessage() {
    if (!ws || ws.readyState !== WebSocket.OPEN) return;

    const content = messageInput.value.trim();
    if (content) {
        // Send raw text to the server (the server wraps it in JSON)
        ws.send(content);
        messageInput.value = '';
        messageInput.focus();
    }
}

// UI Helpers
function showScreen(screen) {
    document.getElementById('login-screen').classList.remove('active');
    document.getElementById('chat-screen').classList.remove('active');
    
    if (screen === 'login') {
        loginScreen.classList.add('active');
        usernameInput.value = '';
    } else {
        chatScreen.classList.add('active');
    }
}

function displayMessage(data) {
    // data format: { type: "system"|"chat", client_id: "...", content: "..." }
    const div = document.createElement('div');
    
    if (data.type === 'system') {
        div.className = 'system-message';
        div.textContent = data.content;
    } else if (data.type === 'chat') {
        const isMine = (data.client_id === currentUsername);
        div.className = `message-row ${isMine ? 'mine' : 'other'}`;
        
        const bubble = document.createElement('div');
        bubble.className = 'message-bubble';
        
        if (!isMine) {
            const sender = document.createElement('span');
            sender.className = 'message-sender';
            sender.textContent = data.client_id;
            bubble.appendChild(sender);
        }
        
        const text = document.createElement('div');
        text.textContent = data.content;
        bubble.appendChild(text);
        
        div.appendChild(bubble);
    }

    messagesContainer.appendChild(div);
    scrollToBottom();
}

function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
