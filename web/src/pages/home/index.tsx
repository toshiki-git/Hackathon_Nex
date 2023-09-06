import PostArea from "@/components/PostArea";
import PostList from "@/components/PostList";
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
