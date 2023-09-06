import React from "react";
import SignUp from "@/components/layouts/main/SignUp/SignUp";
import getLayout from "@/components/layouts/main";

const Welcome = () => (
  <div>
    <SignUp />
  </div>
);

Welcome.getLayout = getLayout;

export default Welcome;
