# Book Scraper API

A simple FastAPI application that scrapes book data from [Books to Scrape](https://books.toscrape.com) and stores it in a PostgreSQL database.

## Table of Contents
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Database Structure](#database-structure)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/book-scraper-api.git
   cd book-scraper-api

2. **Create a virtual environment (optional but recommended)**:
    python -m venv venv

3. **Activate the virtual environment**:
    venv\Scripts\activate

4. **Install the required packages**:
    pip install -r requirements.txt

5. **Set up the environment variables: Create a .env file in the root directory with the following content**:
    DATABASE_URL="postgresql://username:password@localhost:5432/book_scraper_db"


## Running the Project

1. **Create the database tables: The tables will be created automatically when you run the application for the first time.**

2. **Run the FastAPI application: Use Uvicorn to run the application**:
    uvicorn app.main:app --reload

3. **Access the API documentation**: 
    Open your browser and go to http://localhost:8000/docs to see the interactive API documentation.


## API Endpoints

**GET /: Welcome message.**
**POST /books/: Create a new book entry.**
**GET /books/: Retrieve a list of books.**
**GET /scrape/: Scrape books from the website and store them in the database.**

## Database Structure
The database contains a single table named books with the following columns:
    **id: Primary key**
    **title: Book title**
    **price: Book price**
    **availability: Availability status**
    **rating: Book rating**
    **product_url: URL to the product page**


## License
    This project is licensed under the MIT License. See the LICENSE file for more details.    