import Link from "next/link";
import { RegisterForm } from "@/components/forms/RegisterForm";

export default function RegisterPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-6 bg-gray-50">
      <div className="w-full max-w-sm">
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold text-gray-900">Create an Account</h1>
          <p className="text-gray-500">Enter your details to get started</p>
        </div>
        <RegisterForm />
        <p className="mt-4 px-8 text-center text-sm text-gray-500">
          Already have an account?{" "}
          <Link href="/auth/login" className="underline underline-offset-4 hover:text-aurora-600">
            Log in
          </Link>
        </p>
      </div>
    </div>
  );
}
