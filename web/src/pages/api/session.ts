import { withIronSessionApiRoute } from "iron-session/next";
import sessionOptions from "lib/session";
import { NextApiRequest, NextApiResponse } from "next";
import { Token } from "lib/axios";

interface ErrorResponse {
  detail: string;
}

async function tokenRoute(
  req: NextApiRequest,
  res: NextApiResponse<Token | ErrorResponse>,
) {
  if (req.session.auth.refresh_token && req.session.auth.token) {
    res.json({
      ...req.session.auth,
    });
  } else {
    res.status(401).json({ detail: "Authentication information not found." });
  }
}

export default withIronSessionApiRoute(tokenRoute, sessionOptions);
