function addMessage(message, isUser) {
    const chatMessages = document.getElementById('chatMessages');
    if (!chatMessages) {
        console.error('Element with ID "chatMessages" not found.');
        return;
    }

    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(isUser ? 'user-message' : 'bot-message');
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById('userInput');
    if (!userInput) {
        console.error('Element with ID "userInput" not found.');
        return;
    }

    const message = userInput.value.trim();
    if (message) {
        addMessage(message, true);
        userInput.value = '';

        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            if (data && data.response) {
                addMessage(data.response, false);
            } else {
                console.error('Unexpected response format:', data);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('userInput');
    if (userInput) {
        userInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                sendMessage();
            }
        });
    } else {
        console.error('Element with ID "userInput" not found.');
    }
});
