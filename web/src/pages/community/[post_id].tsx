import { useState } from "react";
import { Button, Textarea } from "@nextui-org/react";
import { useRouter } from "next/router";
import useGetMe from "@/hooks/UserMe";
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
    let userName = userData.id;
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
      <Button id="join_room_btn bg-blue-500" onClick={connectToWebSocket}>
        チャット開始
      </Button>

      <br />
      <br />

      <div id="chat">
        {chatLog.map((msg, index) => {
          const parsedMsg = JSON.parse(msg);
          const { userName, message } = parsedMsg;

          const isCurrentUser = Number(userName) === userData.id;
          const messageStyle = isCurrentUser
            ? "bg-blue-500 text-white shadow-md rounded-xl p-3 ml-10 my-2"
            : "bg-gray-200 text-black shadow-md rounded-xl p-3 mr-10 my-2";

          return (
            <div
              key={index}
              className={`message w-3/4 mx-auto ${messageStyle}`}
              style={{ maxWidth: "80%" }}
            >
              <span className="user-name text-xs font-semibold mb-1">
                {`UserID: ${userName}`}
              </span>
              <div className="text">{message}</div>
            </div>
          );
        })}
      </div>
      <div>
        <h1>Community Post {post_id}</h1>
      </div>
    </div>
  );
}
