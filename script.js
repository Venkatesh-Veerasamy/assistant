document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');
    
    // Simple chat response logic
    const response = generateResponse(userInput);
    chatBox.innerHTML += `<div>User: ${userInput}</div>`;
    chatBox.innerHTML += `<div>Assistant: ${response}</div>`;
    document.getElementById('user-input').value = ''; // Clear input
});

function generateResponse(input) {
    // Sample responses
    const responses = {
        "hi": "Hello! How can I assist you today?",
        "bye": "Goodbye! Have a great day!",
        "good night": "Good night! Sleep well!",
        // Add more responses here
    };

    return responses[input.toLowerCase()] || "I'm not sure how to respond to that.";
}
