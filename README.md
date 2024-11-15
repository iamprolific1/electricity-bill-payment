**ELECTRICITY BILL PAYMENT API**

A RESTful API built with FastAPI for managing users and processing electricity bill payments. This project provides endpoints for user registeration, authentication, and bill payment, along with support for database integration and validation.

# Table of Contents
1. Features
2. Technologies used
3. Setup Instructions
4. API Endpoints
6. Testing


## Features
    - FastAPI: Framework for buliding APIs.
    - SQLite: Database for development.
    - SQLAlchemy: ORM for database management.
    - Pydantic: Data validation and settings management.
    - Uvicorn: ASGI server for running the FastAPI app.

## Setup Instructions
### Prerequisites
    - Python 3.8 or higher
    - A virtual environment tool (e.g., venv or virtualenv)

### Installation
1. clone the repository:
    ```bash
        git clone https://github.com/yourusername/electricity-bill-payment.git
        cd electricity-bill-payment

2. create and activate a virtual environment:
    ```bash
        python -m venv venv
        source venv/bin/activate    
        # On Windows: venv\Scripts\activate
    

3. Install the required dependencies:
    `pip install -r requirements.txt`

4. Initialize the database:
    `python -m app.database.py`

5. Run the server
    `uvicorn app.main:app --reload`

## API Endpoints

### User Management
| Method    | Endpoint      | Description   |
---------------------------------------------
| POST      | /users/       | Create a new
|           |               | user          |
| GET       | /users/{id}   | Get a user by
|           |               | ID            |


### Account Management
| Method    | Endpoint      | Description   |
---------------------------------------------
| POST      | /accounts/    | Create a new  |
|           |               | account       


### Transaction Management
| Method    | Endpoint      | Description   |
---------------------------------------------
| POST      | /transactions/| Create a new  |
|           |               | transaction   |


## Database Schema

### Users Table
| Column    | Type      | Description   |
-----------------------------------------
| id        | integer   | Primary Key   |
| name      | String    | User's name   |
| email     | String    | Unique user   |
|           |           | email         |
| password  | String    | Hashed        |
|           |           | Password      |

## Accounts Table
| Column        | Type      | Description   |
-----------------------------------------
| user_id       | integer   | Foreign key   |
|               |           | to Users      |
| outstanding_  | float     | User outstan- |
| balance       |           | ding amount   |

## Transactions Table
| Column        | Type      | Description   |
---------------------------------------------
| account_id    | integer   | Foreign key   |
|               |           | to Accounts   |
| amount        | float     | total amount  |