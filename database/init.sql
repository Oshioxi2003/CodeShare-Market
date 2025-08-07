-- CodeShare Market Database Initialization Script

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS codeshare_market;
USE codeshare_market;

-- Set character encoding
SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

-- Create indexes for better performance
-- These will be created automatically by SQLAlchemy, but we can define some here

-- Insert default categories
INSERT INTO product_categories (name, slug, description, icon, created_at, updated_at) VALUES
('Web Development', 'web-development', 'Web applications, websites, and web tools', 'globe', NOW(), NOW()),
('Mobile Apps', 'mobile-apps', 'iOS, Android, and cross-platform mobile applications', 'smartphone', NOW(), NOW()),
('Desktop Software', 'desktop-software', 'Windows, Mac, and Linux desktop applications', 'computer', NOW(), NOW()),
('Games', 'games', 'Game source codes and game assets', 'gamepad', NOW(), NOW()),
('WordPress', 'wordpress', 'WordPress themes, plugins, and tools', 'wordpress', NOW(), NOW()),
('E-commerce', 'e-commerce', 'Online store solutions and e-commerce tools', 'shopping-cart', NOW(), NOW()),
('Scripts & Tools', 'scripts-tools', 'Utility scripts, automation tools, and helpers', 'code', NOW(), NOW()),
('Machine Learning', 'machine-learning', 'AI, ML models, and data science projects', 'brain', NOW(), NOW()),
('Blockchain', 'blockchain', 'Smart contracts, DApps, and crypto projects', 'link', NOW(), NOW()),
('Templates', 'templates', 'HTML templates, email templates, and UI kits', 'layout', NOW(), NOW());

-- Create default admin user (password: admin123456)
-- Note: This should be changed immediately after first login
INSERT INTO users (
    email, 
    username, 
    full_name, 
    hashed_password,
    role,
    is_active,
    is_verified,
    created_at,
    updated_at
) VALUES (
    'admin@codeshare-market.com',
    'admin',
    'System Administrator',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5C3oLlFA.0yFa',
    'admin',
    true,
    true,
    NOW(),
    NOW()
);
