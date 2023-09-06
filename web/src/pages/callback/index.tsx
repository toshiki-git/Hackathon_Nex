import axios from "lib/axios";
import Axios from "axios";
import { withIronSessionSsr } from "iron-session/next";
import sessionOptions from "lib/session";
import { GetServerSidePropsContext, GetServerSidePropsResult } from "next";

export const getServerSideProps = withIronSessionSsr(
  async ({
    req,
    query,
  }: GetServerSidePropsContext): Promise<
    GetServerSidePropsResult<{ [key: string]: unknown }>
  > => {
    try {
      const request = await axios.post("/api/token", {
        key_token: query.key_token as string,
      });

      const { data } = request;
      req.session.token = data.token;
      req.session.refresh_token = data.refresh_token;
      await req.session.save();
      return {
        redirect: {
          permanent: false,
          destination: "/home",
        },
      };
    } catch (err) {
      if (Axios.isAxiosError(err) && err.response) {
        return {
          props: {
            error: {
              status: err.response.status,
              statusText: err.response.statusText,
              data: err.response.data,
            },
          },
        };
      }

      return {
        props: {
          error: {
            status: 500,
            statusText: "Internal Server Error",
            data: { detail: "An error occurred." },
          },
        },
      };
    }
  },
  sessionOptions,
);

const Callback = ({
  error,
}: {
  error: { status: number; statusText: string; data: { detail: string } };
}) => (
  <div>
    <h1>
      {error.status} - {error.statusText}
    </h1>
    <p>{error.data.detail}</p>
  </div>
);

export default Callback;
