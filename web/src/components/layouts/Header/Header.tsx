import {
  User,
  Avatar,
  Dropdown,
  DropdownTrigger,
  DropdownMenu,
  DropdownItem,
  useDisclosure,
} from "@nextui-org/react";

import { GrMoreVertical } from "react-icons/gr";
import { TbLogout2 } from "react-icons/tb";
import {
  BsFillPersonFill,
  BsMoonStarsFill,
  BsFillSunFill,
  BsBellFill,
  BsSearch,
} from "react-icons/bs";
import { IoSettingsSharp, IoGameController } from "react-icons/io5";
import { useTheme } from "next-themes";
import React from "react";

import useSwitchTheme from "@/utils/theme";
import MenuTab from "./HeaderItem";
import AccoutModal from "./AccoutModal";

const headerItemList = [
  {
    id: 1,
    name: "タイムライン",
    icon: <IoGameController />,
    url: "/home",
  },
  {
    id: 2,
    name: "通知",
    icon: <BsBellFill />,
    url: "/notification",
  },
  {
    id: 3,
    name: "検索",
    icon: <BsSearch />,
    url: "/search",
  },
];

const HeaderItem = () => {
  const headerReactNodeList = headerItemList.map((headerItem) => (
    <MenuTab
      key={headerItem.id}
      name={headerItem.name}
      icon={headerItem.icon}
      url={headerItem.url}
    />
  ));

  return headerReactNodeList;
};

const Header = () => {
  const { theme } = useTheme();
  const {
    isOpen: isAccountModalOpen,
    onOpen: openAccountModal,
    onClose: closeAccountModal,
  } = useDisclosure();
  return (
    <header className="header bg-overlay border-slate-600">
      <div className="header__items">
        <HeaderItem />
      </div>
      <Dropdown>
        <DropdownTrigger>
          <div className="header__icon">
            <div className="header__icon__pc rounded-lg my-2 py-2 px-3 hover:bg-white/[.06]">
              <User
                name="Junior Garcia"
                classNames={{
                  wrapper: "pl-3",
                  description: "text-primary",
                }}
                description="@jrgarciadev"
                avatarProps={{
                  src: "https://avatars.githubusercontent.com/u/30373425?v=4",
                }}
              />
              <GrMoreVertical size={20} />
            </div>
            <Avatar
              className="my-2 w-8 h-8 header__icon__sm"
              src="https://avatars.githubusercontent.com/u/30373425?v=4"
              size="md"
            />
          </div>
        </DropdownTrigger>
        <DropdownMenu variant="faded" aria-label="Static Actions">
          <DropdownItem key="profile" startContent={<BsFillPersonFill />}>
            プロフィール
          </DropdownItem>
          <DropdownItem
            onPress={openAccountModal}
            key="edit"
            startContent={<IoSettingsSharp />}
          >
            アカウント設定
          </DropdownItem>
          <DropdownItem
            key="copy"
            onClick={useSwitchTheme()}
            startContent={theme === "dark" ? <BsFillSunFill /> : <BsMoonStarsFill />}
          >
            テーマ変更
          </DropdownItem>
          <DropdownItem
            key="delete"
            className="text-danger"
            color="danger"
            startContent={<TbLogout2 />}
          >
            ログアウト
          </DropdownItem>
        </DropdownMenu>
      </Dropdown>

      <AccoutModal isOpen={isAccountModalOpen} onClose={closeAccountModal} />
    </header>
  );
};

export default Header;
