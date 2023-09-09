import { useState } from 'react';

let socket: WebSocket | null = null;

export default function Home() {
  const [communityID, setCommunityID] = useState('');
  const [userName, setUserName] = useState('');
  const [message, setMessage] = useState('');
  const [chatLog, setChatLog] = useState<string[]>([]);

  const connectToWebSocket = () => {
    const wsUrl = `ws://localhost:8000/api/ws/${communityID}`;

    socket = new WebSocket(wsUrl);
    socket.onmessage = (event) => {
      const message = event.data;
      console.log(event.data);
      displayMessage(message);
    };

    //websocket接続したとき
    socket.onopen = () => {
      console.log("チャット開始");
      //過去のデーター取得
      fetch(`http://localhost:8000/api/community/?community_id=${communityID}`, {
        method: 'GET',
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('HTTPエラー');
        }
        return response.json();
      })
      .then(data => {
        //過去のコメント出力
        console.log(data)
      })
      .catch(error => {
        console.error('HTTP GETリクエストエラー:', error);
      });
    };
  };

  //リアルタイムチャットを送った時
  const sendMessage = () => {
    console.log("a");
    if (socket) {
      const dataToSend = {
        message: message,
        userName: userName
      };
      socket.send(JSON.stringify(dataToSend));
      setMessage('');
      
      //チャット内容データーベースに保存
      fetch('http://localhost:8000/api/community/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: userName, 
          community_id: communityID,
          content: message,
        }),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('HTTPエラー');
        }
      })
      .catch(error => {
        console.error('HTTP POSTリクエストエラー:', error);
      });
    }
  };

  const displayMessage = (message: string) => {
    setChatLog((prevChatLog) => [...prevChatLog, message]);
  };

  return (
    <div>
      <input
        type="text"
        id="communityID"
        placeholder="コミュニティID兼timelineModelのpost_id"
        value={communityID}
        onChange={(e) => setCommunityID(e.target.value)}
      />
      <input
        type="text"
        id="userName"
        placeholder="ユーザーID"
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
