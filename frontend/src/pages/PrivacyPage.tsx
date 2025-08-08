import React from 'react';

const PrivacyPage: React.FC = () => {
  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="prose max-w-3xl">
        <h1>Privacy Policy</h1>
        <p className="text-gray-500">Last updated: 2025-08-08</p>
        <p>
          We collect only necessary information to operate our marketplace, such as account details and transaction records. We do not sell your personal data.
        </p>
        <h2>Data We Collect</h2>
        <ul>
          <li>Account information (email, username)</li>
          <li>Purchase and sales records</li>
          <li>Technical data like IP address and device info</li>
        </ul>
        <h2>How We Use Data</h2>
        <ul>
          <li>Provide and improve services</li>
          <li>Process payments and prevent fraud</li>
          <li>Send important account notifications</li>
        </ul>
        <h2>Your Rights</h2>
        <p>
          You may request access, correction, or deletion of your personal data by contacting support. We store data only as long as necessary.
        </p>
      </div>
    </div>
  );
};

export default PrivacyPage;
