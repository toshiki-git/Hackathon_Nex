import sessionOptions from "lib/session";
import { NextApiRequest, NextApiResponse } from "next";
import { withIronSessionApiRoute } from "iron-session/next";

const logoutRoute = (req: NextApiRequest, res: NextApiResponse) => {
  req.session.destroy();
  res.json({ token: "", refresh_token: "" });
};

export default withIronSessionApiRoute(logoutRoute, sessionOptions);
