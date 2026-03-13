# Address Book API – FastAPI

This project implements a simple Address Book REST API using FastAPI and SQLAlchemy.
The goal of the project is to demonstrate backend API design, database integration, and location-based querying.

The application allows storing address information along with geographic coordinates and provides an endpoint to search for addresses within a specified radius.

## Tech Stack

* Python 3
* FastAPI
* SQLAlchemy ORM
* SQLite
* Uvicorn (ASGI server)
* Pydantic for request/response validation

## Project Structure

```
address-book-fastapi
│
├── app
│   ├── main.py        # FastAPI application and API routes
│   ├── database.py    # Database connection setup
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   └── crud.py        # Database operations
│
├── address_book.db    # SQLite database file
├── requirements.txt
└── README.md
```

## Running the Project

Clone the repository and install dependencies.

```
pip install -r requirements.txt
```

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

Create Address

POST `/addresses`

Stores a new address record in the database including name, email, phone number, latitude and longitude.

Retrieve All Addresses

GET `/addresses`

Returns the list of all saved addresses.

Delete Address

DELETE `/addresses/{id}`

Removes an address record using its ID.

Nearby Address Search

GET `/addresses/nearby`

Query Parameters

* lat → latitude
* lon → longitude
* radius → search radius in kilometers

This endpoint returns all addresses located within the given radius.

## Distance Search Logic

The nearby search uses the **Haversine formula** to calculate the distance between two geographic coordinates.
Each stored address coordinate is compared with the requested location, and only those within the specified radius are returned.

## Example Request

```
GET /addresses/nearby?lat=12.97&lon=77.59&radius=5
```

## Notes

This project focuses on demonstrating clean API structure using FastAPI along with ORM-based database access.
The architecture separates API routes, database models, schemas, and CRUD operations to keep the codebase maintainable and easy to extend.

Possible extensions include authentication, pagination support, and switching to PostgreSQL for production use.

## Author

Lokesh
