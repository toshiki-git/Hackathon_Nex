import getLayout from "@/components/layouts/main";
import LoginRequired from "@/components/utils/LoginRequired";

const Notification = () => (
  <>
    <LoginRequired />
    <h1>Notification</h1>
  </>
);

Notification.getLayout = getLayout;

export default Notification;
