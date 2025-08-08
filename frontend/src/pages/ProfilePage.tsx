import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { motion } from 'framer-motion';
import { useAuth } from '../contexts/AuthContext';
import { UserCircleIcon, PencilIcon } from '@heroicons/react/24/outline';
import toast from 'react-hot-toast';

interface ProfileFormData {
  full_name?: string;
  bio?: string;
  website?: string;
  github_url?: string;
  linkedin_url?: string;
}

const ProfilePage: React.FC = () => {
  const { user, updateUser } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<ProfileFormData>({
    defaultValues: {
      full_name: user?.full_name || '',
      bio: user?.bio || '',
      website: user?.website || '',
      github_url: user?.github_url || '',
      linkedin_url: user?.linkedin_url || '',
    },
  });

  const onSubmit = async (data: ProfileFormData) => {
    setIsLoading(true);
    try {
      // TODO: Call API to update profile
      // const updatedUser = await userService.updateProfile(data);
      // updateUser(updatedUser);
      
      // For now, just simulate success
      toast.success('Profile updated successfully!');
      setIsEditing(false);
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to update profile');
    } finally {
      setIsLoading(false);
    }
  };

  const handleEditToggle = () => {
    if (isEditing) {
      reset(); // Reset form to original values
    }
    setIsEditing(!isEditing);
  };

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="max-w-2xl mx-auto"
      >
        <div className="bg-white rounded-xl shadow p-6">
          <div className="flex items-center justify-between mb-6">
            <h1 className="text-3xl font-bold">Profile</h1>
            <button
              onClick={handleEditToggle}
              className="flex items-center space-x-2 text-primary-600 hover:text-primary-700"
            >
              <PencilIcon className="h-5 w-5" />
              <span>{isEditing ? 'Cancel' : 'Edit'}</span>
            </button>
          </div>

          <div className="flex items-center mb-6">
            {user.avatar_url ? (
              <img
                src={user.avatar_url}
                alt={user.username}
                className="h-20 w-20 rounded-full object-cover"
              />
            ) : (
              <UserCircleIcon className="h-20 w-20 text-gray-400" />
            )}
            <div className="ml-4">
              <h2 className="text-xl font-semibold">{user.username}</h2>
              <p className="text-gray-600">{user.email}</p>
              <span className={`inline-block px-2 py-1 rounded text-xs font-medium ${
                user.role === 'admin' ? 'bg-red-100 text-red-800' :
                user.role === 'seller' ? 'bg-blue-100 text-blue-800' :
                'bg-gray-100 text-gray-800'
              }`}>
                {user.role}
              </span>
            </div>
          </div>

          {isEditing ? (
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Full Name
                </label>
                <input
                  {...register('full_name')}
                  className="input-field"
                  placeholder="Your full name"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Bio
                </label>
                <textarea
                  {...register('bio')}
                  className="input-field min-h-[100px]"
                  placeholder="Tell us about yourself..."
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Website
                </label>
                <input
                  {...register('website', {
                    pattern: {
                      value: /^https?:\/\/.+/,
                      message: 'Please enter a valid URL (starting with http:// or https://)',
                    },
                  })}
                  className="input-field"
                  placeholder="https://yourwebsite.com"
                />
                {errors.website && (
                  <p className="mt-1 text-sm text-red-600">{errors.website.message}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  GitHub URL
                </label>
                <input
                  {...register('github_url', {
                    pattern: {
                      value: /^https?:\/\/(www\.)?github\.com\/.+/,
                      message: 'Please enter a valid GitHub URL',
                    },
                  })}
                  className="input-field"
                  placeholder="https://github.com/yourusername"
                />
                {errors.github_url && (
                  <p className="mt-1 text-sm text-red-600">{errors.github_url.message}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  LinkedIn URL
                </label>
                <input
                  {...register('linkedin_url', {
                    pattern: {
                      value: /^https?:\/\/(www\.)?linkedin\.com\/.+/,
                      message: 'Please enter a valid LinkedIn URL',
                    },
                  })}
                  className="input-field"
                  placeholder="https://linkedin.com/in/yourusername"
                />
                {errors.linkedin_url && (
                  <p className="mt-1 text-sm text-red-600">{errors.linkedin_url.message}</p>
                )}
              </div>

              <div className="flex space-x-3 pt-4">
                <button
                  type="submit"
                  disabled={isLoading}
                  className="btn-primary"
                >
                  {isLoading ? 'Saving...' : 'Save Changes'}
                </button>
                <button
                  type="button"
                  onClick={handleEditToggle}
                  className="btn-outline"
                >
                  Cancel
                </button>
              </div>
            </form>
          ) : (
            <div className="space-y-4">
              <div>
                <h3 className="text-sm font-medium text-gray-700">Full Name</h3>
                <p className="text-gray-900">{user.full_name || 'Not provided'}</p>
              </div>

              <div>
                <h3 className="text-sm font-medium text-gray-700">Bio</h3>
                <p className="text-gray-900">{user.bio || 'No bio provided'}</p>
              </div>

              <div>
                <h3 className="text-sm font-medium text-gray-700">Website</h3>
                {user.website ? (
                  <a
                    href={user.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary-600 hover:text-primary-700"
                  >
                    {user.website}
                  </a>
                ) : (
                  <p className="text-gray-900">Not provided</p>
                )}
              </div>

              <div>
                <h3 className="text-sm font-medium text-gray-700">GitHub</h3>
                {user.github_url ? (
                  <a
                    href={user.github_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary-600 hover:text-primary-700"
                  >
                    {user.github_url}
                  </a>
                ) : (
                  <p className="text-gray-900">Not provided</p>
                )}
              </div>

              <div>
                <h3 className="text-sm font-medium text-gray-700">LinkedIn</h3>
                {user.linkedin_url ? (
                  <a
                    href={user.linkedin_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary-600 hover:text-primary-700"
                  >
                    {user.linkedin_url}
                  </a>
                ) : (
                  <p className="text-gray-900">Not provided</p>
                )}
              </div>
            </div>
          )}

          {user.role === 'seller' && (
            <div className="mt-8 pt-6 border-t">
              <h3 className="text-lg font-semibold mb-4">Seller Stats</h3>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                <div className="text-center">
                  <div className="text-2xl font-bold text-primary-600">{user.total_sales || 0}</div>
                  <div className="text-sm text-gray-600">Total Sales</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-primary-600">{user.seller_rating || 0}</div>
                  <div className="text-sm text-gray-600">Rating</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-primary-600">${user.total_earnings || 0}</div>
                  <div className="text-sm text-gray-600">Earnings</div>
                </div>
              </div>
            </div>
          )}
        </div>
      </motion.div>
    </div>
  );
};

export default ProfilePage;