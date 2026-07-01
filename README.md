# DING

<p align="center">
  <h1 align="center">DING</h1>
  <p align="center">
    A modern real-time chat backend built with FastAPI, PostgreSQL, JWT Authentication, Google OAuth, and WebSockets.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Google_OAuth-red?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/WebSockets-orange?style=for-the-badge">
</p>

---

## 📖 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Future Improvements](#future-improvements)

---

## 💡 About

DING is a backend-focused real-time chat application built to demonstrate production-style backend architecture. It features secure authentication, Google OAuth integration, chat management, persistent messaging, pagination, and real-time communication using native WebSockets.

The project follows a clean service-oriented architecture, decoupling the API routing layer from business logic and database models, ensuring high maintainability and scalability.

---

## ✨ Features

- **Robust Authentication**: 
  - Local Registration & Login with bcrypt password hashing
  - Google OAuth Sign-In (with seamless account linking)
  - JWT Authentication for both REST API and WebSockets
- **Chat Management**:
  - Create Private and Group Chats
  - Add/Remove Members with strict membership validation
  - Retrieve User's Chats
- **Real-Time Messaging**:
  - Persistent chat history in PostgreSQL
  - Message pagination (Limit/Offset)
  - Real-Time WebSocket broadcasting to active connections
  - Automatic stale connection cleanup
- **Security Best Practices**:
  - Input validation (e.g., message length, password strength)
  - CORS middleware enabled
  - Route authorization

---

## 🛠 Tech Stack

| Layer | Technology | Description |
|--------|------------|-------------|
| **Framework** | FastAPI | High-performance async web framework |
| **Database** | PostgreSQL | Relational database for persistent storage |
| **ORM** | SQLAlchemy | Python SQL toolkit and Object Relational Mapper |
| **Auth** | Authlib & python-jose | JWT and Google OAuth 2.0 integration |
| **Security** | passlib (bcrypt) | Secure password hashing |
| **Real-Time** | WebSockets | Full-duplex communication channels |
| **Language** | Python 3.10+ | |

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.10+
- PostgreSQL
- Node.js (if running the frontend)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DING.git
   cd DING/backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the `backend` directory (use `.env.example` as a template):
   ```env
   DATABASE_URL=postgresql://username:password@localhost/ding
   SECRET_KEY=your_super_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

The API will be running at `http://localhost:8000`. You can explore the interactive API documentation at `http://localhost:8000/docs`.

---

## 📂 Project Structure

```text
app/
├── api/          # FastAPI route handlers (Controllers)
├── core/         # Core configuration, security, and OAuth setup
├── db/           # Database connection and session management
├── models/       # SQLAlchemy database models
├── schemas/      # Pydantic schemas for request/response validation
├── services/     # Business logic layer
├── utils/        # Helper functions (hashing, tokens)
├── websocket/    # WebSocket connection manager
└── main.py       # FastAPI application entry point
```

---

## 📡 API Reference

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login with email/password
- `GET  /auth/me` - Get current authenticated user
- `GET  /auth/google/login` - Redirect to Google OAuth
- `GET  /auth/google/callback` - Handle Google OAuth callback

### Chats
- `POST /chats` - Create a new chat
- `GET  /chats` - Get all chats for current user
- `POST /chats/{chat_id}/members` - Add a member to a chat
- `GET  /chats/{chat_id}/members` - Get members of a chat

### Messages
- `POST /messages` - Send a message to a chat
- `GET  /messages/{chat_id}?limit=50&offset=0` - Get chat messages (paginated)

### WebSockets
- `ws://localhost:8000/ws/chat/{chat_id}?token=JWT_TOKEN` - Connect to a chat room

---

## 🎯 Future Improvements

- React/Next.js Frontend integration
- Alembic Database Migrations
- Read Receipts & Typing Indicators
- Online Presence & Status
- File & Image Sharing
- Message Editing & Deletion
- Redis Pub/Sub for multi-instance scaling

---

## 📄 License

Licensed under the **MIT License**.

---

<p align="center">
Built with ❤️ by <b>Arman</b>
</p>