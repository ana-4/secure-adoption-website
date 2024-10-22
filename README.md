# Secure Cat Adoption Website

This is a simple web application that allows users to browse and adopt cats. The site supports three types of users: **guest**, **logged-in users**, and **administrators**. Guests can browse the available cats for adoption, logged-in users can submit adoption requests, and administrators can manage cats and review adoption requests.

## Features

- **User Roles**:
  - **Guest**: Can browse the list of available cats.
  - **Logged-in User**: Can browse cats, submit adoption requests, and view their own adoption requests.
  - **Administrator**: Has full access to the system, can manage cats, review and approve/reject adoption requests.
  
- **cat Management**: Administrators can add, update, or delete cats available for adoption.
- **Adoption Requests**: Logged-in users can submit requests to adopt cats.
- **File Upload**: cat images are uploaded and stored either locally or in AWS S3.
- **Responsive UI**: A simple front-end built using HTML and CSS.

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Django
- **Database**: PostgreSQL
- **File Storage**: AWS S3 (optional) or local file system

## User Roles and Permissions

- **Guest**:
  - Browse the list of available cats.
  - View details of each cat.
  - Access to public information but cannot interact with the system (e.g., can't submit adoption requests).

- **Logged-in User**:
  - Has access to all guest functionality.
  - Can submit adoption requests.
  - Can view a personal dashboard with submitted adoption requests.

- **Administrator**:
  - Full access to manage cats (add, update, delete).
  - Can view and manage adoption requests.
  - Can approve or reject adoption requests.
  - Has access to the Django admin panel for system management.

## Requirements

- Python 3.x
- Django 4.x
- PostgreSQL
- AWS S3 account (optional for remote file storage)

## Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/cat-adoption.git
   cd cat-adoption
