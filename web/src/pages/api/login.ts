import axios from "lib/axios";
import Axios from "axios";
import { withIronSessionApiRoute } from "iron-session/next";
import sessionOptions from "lib/session";
import { NextApiRequest, NextApiResponse } from "next";

async function loginRoute(req: NextApiRequest, res: NextApiResponse) {
  const reqBody = await req.body;

  try {
    const response = await axios.post("/api/token", {
      key_token: reqBody.key_token,
    });

    const { data } = response;
    req.session.token = data.token;
    req.session.refresh_token = data.refresh_token;
    await req.session.save();

    res.json({
      token: req.session.token,
      refresh_token: req.session.refresh_token,
    });
  } catch (error) {
    if (Axios.isAxiosError(error) && error.response) {
      res.status(error.response.status).json(error.response.data);
    } else {
      res.status(500).json({ error: "Internal Server Error" });
    }
  }
}

export default withIronSessionApiRoute(loginRoute, sessionOptions);
