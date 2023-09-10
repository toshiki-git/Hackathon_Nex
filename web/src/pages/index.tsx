import { Button, Card, CardBody, CardHeader } from "@nextui-org/react";
import getLayout from "@/components/layouts/non_header";
import { FcGoogle } from "react-icons/fc";
import { useRouter } from "next/router";

const Login = () => {
  const router = useRouter();
  const apiEndpoint = `${process.env.NEXT_PUBLIC_API_ENDPOINT}`;
  function redirectGoogleLogin() {
    router.push(`${apiEndpoint}/api/auth/google/login`);
  }

  return (
    <Card className="min-w-[22rem] mx-auto">
      <CardHeader>
        <h1>Login</h1>
      </CardHeader>
      <CardBody>
        <Button
          variant="bordered"
          startContent={<FcGoogle />}
          onPress={() => {
            redirectGoogleLogin();
          }}
        >
          Login with Google
        </Button>
      </CardBody>
    </Card>
  );
};

Login.getLayout = getLayout;

export default Login;
