import React from "react";
import { PiBalloon } from "react-icons/pi";
import PostList from "../Post/PostList";

type ProfProps = {
  name: string;
  userName: string;
  birthday: string;
  image?: string;
};

const ProfItem = ({ name, userName, birthday, image }: ProfProps) => {
  return (
    <div>
      <div className="flex flex-col  space-y-4 pb-4 border-b-1 pt-20">
        <div className="h-20">
          <img src={image} className="rounded-full h-20" />
        </div>

        <div className="items-center">
          <div className="text-xl font-bold">{name}</div>
          <div className="text-sm text-slate-400">@{userName}</div>
        </div>
        <div className="flex items-center">
          <PiBalloon size={20} />
          <div className="text-sm">誕生日:{birthday}</div>
        </div>
        <p className="pt-10">過去の投稿</p>
      </div>
      <PostList />
    </div>
  );
};

export default ProfItem;
