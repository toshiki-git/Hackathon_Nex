import { useState } from 'react';
let socket: WebSocket | null = null;

export default function Home() {
  const [communityName, setcommunityName] = useState('');
  const [userName, setUserName] = useState('');
  const [message, setMessage] = useState('');
  const [chatLog, setChatLog] = useState<string[]>([]);


  const connectToWebSocket = () => {
    const wsUrl = `ws://localhost:8000/api/websocket/${communityName}`;

    socket = new WebSocket(wsUrl);
    socket.onmessage = (event) => {
        const message = event.data;
        console.log(event.data);
        displayMessage(message);
      };

    socket.onopen = () => {
      console.log("チャット開始");
    };
  };

  const sendMessage = () => {
    console.log("a")
    if (socket) {
      const dataToSend = {
        message: message,
        userName: userName
      };
      socket.send(JSON.stringify(dataToSend));
      setMessage('');
    }
  };

  const displayMessage = (message: string) => {
    setChatLog((prevChatLog) => [...prevChatLog, message]);
  };

  return (
    <div>
      <input
        type="text"
        id="communityName"
        placeholder="ルーム名"
        value={communityName}
        onChange={(e) => setcommunityName(e.target.value)}
      />
      <input
        type="text"
        id="userName"
        placeholder="ユーザー名"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
      />
      <button id="join_room_btn" onClick={connectToWebSocket}>入室</button>

      <br/>
      <br/>

      <input
        type="text"
        id="message"
        placeholder="メッセージ"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button id="send_ms_btn" onClick={sendMessage}>送信</button>

      <div id="chat">
        {chatLog.map((msg, index) => (
          <p key={index}>{msg}</p>
        ))}
      </div>
    </div>
  );
}
