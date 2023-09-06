/* eslint no-param-reassign: "error" */
import axios from "axios";

const instance = axios.create();

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
