type sesisonIdType = string;
type accessTokenType = string;

async function refershToken(sessionId: sesisonIdType): Promise<null | accessTokenType> {
  const token = await fetch(`${process.env.API_ENDPOINT}/api/token/refresh`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json; charset=utf-8",
    },
    body: JSON.stringify({
      session_id: sessionId,
    }),
  }).then((res) => {
    if (!res.ok) {
      return null;
    }
    return res;
  });

  if (token !== null) {
    const tokenData = await token.json();
    return tokenData.access_token;
  }
  return null;
}
