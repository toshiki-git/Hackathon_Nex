import React, { useState } from "react";

interface ContentSearchProps {
  setShowResults: (value: boolean) => void;
}

const ContentSearch: React.FC<ContentSearchProps> = ({ setShowResults }) => {
  const [content, setContent] = useState("");

  const handleSearch = () => {
    // この部分にAPI呼び出しや実際の検索処理を追加する。
    // 現在は必ずPostListコンポーネントが呼び出される。
    setShowResults(true);
  };

  return (
    <div className="mb-4">
      <input
        type="text"
        value={content}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setContent(e.target.value)
        }
        placeholder="内容で検索..."
        className="p-2 w-4/5 border border-foreground rounded bg-overlay"
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

export default ContentSearch;
