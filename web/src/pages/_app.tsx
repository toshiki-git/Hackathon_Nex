/* eslint-disable react/jsx-props-no-spreading */
import "@/styles/globals.css";
import { Noto_Sans_JP } from "next/font/google";
import "@/components/layouts/Header/Header.scss";
import Header from "@/components/layouts/Header/Header";

import type { AppProps } from "next/app";
import { NextUIProvider } from "@nextui-org/react";
import { ThemeProvider as NextThemesProvider } from "next-themes";

const notoSansJapanese = Noto_Sans_JP({
  subsets: ["latin"],
});

const App = ({ Component, pageProps }: AppProps) => (
  <NextUIProvider>
    <NextThemesProvider attribute="class" defaultTheme="dark" enableSystem={false}>
      <div className={`${notoSansJapanese.className}`}>
        <Header />
        <main className="w-full max-w-[45rem] mx-auto my-2">
          <Component {...pageProps} />
        </main>
      </div>
    </NextThemesProvider>
  </NextUIProvider>
);

export default App;
