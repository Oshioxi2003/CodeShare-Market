import React, { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { Link, useSearchParams } from 'react-router-dom';
import { productService, Product } from '../services/productService';
import { categoryService } from '../services/categoryService';

const ProductsPage: React.FC = () => {
  const [params, setParams] = useSearchParams();
  const [searchTerm, setSearchTerm] = useState(params.get('q') || '');
  
  const q = params.get('q') || undefined;
  const category = params.get('category_id');
  const category_id = category ? Number(category) : undefined;

  const { data: products, isLoading } = useQuery({
    queryKey: ['products', { q, category_id }],
    queryFn: () => productService.list({ q, category_id }),
  });

  const { data: categories } = useQuery({
    queryKey: ['categories'],
    queryFn: () => categoryService.list(),
  });

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    const newParams = new URLSearchParams(params);
    if (searchTerm.trim()) {
      newParams.set('q', searchTerm.trim());
    } else {
      newParams.delete('q');
    }
    setParams(newParams);
  };

  const handleCategoryFilter = (categoryId: number | null) => {
    const newParams = new URLSearchParams(params);
    if (categoryId) {
      newParams.set('category_id', categoryId.toString());
    } else {
      newParams.delete('category_id');
    }
    setParams(newParams);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Browse Products</h1>

      {/* Search and Filters */}
      <div className="bg-white rounded-xl shadow p-6 mb-8">
        <form onSubmit={handleSearch} className="mb-4">
          <div className="flex gap-4">
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Search products..."
              className="input-field flex-1"
            />
            <button type="submit" className="btn-primary">
              Search
            </button>
          </div>
        </form>

        {/* Category Filter */}
        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => handleCategoryFilter(null)}
            className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
              !category_id
                ? 'bg-primary-600 text-white'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            All Categories
          </button>
          {categories?.items.map(cat => (
            <button
              key={cat.id}
              onClick={() => handleCategoryFilter(cat.id)}
              className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
                category_id === cat.id
                  ? 'bg-primary-600 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              {cat.name}
            </button>
          ))}
        </div>
      </div>

      {/* Results */}
      {isLoading && (
        <div className="flex justify-center items-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
        </div>
      )}

      {products && products.items.length === 0 && (
        <div className="text-center py-12">
          <div className="text-gray-600 text-lg">No products found.</div>
          <p className="text-gray-500 mt-2">Try adjusting your search or filters.</p>
        </div>
      )}

      {products && products.items.length > 0 && (
        <div>
          <div className="flex justify-between items-center mb-6">
            <p className="text-gray-600">
              Showing {products.items.length} of {products.total} products
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {products.items.map((p: Product) => (
              <Link key={p.id} to={`/products/${p.id}`} className="card hover:scale-[1.02] transition-transform">
                <div className="h-40 bg-gradient-to-br from-primary-100 to-secondary-100 rounded-lg mb-4 flex items-center justify-center">
                  <div className="text-4xl font-bold text-primary-600">&lt;/&gt;</div>
                </div>
                <div className="flex justify-between items-start mb-2">
                  <h3 className="text-lg font-semibold line-clamp-2 mr-2">{p.title}</h3>
                  <span className="text-primary-600 font-bold whitespace-nowrap">
                    ${p.price.toFixed(2)}
                  </span>
                </div>
                <div className="flex items-center justify-between text-sm text-gray-500">
                  <div className="flex items-center">
                    <span>⭐ {(p.rating ?? 0).toFixed(1)}</span>
                    <span className="mx-1">•</span>
                    <span>{p.total_reviews ?? 0} reviews</span>
                  </div>
                  <span className="text-xs bg-gray-100 px-2 py-1 rounded">
                    {new Date(p.created_at).toLocaleDateString()}
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ProductsPage;
