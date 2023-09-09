import React, { useState } from "react";

const HashtagSearch: React.FC = () => {
  const [hashtag, setHashtag] = useState("");

  return (
    <div className="mb-4">
      <input
        type="text"
        value={hashtag}
        onChange={(e) => setHashtag(e.target.value)}
        placeholder="ハッシュタグで検索..."
        className="p-2 w-4/5 border border-foreground rounded bg-overlay"
      />
      <button className="ml-2 p-2 bg-primary text-white rounded-full w-20">検索</button>
    </div>
  );
};

export default HashtagSearch;
