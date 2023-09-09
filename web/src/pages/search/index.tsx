import React, { useState } from "react";
import getLayout from "@/components/layouts/main";
import LoginRequired from "@/components/utils/LoginRequired";
import ContentSearch from "@/components/layouts/main/Search/ContentSearch";
import HashtagSearch from "@/components/layouts/main/Search/HashtagSearch";
import { BsSearch } from "react-icons/bs";
import PostList from "@/components/layouts/main/Post/PostList";

const Search = () => {
  const [showResults, setShowResults] = useState(false);

  return (
    <>
      <LoginRequired />
      <div className="flex items-center text-4xl font-bold text-foreground mt-6 mb-4">
        <BsSearch className="mr-2" /> 検索
      </div>
      <HashtagSearch setShowResults={setShowResults} />
      <ContentSearch setShowResults={setShowResults} />
      {showResults && <PostList />}
    </>
  );
};

Search.getLayout = getLayout;

export default Search;
