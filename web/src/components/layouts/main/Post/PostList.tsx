import React from "react";
import PostDisplay from "./PostDisplay";
import posts from "./temporary_post_data.json";

const PostList = () => {
  return (
    <div>
      {posts.map((post) => (
        <PostDisplay
          key={post.id}
          content={post.content}
          hashtags={post.hashtags}
          image={post.image}
        />
      ))}
    </div>
  );
};

export default PostList;
