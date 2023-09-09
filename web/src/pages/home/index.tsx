import PostArea from "@/components/layouts/main/Post/PostArea";
import PostList from "@/components/layouts/main/Post/PostList";
import getLayout from "@/components/layouts/main";
import LoginRequired from "@/components/utils/LoginRequired";
import React from "react";

const Home = () => (
  <div>
    <LoginRequired />
    <PostArea />
    <PostList />
  </div>
);

Home.getLayout = getLayout;

export default Home;
