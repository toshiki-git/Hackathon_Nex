import { ReactElement } from "react";
import Header from "./Header/Header";

type LayoutProps = Required<{
  readonly children: ReactElement;
}>;

export const Layout = ({ children }: LayoutProps) => (
  <>
    <Header />
    <main className="w-full max-w-[45rem] mx-auto my-2">{children}</main>
  </>
);

const getLayout = (page: React.ReactElement) => <Layout>{page}</Layout>;

export default getLayout;
