/* eslint no-param-reassign: "error" */
import axios from "axios";

const instance = axios.create();

export interface ErrorResponse {
  detail: string;
}

export interface Token {
  token: string;
  refresh_token: string;
}

instance.interceptors.request.use(
  (config) => {
    config.baseURL = process.env.NEXT_PUBLIC_API_ENDPOINT as string;
    return config;
  },
  (error) =>
    // エラー時の処理
    Promise.reject(error),
);

export default instance;
