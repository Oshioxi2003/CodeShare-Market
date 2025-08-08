import api from './api';
import { AxiosResponse } from 'axios';

export interface Product {
  id: number;
  title: string;
  slug: string;
  price: number;
  currency: string;
  rating?: number;
  total_reviews?: number;
  demo_url?: string | null;
  created_at: string;
}

export interface ProductDetail extends Product {
  description: string;
  short_description?: string | null;
  programming_language?: string | null;
  framework?: string | null;
  github_url?: string | null;
  seller_id: number;
  category_id?: number | null;
}

export interface Paginated<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
}

class ProductService {
  async list(params?: { q?: string; category_id?: number; page?: number; page_size?: number }): Promise<Paginated<Product>> {
    const { data } = await api.get<Paginated<Product>>('/products', { params });
    return data;
  }
  async get(productId: number): Promise<ProductDetail> {
    const { data } = await api.get<ProductDetail>(`/products/${productId}`);
    return data;
  }
}

export const productService = new ProductService();
