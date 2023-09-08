import PostArea from "@/components/PostArea";
import PostList from "@/components/PostList";
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
