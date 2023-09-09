import React, { useState } from "react";
import getLayout from "@/components/layouts/main";
import ContentSearch from "@/components/layouts/main/Search/ContentSearch";
import HashtagSearch from "@/components/layouts/main/Search/HashtagSearch";
import PostList from "@/components/layouts/main/Post/PostList";
import SearchIcon from "@/components/layouts/main/Search/SearchIcon";

const Search = () => {
  const [showResults, setShowResults] = useState(false);

  return (
    <>
      <SearchIcon />
      <HashtagSearch setShowResults={setShowResults} />
      <ContentSearch setShowResults={setShowResults} />
      {showResults && <PostList />}
    </>
  );
};

Search.getLayout = getLayout;

export default Search;
