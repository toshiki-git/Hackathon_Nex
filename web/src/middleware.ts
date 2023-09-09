import { NextRequest, NextResponse } from "next/server";

type SessisonIdType = string;
type AccessTokenType = string;

async function refershToken(
  sessionId: SessisonIdType,
): Promise<undefined | AccessTokenType> {
  const token = await fetch(`${process.env.API_ENDPOINT}/api/token/refresh`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json; charset=utf-8",
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

async function middleware(request: NextRequest) {
  const response = await NextResponse.next();
  const sessionId: SessisonIdType | undefined =
    request.cookies.get("session_id")?.value;
  let accessToken: AccessTokenType | undefined =
    request.cookies.get("access_token")?.value;

  if (sessionId === undefined) {
    return redirectToLoginPage(request);
  }

  // If accessToken is not validated or null.
  if (
    accessToken === undefined ||
    (accessToken !== undefined && !(await checkAuth(accessToken)))
  ) {
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

    return response;
  }

  return response;
}

export const config = {
  matcher: ["/home", "/search", "/notifications", "/profile"],
};

export default middleware;
