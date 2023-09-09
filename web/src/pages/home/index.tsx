import PostArea from "@/components/layouts/main/Post/PostArea";
import PostList from "@/components/layouts/main/Post/PostList";
import getLayout from "@/components/layouts/main";
import React from "react";

const Home = () => (
  <div>
    <PostArea />
    <PostList />
  </div>
);

Home.getLayout = getLayout;

export default Home;
