import api from './api';

export interface ContactPayload {
  name: string;
  email: string;
  subject: string;
  message: string;
}

class SupportService {
  async submitContact(payload: ContactPayload): Promise<void> {
    // Attempt to call backend endpoint; UI will handle any errors.
    await api.post('/support/contact', payload);
  }
}

export const supportService = new SupportService();
