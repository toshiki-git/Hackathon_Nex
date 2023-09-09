import getLayout from "@/components/layouts/main";
import LoginRequired from "@/components/utils/LoginRequired";
import ContentSearch from "@/components/layouts/main/Search/ContentSearch";
import HashtagSearch from "@/components/layouts/main/Search/HashtagSearch";
import { BsSearch } from "react-icons/bs";

const Search = () => (
  <>
    <LoginRequired />
    <div className="flex items-center text-4xl font-bold text-foreground mt-6 mb-4">
      <BsSearch className="mr-2" /> 検索
    </div>
    <HashtagSearch />
    <ContentSearch />
  </>
);

Search.getLayout = getLayout;

export default Search;
