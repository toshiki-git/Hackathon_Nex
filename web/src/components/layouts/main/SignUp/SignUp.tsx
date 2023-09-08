import React from "react";
import { Input, Avatar, Button } from "@nextui-org/react";

const SignUp = () => (
  <div className="signup">
    <div className="flex w-full flex-wrap md:flex-nowrap mb-6 md:mb-0 gap-4">
      <p>プロフィールを登録</p>
      <Input type="text" label="表示名" maxLength={50} />
      <Input type="text" label="ユーザー名" />
      <Input type="text" label="誕生日 yyyy/mm/dd" />
      <div className="flex gap-10 items-center justify-center">
        <Avatar src="{}" className="w-20 h-20 text-large" />
        <input type="file" label="アイコン" />
      </div>
    </div>
    <div className="flex flex-wrap justify-end">
      <Button color="primary">登録</Button>
    </div>
  </div>
);

export default SignUp;
