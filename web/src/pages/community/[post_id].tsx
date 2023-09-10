import { useState } from "react";
import { Button, Textarea } from "@nextui-org/react";
import { useRouter } from "next/router";
import useGetMe from "@/hooks/UserMe";
import { Chat } from "@/components/layouts/main/Chat/Chat";
let socket: WebSocket | null = null;

export default function Home() {
  const [userName, setUserName] = useState("");
  const [message, setMessage] = useState("");
  const [chatLog, setChatLog] = useState<string[]>([]);
  const router = useRouter();
  const { post_id } = router.query;

  const { userData } = useGetMe();

  const connectToWebSocket = () => {
    const wsUrl = `ws://localhost:8000/ws/${post_id}`;

    socket = new WebSocket(wsUrl);
    socket.onmessage = (event) => {
      const message = event.data;
      console.log(event.data);
      displayMessage(message);
    };

    // websocket接続したとき
    socket.onopen = () => {
      console.log("チャット開始");
      console.log(userData);
      // 過去のデーター取得
      fetch(`http://localhost:8000/api/community/?community_id=${post_id}`, {
        method: "GET",
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTPエラー");
          }
          return response.json();
        })
        .then((data) => {
          // 過去のコメント出力
          console.log(data);
        })
        .catch((error) => {
          console.error("HTTP GETリクエストエラー:", error);
        });
    };
  };

  // リアルタイムチャットを送った時
  const sendMessage = () => {
    console.log("a");
    if (socket) {
      const dataToSend = {
        message,
        userName,
      };
      socket.send(JSON.stringify(dataToSend));
      setMessage("");

      // チャット内容データーベースに保存
      fetch("http://localhost:8000/api/community/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: userName,
          community_id: post_id,
          content: message,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTPエラー");
          }
        })
        .catch((error) => {
          console.error("HTTP POSTリクエストエラー:", error);
        });
    }
  };

  const displayMessage = (message: string) => {
    setChatLog((prevChatLog) => [...prevChatLog, message]);
  };

  return (
    <div>
      <div className="flex-1 rounded-md p-1 mb-2 text-foreground placeholder-focus">
        <Textarea
          placeholder="投稿内容"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
      </div>
      <Button color="primary" onClick={sendMessage}>
        投稿
      </Button>
      <input
        type="text"
        id="userName"
        placeholder="ユーザーID"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
      />
      <button id="join_room_btn" onClick={connectToWebSocket}>
        入室
      </button>

      <br />
      <br />

      <div id="chat">
        {chatLog.map((msg, index) => (
          <div
            key={index}
            className={`message ${
              JSON.parse(msg).userName === userData.id
                ? "bg-blue-500 text-white rounded-tl-lg rounded-bl-lg rounded-br-lg p-2 ml-auto mb-2"
                : "bg-overlay text-black rounded-tr-lg rounded-tl-lg rounded-br-lg p-2 mr-auto mb-2"
            }`}
            style={{
              maxWidth: "80%",
            }}
          >
            <span className="user-name text-foreground font-bold mb-1">
              {`UserID: ${JSON.parse(msg).userName}`}
            </span>
            <div className="text text-foreground">{JSON.parse(msg).message}</div>
          </div>
        ))}
      </div>
      <div>
        <h1>Community Post {post_id}</h1>
      </div>
    </div>
  );
}
