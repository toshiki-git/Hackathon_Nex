import React from "react";
import getLayout from "@/components/layouts/main";
import Prof from "@/components/layouts/main/Prof/Prof";

const Profile = () => (
  <div>
    <Prof />
  </div>
);
Profile.getLayout = getLayout;

export default Profile;
