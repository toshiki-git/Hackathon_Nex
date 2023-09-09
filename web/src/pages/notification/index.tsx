import getLayout from "@/components/layouts/main";
import NotificationList from "@/components/layouts/main/Notification/NotificationList";
import { BsBellFill } from "react-icons/bs";

const Notification = () => (
  <>
    <div className="flex items-center text-4xl font-bold text-foreground mt-6 mb-4">
      <BsBellFill className="mr-2" /> 通知
    </div>
    <NotificationList />
  </>
);

Notification.getLayout = getLayout;

export default Notification;
