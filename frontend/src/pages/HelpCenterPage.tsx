import React, { useState } from 'react';

interface FaqItem {
  question: string;
  answer: string;
}

const faqs: FaqItem[] = [
  {
    question: 'How do I buy source code?',
    answer:
      'Browse products, add to cart, and complete checkout with your preferred payment method. Once paid, your downloads are available immediately in your dashboard.',
  },
  {
    question: 'How do I sell my code?',
    answer:
      'Create an account, switch your role to Seller in your profile, then upload your project with description, price, and demo. Our team will review before publishing.',
  },
  {
    question: 'Is there a refund policy?',
    answer:
      'Yes. If a product is misrepresented or has critical issues that cannot be resolved, you can request a refund within 7 days. See Terms for details.',
  },
  {
    question: 'How many times can I download?',
    answer:
      'By default, each purchase allows up to 5 downloads and never expires. If you have issues, contact support and we will assist.',
  },
];

const HelpCenterPage: React.FC = () => {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl md:text-4xl font-bold mb-4">Help Center</h1>
        <p className="text-gray-600 mb-8">
          Find answers to the most common questions. If you still need help, head to the Contact page and our team will assist you shortly.
        </p>

        <div className="space-y-4">
          {faqs.map((item, index) => (
            <div key={index} className="bg-white rounded-xl shadow p-5">
              <button
                className="w-full text-left flex justify-between items-center"
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
              >
                <span className="font-semibold text-lg">{item.question}</span>
                <span className="text-xl">{openIndex === index ? '−' : '+'}</span>
              </button>
              {openIndex === index && (
                <div className="mt-3 text-gray-700 leading-relaxed">{item.answer}</div>
              )}
            </div>
          ))}
        </div>

        <div className="mt-12">
          <h2 className="text-2xl font-semibold mb-3">Still need help?</h2>
          <p className="text-gray-600">
            Visit the Contact page and send us a message. We typically reply within 24 hours.
          </p>
        </div>
      </div>
    </div>
  );
};

export default HelpCenterPage;
