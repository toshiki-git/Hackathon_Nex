import axios from "lib/axios";
import { useEffect } from "react";

const checkAuth = () => {
  axios.get("/api/auth/jwt_verify");
};

const LoginRequired = () => {
  useEffect(() => {
    checkAuth();
  }, []);

  return null;
};

export default LoginRequired;
