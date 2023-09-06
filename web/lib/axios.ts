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

export const axiosClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_ENDPOINT,
  headers: {
    "Content-Type": "application/json",
  },
});

export const axiosServer = axios.create({
  baseURL: process.env.API_ENDPOINT,
  headers: {
    "Content-Type": "application/json",
  },
});

const axiosSelf = axios.create({
  baseURL: process.env.HOST,
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosSelf;
