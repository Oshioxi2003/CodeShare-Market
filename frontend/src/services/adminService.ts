import api from './api';

export const getStats = async () => {
  const { data } = await api.get('/admin/stats');
  return data;
};

export const getUsers = async () => {
  const { data } = await api.get('/admin/users');
  return data;
};

export const getProducts = async () => {
  const { data } = await api.get('/admin/products');
  return data;
};

export const getTransactions = async () => {
  const { data } = await api.get('/admin/transactions');
  return data;
};

export default { getStats, getUsers, getProducts, getTransactions };
