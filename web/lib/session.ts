import type { IronSessionOptions } from "iron-session";

export interface Token {
  token: string;
  refresh_token: string;
}

export interface ErrorResponse {
  status: number;
  error: string;
  message: string;
}

const sessionOptions: IronSessionOptions = {
  password: process.env.SECRET_COOKIE_PASSWORD as string,
  cookieName: "night_g/token",
  cookieOptions: {
    secure: process.env.NODE_ENV === "production",
  },
};

declare module "iron-session" {
  interface IronSessionData {
    token: string;
    refresh_token: string;
  }
}

export default sessionOptions;
