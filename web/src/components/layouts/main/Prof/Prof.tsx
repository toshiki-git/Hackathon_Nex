import React from "react";
import useGetMe from "@/hooks/UserMe";
import ProfItem from "./ProfItem";

const Prof = () => {
  const { userData } = useGetMe();
  return (
    <div>
      <ProfItem
        display_name={userData.display_name}
        username={userData.username}
        birthday="2000/01/01"
        image="https://avatars.githubusercontent.com/u/30373425?v=4"
      />
    </div>
  );
};

export default Prof;
