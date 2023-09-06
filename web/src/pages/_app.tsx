/* eslint-disable react/jsx-props-no-spreading */
import "@/styles/globals.css";
import { Noto_Sans_JP } from "next/font/google";
import { NextPage } from "next";
import { AppProps } from "next/app";
import { NextUIProvider } from "@nextui-org/react";
import { ThemeProvider as NextThemesProvider } from "next-themes";
import { ReactElement } from "react";

const notoSansJapanese = Noto_Sans_JP({
  subsets: ["latin"],
});

type NextPageWithLayout = NextPage & {
  getLayout?: (page: React.ReactElement) => React.ReactNode;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

const App = ({ Component, pageProps }: AppPropsWithLayout) => {
  const getLayout = Component.getLayout ?? ((page) => page);

  return (
    <NextUIProvider>
      <NextThemesProvider attribute="class" defaultTheme="dark" enableSystem={false}>
        <div className={`${notoSansJapanese.className}`}>
          {getLayout(<Component {...pageProps} />)}
        </div>
      </NextThemesProvider>
    </NextUIProvider>
  );
};

export default App;
