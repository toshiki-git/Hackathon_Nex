import axios from "lib/axios";
import getLayout from "@/components/layouts/non_header";
import { Card, CardBody, Input, Button } from "@nextui-org/react";
import { useState } from "react";
import { NextRouter, useRouter } from "next/router";

async function updateUserInfo(
  router: NextRouter,
  username: string,
  display_name: string,
) {
  axios.patch("/api/users/me", {
    username,
    display_name,
  });
  router.push("/home");
}

const Welcome = () => {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [displayName, setDisplayName] = useState("");

  return (
    <div>
      <Card className="min-w-[420px] mx-auto">
        <CardBody>
          <div className="signup">
            <div className="flex flex-wrap md:flex-nowrap mb-6 md:mb-0 gap-4">
              <p>プロフィールを登録</p>
              <Input
                type="text"
                label="表示名"
                onChange={(e) => setDisplayName(e.currentTarget.value)}
                maxLength={50}
              />
              <Input
                type="text"
                label="ユーザー名"
                maxLength={50}
                onChange={(e) => setUsername(e.currentTarget.value)}
              />
            </div>
            <div className="flex flex-wrap justify-end">
              <Button
                color="primary"
                onPress={() => updateUserInfo(router, username, displayName)}
              >
                登録
              </Button>
            </div>
          </div>
        </CardBody>
      </Card>
    </div>
  );
};

Welcome.getLayout = getLayout;

export default Welcome;
