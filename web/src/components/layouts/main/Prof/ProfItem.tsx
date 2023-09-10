import React from "react";
import { PiBalloon } from "react-icons/pi";
import { UserDataType } from "lib/types";
import PostList from "../Post/PostList";
import ProfCSS from "./Prof.module.scss";

interface PropsType extends UserDataType {
  birthday: string;
  image: string;
}

const ProfItem = ({ display_name, username, birthday, image }: PropsType) => (
  <div className={`${ProfCSS.profArea}`}>
    <div className="flex flex-col  space-y-4 pb-4 border-b-1 pt-20">
      <div className="h-20">
        <img src={image} className="rounded-full h-20" />
      </div>

      <div className="items-center">
        <div className="text-xl font-bold">{display_name}</div>
        <div className="text-sm text-slate-400">@{username}</div>
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

export default ProfItem;
