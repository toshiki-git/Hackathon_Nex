import getLayout from "@/components/layouts/main";
import LoginRequired from "@/components/utils/LoginRequired";

const Search = () => (
  <>
    <LoginRequired />
    <h1>Search</h1>
  </>
);

Search.getLayout = getLayout;

export default Search;
