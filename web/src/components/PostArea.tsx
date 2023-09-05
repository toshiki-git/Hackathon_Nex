import React, { useRef, useState } from "react";
import { Button, Textarea } from "@nextui-org/react";
import { CameraIcon } from "./CameraIcon";

const PostArea: React.FC = () => {
  const [content, setContent] = useState<string>("");
  const [hashtags, setHashtags] = useState<string>("");
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const imagePreviewUrl = selectedImage ? URL.createObjectURL(selectedImage) : null;

  const handleImageUpload = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files ? e.target.files[0] : null;
    setSelectedImage(file);
  };

  const handlePost = () => {
    // 投稿処理をここに書く
  };

  return (
    <div className="bg-gray-800 p-4 rounded-md">
      <div className="text-xl text-white mb-4">投稿</div>
      <div className="flex">
        <div className="flex-1">
          <Textarea
            minRows={1}
            placeholder="#ハッシュタグ"
            value={hashtags}
            className="bg-gray-700 border border-gray-600 rounded-md p-1 mb-2 text-white placeholder-gray-400"
            onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
              setHashtags(e.target.value)
            }
          />
          <Textarea
            placeholder="投稿内容"
            value={content}
            className="w-full bg-gray-700 border border-gray-600 rounded-md p-1 text-white placeholder-gray-400"
            onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
              setContent(e.target.value)
            }
          />
        </div>
      </div>
      <div className="mt-3 ml-2 flex justify-between items-center">
        <div className="flex items-center">
          <Button
            onClick={handleImageUpload}
            isIconOnly
            color="warning"
            variant="faded"
            aria-label="画像をアップロード"
            className="mr-2 bg-gray-700 hover:bg-gray-600"
          >
            <CameraIcon />
          </Button>
          {selectedImage && imagePreviewUrl && (
            <div className="flex">
              <img
                className="mr-1"
                src={imagePreviewUrl}
                alt="Selected preview"
                style={{
                  width: "30px",
                  height: "30px",
                  objectFit: "cover",
                }}
              />
              <p className="text-white ml-1">{selectedImage.name}が選択されました。</p>
            </div>
          )}
        </div>

        <Button color="primary" onClick={handlePost}>
          投稿
        </Button>
      </div>

      <input
        ref={fileInputRef}
        type="file"
        className="hidden"
        accept="image/*"
        onChange={handleImageChange}
      />
    </div>
  );
};

export default PostArea;
