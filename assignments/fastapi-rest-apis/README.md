# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern REST APIs using the FastAPI framework. You'll create a functional API with request validation, response models, and proper HTTP methods to handle data operations.

**Skills practiced:** REST API design, HTTP methods, request validation, response models, data serialization, async programming basics

## 📝 Tasks

### 🛠️ Set Up FastAPI Server and Create Basic Endpoints

#### Description
Set up a FastAPI application and create your first GET and POST endpoints to handle basic data requests.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Create a GET endpoint that returns a welcome message or list of items
- Create a POST endpoint that accepts JSON data and returns a confirmation response
- Run the server and test endpoints using the interactive API documentation (Swagger UI at `/docs`)

### 🛠️ Implement Request Validation with Pydantic Models

#### Description
Add Pydantic models to validate incoming requests and ensure data integrity.

#### Requirements
Completed program should:

- Define Pydantic model(s) for request and response data
- Use the model(s) in your endpoints for automatic validation
- Return appropriate error responses (400 Bad Request) for invalid data
- Test validation by sending invalid requests and confirming error messages

### 🛠️ Implement CRUD Operations

#### Description
Expand your API to support Create, Read, Update, and Delete operations on a collection of items.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all items
- Implement GET endpoint with a path parameter to retrieve a single item by ID
- Implement PUT or PATCH endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Store items in memory (using a list or dictionary) for now

### 🛠️ Add Error Handling and Status Codes

#### Description
Enhance your API with proper HTTP status codes and error handling for edge cases.

#### Requirements
Completed program should:

- Return appropriate HTTP status codes (200, 201, 404, 400, etc.)
- Raise `HTTPException` for missing resources or invalid operations
- Include meaningful error messages
- Test various error scenarios (e.g., deleting non-existent items, updating invalid data)
