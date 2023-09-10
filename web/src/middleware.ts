import { NextRequest, NextResponse } from "next/server";

type SessisonIdType = string;
type AccessTokenType = string;

async function isUserInit(accessToken: AccessTokenType) {
  const userRes = await fetch(`${process.env.API_ENDPOINT}/api/users/me`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
  }).then(async (res) => res);

  const userData = await userRes.json();
  return userData.is_initialized;
}

async function refershToken(
  sessionId: SessisonIdType,
): Promise<undefined | AccessTokenType> {
  const token = await fetch(`${process.env.API_ENDPOINT}/api/token/refresh`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      session_id: sessionId,
    }),
  }).then((res) => (res.ok ? res : undefined));

  if (token !== undefined) {
    const tokenData = await token.json();
    return tokenData.access_token;
  }
  return undefined;
}

async function checkAuth(accessToken: AccessTokenType): Promise<boolean> {
  const isSucceeded = await fetch(`${process.env.API_ENDPOINT}/api/users/me`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
  }).then(async (res) => res.ok);

  return isSucceeded;
}

function redirectToLoginPage(request: NextRequest): NextResponse {
  return NextResponse.redirect(new URL("/", request.url));
}

function redirectToHomePage(request: NextRequest): NextResponse {
  return NextResponse.redirect(new URL("/home", request.url));
}

function redirectToWelcomePage(request: NextRequest): NextResponse {
  return NextResponse.redirect(new URL("/welcome", request.url));
}

async function middleware(request: NextRequest) {
  const response = await NextResponse.next();
  const sessionId: SessisonIdType | undefined =
    request.cookies.get("session_id")?.value;
  let accessToken: AccessTokenType | undefined =
    request.cookies.get("access_token")?.value;

  if (request.nextUrl.pathname === "/" && accessToken !== undefined) {
    if (await checkAuth(accessToken)) {
      return redirectToHomePage(request);
    }

    if (sessionId !== undefined) {
      accessToken = await refershToken(sessionId);
      if (accessToken !== undefined && (await checkAuth(accessToken))) {
        return redirectToHomePage(request);
      }
    }
  }

  // If accessToken is not validated or null.
  if (
    accessToken === undefined ||
    (accessToken !== undefined && !(await checkAuth(accessToken)))
  ) {
    if (sessionId !== undefined) {
      accessToken = await refershToken(sessionId);

      // Check the accessToken was refreshed
      if (
        accessToken === undefined ||
        (accessToken !== undefined && !(await checkAuth(accessToken)))
      ) {
        return redirectToLoginPage(request);
      }
      response.cookies.set({
        name: "access_token",
        value: accessToken,
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "strict",
        domain: request.nextUrl.domainLocale?.domain,
      });
    }
    if (accessToken !== undefined && (await !isUserInit(accessToken))) {
      return redirectToWelcomePage(request);
    }
    return response;
  }

  if (accessToken !== undefined && (await !isUserInit(accessToken))) {
    return redirectToWelcomePage(request);
  }
  return response;
}

export const config = {
  matcher: ["/", "/home", "/search", "/notifications", "/profile"],
};

export default middleware;
