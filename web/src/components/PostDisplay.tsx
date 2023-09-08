import React from "react";
import postAreaCSS from "./PostArea.module.scss";

interface PostProps {
  content: string;
  hashtags: string;
  image?: string;
}

const PostDisplay: React.FC<PostProps> = ({ content, hashtags, image }) => {
  return (
    <div className={`${postAreaCSS.postArea} bg-overlay p-4 rounded-md mt-4`}>
      <div className="mb-2 text-foreground">
        <p>{hashtags}</p>
      </div>

      <div className="mb-2 text-foreground">
        <p>{content}</p>
      </div>
      {image && (
        <div className="image-section mt-3">
          <img
            className="rounded-md w-72 h-48 object-cover"
            src={image}
            alt="投稿画像"
          />
        </div>
      )}
    </div>
  );
};

export default PostDisplay;
