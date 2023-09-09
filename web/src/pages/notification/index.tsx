import getLayout from "@/components/layouts/main";
import NotificationList from "@/components/layouts/main/Notification/NotificationList";
import NotificationIcon from "@/components/layouts/main/Notification/NotificationIcon";

const Notification = () => (
  <>
    <NotificationIcon />
    <NotificationList />
  </>
);

Notification.getLayout = getLayout;

export default Notification;
