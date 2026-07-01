# DING

<p align="center">
  <h1 align="center">DING</h1>
  <p align="center">
    A modern real-time chat backend built with FastAPI, PostgreSQL, JWT Authentication, Google OAuth and WebSockets.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Google-OAuth-red?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/WebSockets-Real--Time-orange?style=for-the-badge">
</p>

---

## About

DING is a backend-focused real-time chat application built to explore production-style backend architecture. It features secure authentication, Google OAuth, chat management, persistent messaging, and real-time communication using native WebSockets.

The project follows a clean service-based architecture with SQLAlchemy models, JWT authentication, and PostgreSQL as the primary database.

---

## Features

### Authentication

- User Registration & Login
- Google OAuth Sign-In
- JWT Authentication
- bcrypt Password Hashing
- Protected API Routes
- Account Linking
- Current User Endpoint

### Chat System

- Create Private Chats
- Add Chat Members
- Retrieve User Chats
- Membership Validation
- Secure Chat Access

### Messaging

- Real-Time Messaging
- WebSocket Broadcasting
- Chat History
- Persistent Storage
- Timestamped Messages

### Security

- JWT-Protected WebSockets
- Password Encryption
- Google OAuth Integration
- Chat Authorization
- Duplicate Account Protection

---

## Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT + Google OAuth |
| Password Security | bcrypt |
| Real-Time | Native WebSockets |
| Language | Python |

---

## Project Structure

```text
app/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── services/
├── utils/
├── websocket/
└── main.py
```

---

## Authentication Flow

```text
Register / Google Login
          │
          ▼
     User Verified
          │
          ▼
     JWT Generated
          │
          ▼
 Protected API Access
          │
          ▼
 WebSocket Authentication
          │
          ▼
 Real-Time Chat
```

---

## API

### Authentication

```http
POST /auth/register
POST /auth/login
GET  /auth/me
GET  /auth/google/login
GET  /auth/google/callback
```

### Chats

```http
POST /chats
GET  /chats
POST /chats/{chat_id}/members
GET  /chats/{chat_id}/members
```

### Messages

```http
POST /messages
GET  /messages/{chat_id}
```

### WebSocket

```text
ws://localhost:8000/ws/chat/{chat_id}?token=JWT_TOKEN
```

---

## What I Learned

- FastAPI Application Design
- SQLAlchemy ORM
- PostgreSQL Integration
- JWT Authentication
- Google OAuth
- WebSocket Communication
- Service Layer Architecture
- Authorization & Access Control
- Building Real-Time Systems

---

## Future Improvements

- React Frontend
- Read Receipts
- Typing Indicators
- Online Presence
- File & Image Sharing
- Message Editing
- Docker Support
- Automated Testing
- Redis Pub/Sub Scaling

---

## License

Licensed under the **MIT License**.

---

<p align="center">
Built with ❤️ by <b>Arman</b>
</p>