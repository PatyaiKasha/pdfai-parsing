// This file contains shared TypeScript types that correspond to the backend's Pydantic schemas.

/**
 * Represents a user's profile information.
 * Corresponds to the `User` schema in `backend/app/schemas/user.py`.
 */
export interface User {
  id: string;
  email: string;
  is_active: boolean;
  plan: 'free' | 'pro' | 'enterprise';
  usage_count: number;
  usage_limit: number;
  created_at: string; // ISO date string
}

/**
 * Represents a PDF parsing job.
 * Corresponds to the `ParseJob` schema in `backend/app/schemas/parse.py`.
 */
export interface ParseJob {
  id: string;
  user_id: string;
  filename: string;
  file_url: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  created_at: string;
  completed_at: string | null;
  error_message: string | null;
  result_data: any | null;
}

/**
 * Represents the authentication token returned upon successful login.
 * Corresponds to the `Token` schema in `backend/app/schemas/auth.py`.
 */
export interface AuthToken {
  access_token: string;
  token_type: string;
}
