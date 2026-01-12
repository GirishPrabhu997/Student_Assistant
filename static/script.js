document.addEventListener('DOMContentLoaded', () => {
    const chatHistory = document.getElementById('chat-history');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    
    // CHANGED: Fixed port to 5000 to match Flask default
    const API_URL = '/chat'; 

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(`${sender}-message`);
        messageDiv.innerHTML = `<p>${text}</p>`;
        chatHistory.appendChild(messageDiv);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    async function getAiResponse(userMessage) {
        userInput.disabled = true;
        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();
            addMessage(data.response, 'assistant');
        } catch (error) {
            addMessage("I'm having trouble connecting to the local AI. Is Ollama running?", 'assistant');
        } finally {
            userInput.disabled = false;
            userInput.focus();
        }
    }

    function sendMessage() {
        const userText = userInput.value.trim();
        if (userText === "") return;
        addMessage(userText, 'user');
        userInput.value = '';
        getAiResponse(userText);
    }

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
});