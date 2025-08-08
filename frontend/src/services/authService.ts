import api from './api';
import { User } from '../types/user';

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

// Use centralized User type from types/user

class AuthService {
  async login(username: string, password: string): Promise<LoginResponse> {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    const response = await api.post<LoginResponse>('/auth/login', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    return response.data;
  }

  async register(
    email: string,
    username: string,
    password: string,
    full_name?: string
  ): Promise<User> {
    const response = await api.post<User>('/auth/register', {
      email,
      username,
      password,
      full_name,
    });
    return response.data;
  }

  async getMe(): Promise<User> {
    const response = await api.get<User>('/auth/me');
    return response.data;
  }

  async logout(): Promise<void> {
    await api.post('/auth/logout');
  }

  async requestPasswordReset(email: string): Promise<void> {
    await api.post('/auth/password-reset', { email });
  }

  async confirmPasswordReset(token: string, newPassword: string): Promise<void> {
    await api.post('/auth/password-reset/confirm', {
      token,
      new_password: newPassword,
    });
  }

  async verifyEmail(token: string): Promise<void> {
    await api.post('/auth/verify-email', { token });
  }
}

export const authService = new AuthService();
