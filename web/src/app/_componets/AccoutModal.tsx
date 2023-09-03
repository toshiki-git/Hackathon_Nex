import React from 'react';
import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
} from '@nextui-org/react';

type AccoutModalProps = {
  isOpen: boolean;
  onOpen: () => void;
  onClose: () => void;
};

const AccoutModal: React.FC<AccoutModalProps> = ({
  isOpen,
  onOpen,
  onClose,
}) => {
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
        {(onClose) => (
          <>
            <ModalHeader className="flex flex-col gap-1">
              アカウント設定
            </ModalHeader>
            <ModalBody>
              <div className="icon-change-form mb-6">
                <label
                  htmlFor="iconUpload"
                  className="block text-gray-600 text-sm font-semibold mb-2"
                >
                  アイコンを変更:
                </label>
                <div className="mt-1 flex items-center p-2 border border-gray-300 rounded-lg bg-white hover:border-gray-400">
                  <input
                    type="file"
                    id="iconUpload"
                    name="iconUpload"
                    className="w-full text-gray-600 focus:outline-none"
                  />
                </div>
              </div>

              <div className="name-change-form">
                <label
                  htmlFor="username"
                  className="block text-gray-600 text-sm font-semibold mb-2"
                >
                  名前を変更:
                </label>
                <div className="mt-1 relative rounded-lg shadow-sm">
                  <input
                    type="text"
                    id="username"
                    name="username"
                    placeholder="変更名"
                    className="form-input block w-full px-4 py-2 text-gray-600 bg-white border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500 focus:shadow-outline-indigo"
                  />
                </div>
              </div>
            </ModalBody>
            <ModalFooter>
              <Button
                color="danger"
                variant="light"
                onPress={onClose}
              >
                Close
              </Button>
              <Button color="primary" onPress={onClose}>
                Action
              </Button>
            </ModalFooter>
          </>
        )}
      </ModalContent>
    </Modal>
  );
};

export default AccoutModal;
