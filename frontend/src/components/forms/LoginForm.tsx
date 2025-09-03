"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/store/authStore";
import api from "@/lib/api";
import { AuthToken, User } from "@/lib/types";

const loginSchema = z.object({
  email: z.string().email({ message: "Invalid email address." }),
  password: z.string().min(1, { message: "Password is required." }),
});

type LoginFormValues = z.infer<typeof loginSchema>;

export function LoginForm() {
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();
  const login = useAuthStore((state) => state.login);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
  });

  async function onSubmit(data: LoginFormValues) {
    setError(null);
    try {
      // Step 1: Log the user in to get the token
      const tokenResponse = await api.post<AuthToken>("/auth/login", new URLSearchParams({
        username: data.email,
        password: data.password,
      }));
      const { access_token } = tokenResponse.data;

      // Step 2: Use the token to fetch the user data
      const userResponse = await api.get<User>("/auth/me", {
        headers: { Authorization: `Bearer ${access_token}` }
      });
      const user = userResponse.data;

      // Step 3: Update the auth store
      login(access_token, user);

      router.push("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "An unexpected error occurred.");
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div className="grid gap-2">
        <div>
          <Input
            id="email"
            placeholder="name@example.com"
            type="email"
            autoCapitalize="none"
            autoComplete="email"
            autoCorrect="off"
            disabled={isSubmitting}
            {...register("email")}
          />
          {errors?.email && <p className="px-1 text-xs text-red-600">{errors.email.message}</p>}
        </div>
        <div>
          <Input
            id="password"
            placeholder="password"
            type="password"
            disabled={isSubmitting}
            {...register("password")}
          />
          {errors?.password && <p className="px-1 text-xs text-red-600">{errors.password.message}</p>}
        </div>
        {error && <p className="text-sm font-medium text-red-600">{error}</p>}
        <Button disabled={isSubmitting} className="w-full">
          {isSubmitting ? "Signing In..." : "Sign In"}
        </Button>
      </div>
    </form>
  );
}
