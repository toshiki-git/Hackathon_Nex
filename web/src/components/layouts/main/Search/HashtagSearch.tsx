import React, { useState } from "react";
import SearchCSS from "./Search.module.scss";

interface HashtagSearchProps {
  setShowResults: (value: boolean) => void;
}

const HashtagSearch: React.FC<HashtagSearchProps> = ({ setShowResults }) => {
  const [hashtag, setHashtag] = useState("");

  const handleSearch = () => {
    // この部分にAPI呼び出しや実際の検索処理を追加する。
    // 現在は必ずPostListコンポーネントが呼び出される。
    setShowResults(true);
  };

  return (
    <div className={`${SearchCSS.hashtag}`}>
      <input
        type="text"
        value={hashtag}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setHashtag(e.target.value)
        }
        placeholder="ハッシュタグで検索..."
        className={`${SearchCSS.input} p-2 border border-foreground rounded bg-overlay`}
      />
      <button
        onClick={handleSearch}
        className="ml-2 p-2 bg-primary text-white rounded-full w-20"
      >
        検索
      </button>
    </div>
  );
};

export default HashtagSearch;
