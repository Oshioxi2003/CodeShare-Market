export type UserRole = 'admin' | 'seller' | 'buyer' | 'moderator';

export interface User {
  id: number;
  email: string;
  username: string;
  full_name?: string;
  avatar_url?: string;
  role: UserRole | string;
  is_verified: boolean;
  // optional account flags
  is_active?: boolean;
  is_banned?: boolean;
  created_at?: string;
  updated_at?: string;
  last_login_at?: string | null;

  // optional profile fields
  bio?: string | null;
  website?: string | null;
  github_url?: string | null;
  linkedin_url?: string | null;

  // optional seller stats
  seller_rating?: number | null;
  total_sales?: number | null;
  total_earnings?: number | null;
}



