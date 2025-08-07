# CodeShare Market - Source Code Marketplace

## 📋 Giới thiệu

CodeShare Market là một nền tảng marketplace cho phép các lập trình viên chia sẻ, mua bán và trao đổi source code. Dự án được xây dựng với công nghệ hiện đại, bảo mật cao và giao diện thân thiện.

## 🚀 Tính năng chính

### Cho người dùng
- ✅ Đăng ký, đăng nhập (Email, Google)
- ✅ Tìm kiếm, lọc và xem demo code
- ✅ Mua source code với thanh toán online (PayPal, VNPay)
- ✅ Tải code đã mua, quản lý thư viện cá nhân
- ✅ Đánh giá, bình luận sản phẩm
- ✅ Upload và bán source code

### Cho người bán
- ✅ Tạo bài đăng với mô tả chi tiết
- ✅ Upload file, ảnh và video demo
- ✅ Theo dõi thống kê bán hàng
- ✅ Rút tiền về tài khoản

### Cho quản trị viên
- ✅ Duyệt và kiểm duyệt code
- ✅ Quản lý người dùng, giao dịch
- ✅ Thống kê doanh thu
- ✅ Xử lý tranh chấp

## 🛠 Công nghệ sử dụng

### Backend
- **FastAPI** (Python) - Framework API hiệu năng cao
- **SQLAlchemy** - ORM cho database
- **MySQL** - Database chính
- **Redis** - Cache và session management
- **Celery** - Background tasks
- **JWT** - Authentication

### Frontend
- **React** (TypeScript) - UI Framework
- **TailwindCSS** - Styling
- **React Router** - Routing
- **React Query** - Data fetching
- **React Hook Form** - Form handling
- **Framer Motion** - Animations

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **GitHub Actions** - CI/CD (sẽ cấu hình)

## 📦 Cài đặt và chạy dự án

### Yêu cầu hệ thống
- Python 3.9+
- Node.js 16+
- MySQL 8.0+
- Redis 6+
- Docker & Docker Compose (optional)

### 1. Clone repository
```bash
git clone https://github.com/yourusername/codeshare-market.git
cd codeshare-market
```

### 2. Cài đặt Backend

#### Tạo virtual environment
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

#### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

#### Tạo file .env
```bash
cp .env.example .env
# Chỉnh sửa file .env với thông tin database và các API keys
```

#### Chạy database với Docker
```bash
# Từ thư mục root
docker-compose up -d mysql redis phpmyadmin
```

#### Chạy migrations
```bash
alembic upgrade head
```

#### Khởi động server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend sẽ chạy tại: http://localhost:8000
API Docs: http://localhost:8000/docs

### 3. Cài đặt Frontend

#### Cài đặt dependencies
```bash
cd frontend
npm install
```

#### Tạo file .env
```bash
REACT_APP_API_URL=http://localhost:8000/api/v1
```

#### Khởi động development server
```bash
npm start
```

Frontend sẽ chạy tại: http://localhost:3000

### 4. Chạy với Docker Compose (Recommended)

```bash
# Từ thư mục root
docker-compose up -d
```

Các services sẽ chạy tại:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- PHPMyAdmin: http://localhost:8080
- MySQL: localhost:3306
- Redis: localhost:6379

## 📝 API Documentation

### Authentication
- `POST /api/v1/auth/register` - Đăng ký tài khoản
- `POST /api/v1/auth/login` - Đăng nhập
- `POST /api/v1/auth/refresh` - Refresh token
- `GET /api/v1/auth/me` - Lấy thông tin user hiện tại

### Products
- `GET /api/v1/products` - Danh sách sản phẩm
- `GET /api/v1/products/{id}` - Chi tiết sản phẩm
- `POST /api/v1/products` - Tạo sản phẩm mới (seller)
- `PUT /api/v1/products/{id}` - Cập nhật sản phẩm
- `DELETE /api/v1/products/{id}` - Xóa sản phẩm

### Transactions
- `POST /api/v1/transactions/create` - Tạo giao dịch
- `GET /api/v1/transactions/my` - Lịch sử giao dịch
- `POST /api/v1/transactions/verify` - Xác nhận thanh toán

## 🔒 Bảo mật

- Password được hash với bcrypt
- JWT tokens cho authentication
- Rate limiting để chống DDoS
- Input validation với Pydantic
- SQL injection protection với SQLAlchemy ORM
- XSS protection
- CORS configuration

## 🚧 Roadmap

- [ ] Tích hợp thêm payment gateways (Stripe, Momo)
- [ ] AI code review và quality check
- [ ] Real-time chat giữa buyer và seller
- [ ] Mobile app (React Native)
- [ ] Blockchain integration cho license management
- [ ] Multi-language support
- [ ] Advanced search với Elasticsearch

## 👥 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết.

## 📄 License

Dự án này được cấp phép theo [MIT License](LICENSE).

## 📞 Liên hệ

- Email: admin@codeshare-market.com
- Website: https://codeshare-market.com
- GitHub: https://github.com/codeshare-market

## 🙏 Cảm ơn

Cảm ơn tất cả các contributors và open-source projects đã giúp xây dựng CodeShare Market.

---
Made with ❤️ by CodeShare Market Team
