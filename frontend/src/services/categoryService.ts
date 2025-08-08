import api from './api';

export interface Category {
  id: number;
  name: string;
  slug: string;
}

export interface CategoryListResponse {
  items: Category[];
  total: number;
}

class CategoryService {
  async list(): Promise<CategoryListResponse> {
    const { data } = await api.get<CategoryListResponse>('/categories');
    return data;
  }
}

export const categoryService = new CategoryService();
