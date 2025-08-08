import React from 'react';
import { useForm } from 'react-hook-form';
import toast from 'react-hot-toast';
import { supportService } from '../services/supportService';

interface ContactForm {
  name: string;
  email: string;
  subject: string;
  message: string;
}

const ContactPage: React.FC = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ContactForm>();

  const onSubmit = async (data: ContactForm) => {
    try {
      await supportService.submitContact(data);
      toast.success('Message sent! We will get back to you soon.');
      reset();
    } catch (error: any) {
      toast.error(error?.response?.data?.detail || 'Unable to send message right now.');
    }
  };

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="max-w-3xl mx-auto bg-white rounded-xl shadow p-6 md:p-8">
        <h1 className="text-3xl font-bold mb-2">Contact Us</h1>
        <p className="text-gray-600 mb-6">Have questions or need help? Send us a message.</p>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Name</label>
            <input
              className="input-field"
              placeholder="Your name"
              {...register('name', { required: 'Name is required' })}
            />
            {errors.name && <p className="text-sm text-red-600 mt-1">{errors.name.message}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
            <input
              className="input-field"
              placeholder="you@example.com"
              type="email"
              {...register('email', { required: 'Email is required' })}
            />
            {errors.email && <p className="text-sm text-red-600 mt-1">{errors.email.message}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Subject</label>
            <input
              className="input-field"
              placeholder="How can we help?"
              {...register('subject', { required: 'Subject is required' })}
            />
            {errors.subject && <p className="text-sm text-red-600 mt-1">{errors.subject.message}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Message</label>
            <textarea
              className="input-field min-h-[140px]"
              placeholder="Tell us more about your issue..."
              {...register('message', { required: 'Message is required', minLength: { value: 10, message: 'Please provide more details (min 10 chars)' } })}
            />
            {errors.message && <p className="text-sm text-red-600 mt-1">{errors.message.message}</p>}
          </div>

          <div className="flex justify-end">
            <button
              type="submit"
              disabled={isSubmitting}
              className="btn-primary disabled:opacity-50"
            >
              {isSubmitting ? 'Sending...' : 'Send message'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ContactPage;
