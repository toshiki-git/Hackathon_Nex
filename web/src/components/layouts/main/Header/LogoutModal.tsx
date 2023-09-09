import React from "react";
import axios from "lib/axios";
import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
} from "@nextui-org/react";
import { useRouter } from "next/router";

type LogoutModalProps = {
  isOpen: boolean;
  onClose: () => void;
};

const LogoutModal: React.FC<LogoutModalProps> = ({ isOpen, onClose }) => {
  const router = useRouter();
  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      backdrop="blur"
      size="sm"
      placement="center"
      scrollBehavior="inside"
    >
      <ModalContent>
        <ModalHeader className="flex flex-col gap-1">ログアウトしますか？</ModalHeader>
        <ModalBody>
          <p className="text-gray-400 text-sm font-semibold mb-2">
            ログアウトすると、再度ログインするまでアカウントを利用できなくなります。
          </p>
        </ModalBody>
        <ModalFooter>
          <Button variant="light" onPress={onClose}>
            キャンセル
          </Button>
          <Button
            color="danger"
            variant="light"
            onPress={onClose}
            onClick={async (e) => {
              e.preventDefault();
              await axios.post("/api/auth/logout");
              router.push("/");
            }}
          >
            ログアウト
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
};

export default LogoutModal;
