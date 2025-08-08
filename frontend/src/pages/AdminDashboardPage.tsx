import React, { useEffect, useState } from 'react';
import adminService from '../services/adminService';

interface StatSummary {
  users: number;
  products: number;
  transactions: number;
}

const AdminDashboardPage: React.FC = () => {
  const [stats, setStats] = useState<StatSummary | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await adminService.getStats();
        setStats(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) {
    return <div className="p-6">Loading...</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Admin Dashboard</h1>
      {stats && (
        <div className="grid grid-cols-3 gap-4">
          <div className="p-4 bg-white shadow rounded">Users: {stats.users}</div>
          <div className="p-4 bg-white shadow rounded">Products: {stats.products}</div>
          <div className="p-4 bg-white shadow rounded">Transactions: {stats.transactions}</div>
        </div>
      )}
    </div>
  );
};

export default AdminDashboardPage;
