import React, { useState } from "react";
import './App.css'; // Make sure this path is correct

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input) return;

    // Append the user's message to the chat
    const newMessage = { user: "You", text: input };
    setMessages([...messages, newMessage]);

    try {
      // Make a request to the Flask backend
      const response = await fetch(`/get?msg=${encodeURIComponent(input)}`);
      const data = await response.text();

      // Append the bot's response to the chat
      const botMessage = { user: "Bot", text: data };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error fetching bot response:", error);
    }

    // Clear the input field
    setInput("");
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>EndoAssist</h1>
        <h4>Clarify any questions/concerns about the doctor's office here</h4>
        <p>This chatbot is powered by AI and is designed to assist with general inquiries. Please consult a professional or trusted source for critical decisions.</p>
      </header>
      <div className="chat-container">
        <div className="chatbox">
        <p class="botText">
        <span>Hi! I'm EndoAssist, your chatbot.</span>
        </p>
          {messages.map((msg, index) => (
            <p key={index} className={msg.user === "Bot" ? "botText" : "userText"}>
              <span>{msg.text}</span>
            </p>
          ))}
        </div>
        <div className="inputArea">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Type a message..."
            className="textInput"
          />
          <button onClick={sendMessage} className="sendButton">Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
