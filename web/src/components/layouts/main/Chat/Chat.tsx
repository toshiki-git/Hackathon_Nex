import React from "react";

type Message = {
  user: string;
  text: string;
};

type ChatProps = {
  chatLog: Message[];
  userName: string;
};

export const Chat: React.FC<ChatProps> = ({ chatLog, userName }) => {
  return (
    <div className="chat-container p-4 h-screen">
      <div className="chat-log max-w-md mx-auto overflow-y-auto h-4/5 space-y-4">
        {chatLog.map((msg, index) => (
          <div
            key={index}
            className={`message ${
              msg.user === userName
                ? "bg-blue-500 text-white rounded-tl-lg rounded-bl-lg rounded-br-lg p-2 ml-auto"
                : "bg-gray-300 text-black rounded-tr-lg rounded-tl-lg rounded-br-lg p-2 mr-auto"
            }`}
            style={{
              maxWidth: "80%",
            }}
          >
            <span className="user-name block font-bold mb-1">{msg.user}</span>
            <div className="text">{msg.text}</div>
          </div>
        ))}
      </div>
    </div>
  );
};
