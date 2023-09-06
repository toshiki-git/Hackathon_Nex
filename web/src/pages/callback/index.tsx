import { useRouter } from "next/router";
import { useEffect, useState } from "react";

const Callback = () => {
  const router = useRouter();
  const { query } = router;
  const [errorData, setErrorData] = useState(null);

  useEffect(() => {
    if (router.isReady) {
      const Login = async () => {
        await fetch("/api/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ key_token: "" }),
        })
          .catch((err) => {
            // eslint-disable-next-line no-console
            console.error(err);
            setErrorData(err);
          })
          .finally(() => {
            if (errorData === null) {
              router.replace("/home");
            }
          });
      };
      Login();
    }
  }, [errorData, query, router, router.isReady]);

  let errorName = <h1>{}</h1>;
  if (errorData) {
    errorName = <h1>{errorData}</h1>;
  }

  return errorName;
};

export default Callback;
