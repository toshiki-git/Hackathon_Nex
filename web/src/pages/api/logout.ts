import { withIronSessionApiRoute } from "iron-session/next";
import sessionOptions from "lib/session";
import { NextApiRequest, NextApiResponse } from "next";

const logoutRoute = (req: NextApiRequest, res: NextApiResponse) => {
  req.session.destroy();
  res.json({ message: "Successfully logged out" });
};

export default withIronSessionApiRoute(logoutRoute, sessionOptions);
