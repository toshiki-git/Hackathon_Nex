import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

type RefreshTokenResponse = {
  access_token: string;
};

async function getNewAccessToken(
  sessionId: string | undefined | void,
): Promise<string | void> {
  const userData = await fetch(`${process.env.API_ENDPOINT}/api/token/refresh`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      session_id: sessionId,
    }),
  })
    .then(async (res) => {
      if (!res.ok) {
        switch (res.status) {
          case 401:
            throw new Error("Ivalid Session id");
          default:
            throw new Error(res.statusText);
        }
      }
      const resData: RefreshTokenResponse = await res.json();
      const newAccessToken = resData.access_token;

      return newAccessToken;
    })
    .catch(() => ({ redirect: true }));
  return { user_data: await userData, access_token: undefined, redirect: false };
}
async function getUserInfo(
  sessionId: string | undefined | void,
  accessToken: string | undefined | void,
) {
  if (accessToken === undefined) {
    // eslint-disable-next-line no-param-reassign
    accessToken = await getNewAccessToken(sessionId);
  }

  const user = await fetch(`${process.env.API_ENDPOINT}/api/auth/jwt_verify`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
  })
    .then(async (res) => {
      if (!res.ok) {
        throw new Error(res.statusText);
      }
      return res.json();
    })
    .catch(() => ({ redirect: true, access_token: undefined, user_data: undefined }));

  // eslint-disable-next-line @typescript-eslint/return-await
  return { user_data: await user, access_token: accessToken, redirect: false };
}

export async function middleware(request: NextRequest) {
  const response = NextResponse.next();
  const sessionId = request.cookies.get("session_id")?.value;
  const accessToken = request.cookies.get("access_token")?.value;
  let newAccessToken: string | undefined | void = "";

  const user = await getUserInfo(sessionId, accessToken).catch(async () => {
    newAccessToken = await getNewAccessToken(sessionId);
    try {
      const userWithNewToken = await getUserInfo(sessionId, newAccessToken);
      const userData = {
        user_data: await userWithNewToken.user_data.json(),
        access_token: newAccessToken,
        redirect: false,
      };
      return userData;
    } catch (err) {
      return { redirect: true, access_token: undefined, user_data: undefined };
    }
  });

  if (user.redirect) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  if (typeof user.access_token === "string" && user.access_token !== undefined) {
    response.cookies.set({
      name: "access_token",
      value: user.access_token,
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "strict",
      domain: request.nextUrl.domainLocale?.domain,
    });
  }

  return response;
}

export const config = {
  matcher: ["/home", "/search", "/notifications", "/profile"],
};
