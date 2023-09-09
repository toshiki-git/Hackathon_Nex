import React, { useState } from "react";

const ContentSearch: React.FC = () => {
  const [content, setContent] = useState("");

  return (
    <div className="mb-4">
      <input
        type="text"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="内容で検索..."
        className="p-2 w-4/5 border border-foreground rounded bg-overlay"
      />
      <button className="ml-2 p-2 bg-primary text-white rounded-full w-20">検索</button>
    </div>
  );
};

export default ContentSearch;
