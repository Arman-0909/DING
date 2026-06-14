# DING

<p align="center">
  <h3 align="center">Real-Time Chat Backend</h3>
  <p align="center">
    Built with FastAPI, PostgreSQL, JWT Authentication and WebSockets.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/WebSockets-RealTime-orange?style=for-the-badge">
</p>

---

## About

DING is a backend-focused real-time chat application designed to explore how modern messaging systems work under the hood.

The project implements authentication, authorization, persistent message storage, chat membership validation, and real-time communication using WebSockets.

---

## Features

### Authentication

- User Registration
- User Login
- Password Hashing (bcrypt)
- JWT Access Tokens
- Protected Endpoints

### Chats

- Create Chats
- Add Members
- Retrieve User Chats
- Membership Validation

### Messaging

- Send Messages
- Retrieve Message History
- Persistent Storage
- Timestamped Messages

### Real-Time Communication

- WebSocket Connections
- JWT-Protected WebSockets
- Real-Time Message Broadcasting
- Multi-User Chat Rooms

### Security

- Password Hashing
- JWT Verification
- Chat Membership Checks
- Unauthorized Connection Blocking

---

## Tech Stack

| Technology | Purpose |
|------------|----------|
| FastAPI | API Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| JWT | Authentication |
| bcrypt | Password Hashing |
| WebSockets | Real-Time Communication |
| Python | Backend Language |

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

## Database Design

### Users

Stores account information.

### Chats

Stores chat metadata.

### Chat Members

Links users to chats.

### Messages

Stores all chat messages and timestamps.

---

## WebSocket Authentication Flow

```text
Client
   │
   ▼
JWT Token
   │
   ▼
Token Validation
   │
   ▼
Membership Check
   │
   ▼
Connection Accepted
   │
   ▼
Real-Time Messaging
```

---

## API Capabilities

### Auth

```http
POST /auth/register
POST /auth/login
GET  /auth/me
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

- FastAPI Application Architecture
- SQLAlchemy Relationships
- JWT Authentication
- Authorization Patterns
- WebSocket Communication
- PostgreSQL Integration
- Service Layer Design
- Real-Time System Development

---

## Future Improvements

- Read Receipts
- Typing Indicators
- Online Presence
- File Sharing
- Message Editing
- Docker Deployment
- Automated Testing
- Redis Pub/Sub Scaling

---

## License

This project is licensed under the MIT License.

---

Built by **Arman**.