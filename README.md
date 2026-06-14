# DING

<p align="center">
  <b>Real-time chat backend built with FastAPI, PostgreSQL, JWT Authentication, and WebSockets.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/WebSockets-Real--Time-orange?style=for-the-badge">
</p>

---

## Overview

DING is a backend-focused real-time chat application built to understand how modern messaging platforms work behind the scenes.

Instead of creating another CRUD application, this project focuses on authentication, authorization, database relationships, persistent messaging, and real-time communication.

---

## Features

### Authentication

- User Registration
- User Login
- Password Hashing (bcrypt)
- JWT Authentication
- Protected Routes
- Current User Endpoint

### Chats

- Create Chats
- Private & Group Chats
- Add Members
- Retrieve User Chats
- Prevent Duplicate Members

### Messaging

- Send Messages
- Retrieve Message History
- Persistent PostgreSQL Storage
- Timestamped Messages

### Real-Time Communication

- WebSocket Connections
- Real-Time Message Broadcasting
- Multi-User Chat Rooms
- Automatic Message Persistence

### Security

- JWT-Protected WebSockets
- Chat Membership Validation
- Unauthorized Access Prevention
- Secure Password Storage

---

## Tech Stack

| Category | Technology |
|-----------|-----------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Security | bcrypt |
| Real-Time Communication | WebSockets |
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

## Architecture

```text
Client
   │
   ▼
API Routes
   │
   ▼
Service Layer
   │
   ▼
Database Layer
```

Business logic is separated from routes using a service-layer architecture.

---

## Authentication Flow

```text
Register
   │
   ▼
Login
   │
   ▼
JWT Token Generated
   │
   ▼
Protected Endpoints
```

### WebSocket Authentication

```text
Connect
   │
   ▼
Validate JWT
   │
   ▼
Verify Membership
   │
   ▼
Accept Connection
```

---

## Chat Flow

```text
User A
   │
   ▼
Create Chat
   │
   ▼
Add User B
   │
   ▼
Both Join Chat
   │
   ▼
Send Message
   │
   ▼
Broadcast To All Members
   │
   ▼
Store In PostgreSQL
```

---

## Database Design

### Users

Stores account information.

### Chats

Stores chat metadata.

### Chat Members

Links users and chats together.

### Messages

Stores chat messages and timestamps.

---

## Example WebSocket Connection

```text
ws://localhost:8000/ws/chat/1?token=YOUR_JWT_TOKEN
```

---

## What I Learned

Building DING helped me gain hands-on experience with:

- JWT Authentication
- Authorization
- Database Relationships
- SQLAlchemy
- PostgreSQL
- WebSockets
- Real-Time Messaging
- Service Layer Architecture
- Backend Security Practices
- Debugging Real-Time Systems

---

## Future Improvements

- Read Receipts
- Typing Indicators
- Online Presence
- Message Editing
- File Attachments
- Docker Support
- Alembic Migrations
- Automated Tests
- Redis Pub/Sub

---

## Author

Built by **Arman** as a backend engineering learning project.