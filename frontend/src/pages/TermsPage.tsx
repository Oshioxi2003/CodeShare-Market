import React from 'react';

const TermsPage: React.FC = () => {
  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="prose max-w-3xl">
        <h1>Terms of Service</h1>
        <p className="text-gray-500">Last updated: 2025-08-08</p>
        <p>
          By accessing or using CodeShare Market, you agree to be bound by these Terms. If you disagree with any part, you may not access the service.
        </p>
        <h2>Licensing</h2>
        <p>
          Purchases grant you a non-exclusive license to use the code in your own projects. Resale, redistribution, or claiming authorship is prohibited unless explicitly allowed by the seller.
        </p>
        <h2>Payments & Refunds</h2>
        <p>
          All payments are processed by third-party gateways. Refunds may be granted within 7 days if the product is misrepresented or contains unresolved critical issues.
        </p>
        <h2>Seller Responsibilities</h2>
        <p>
          Sellers must ensure their submissions are legal, free of malware, and accurately described. Violation may result in account suspension.
        </p>
        <h2>Limitation of Liability</h2>
        <p>
          We are not liable for any indirect or consequential damages arising from the use of products purchased on the marketplace.
        </p>
      </div>
    </div>
  );
};

export default TermsPage;
