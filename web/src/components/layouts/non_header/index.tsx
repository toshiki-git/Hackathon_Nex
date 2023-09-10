import { ReactElement } from "react";

type LayoutProps = Required<{
  readonly children: ReactElement;
}>;

export const Layout = ({ children }: LayoutProps) => (
  <main className="w-full min-h-screen my-4 flex-col flex items-center">
    {children}
  </main>
);

const getLayout = (page: React.ReactElement) => <Layout>{page}</Layout>;

export default getLayout;
