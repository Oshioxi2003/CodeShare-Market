import api from './api';

export interface UploadResponse {
  filename: string;
  stored_as: string;
  size: number;
}

class UploadService {
  async uploadFile(file: File): Promise<UploadResponse> {
    const formData = new FormData();
    formData.append('file', file);

    const { data } = await api.post<UploadResponse>('/upload/file', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    return data;
  }
}

export const uploadService = new UploadService();
