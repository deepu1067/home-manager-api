# Writing the README.md file for the user's Django API

The spreadsheet should have 2 main sheets. First sheet is for meal calculation and another is for cost of bazar done by an individual

# Home API

This API allows you to perform various CRUD operations and retrieve data from Google Sheets. The operations include listing data, adding rows, updating rows, and calculating totals, all organized by user and sheet name.

## Endpoints

### 1. **List Main Sheet Data**

- **URL**: `/`
- **Method**: `GET`
- **Description**: Retrieve data from the main sheet.
- **Example**:
  ```bash
  curl -X GET http://localhost:8000/
  ```

### 2. **List Given Sheet Data**

- **URL**: `/given/`
- **Method**: `GET`
- **Description**: Retrieve data from a specified sheet.
- **Example**:
  ```bash
  curl -X GET http://localhost:8000/given/
  ```

### 3. **Add Row for a User to a Specific Sheet**

- **URL**: `/add/<str:user>/<str:sheet>/`
- **Method**: `POST`
- **Description**: Add a new row for a user to a specific sheet.
- **Parameters**:
  - `user`: The name of the user.
  - `sheet`: The sheet where the row will be added.
- **Example**:
  ```bash
  curl -X POST http://localhost:8000/add/john/Sheet1/ -H "Content-Type: application/json" -d '{"values": [1, 2, 3]}'
  ```

### 4. **Add Row for a User on a Specific Day**

- **URL**: `/add/<str:user>/<int:day>/<str:sheet>/`
- **Method**: `POST`
- **Description**: Add a new row for a user on a specified day in a specific sheet.
- **Parameters**:
  - `user`: The name of the user.
  - `day`: The day to add the row for.
  - `sheet`: The sheet where the row will be added.
- **Example**:
  ```bash
  curl -X POST http://localhost:8000/add/john/4/Sheet1/ -H "Content-Type: application/json" -d '{"values": [1, 2, 3]}'
  ```

### 5. **Update a Row for a User**

- **URL**: `/update/<int:day>/<str:user>/<str:sheet>/`
- **Method**: `PUT`
- **Description**: Update a row for a specific user on a specific day in a given sheet.
- **Parameters**:
  - `day`: The day to update.
  - `user`: The name of the user.
  - `sheet`: The sheet where the row is located.
- **Example**:
  ```bash
  curl -X PUT http://localhost:8000/update/4/john/Sheet1/ -H "Content-Type: application/json" -d '{"values": [5, 6, 7]}'
  ```

### 6. **Delete a Row for a Given Day**

- **URL**: `/delete/<int:day>/<str:sheet>/`
- **Method**: `DELETE`
- **Description**: Delete a row for a specific day in a given sheet.
- **Parameters**:
  - `day`: The day to delete.
  - `sheet`: The sheet where the row will be deleted.
- **Example**:
  ```bash
  curl -X DELETE http://localhost:8000/delete/4/Sheet1/
  ```

### 7. **Get Total Meal Count for a User**

- **URL**: `/total-meal/<str:user>/<str:sheet>/`
- **Method**: `GET`
- **Description**: Get the total meal count for a specific user from a specific sheet.
- **Parameters**:
  - `user`: The name of the user.
  - `sheet`: The sheet from which to get the total meal count.
- **Example**:
  ```bash
  curl -X GET http://localhost:8000/total-meal/john/Sheet1/
  ```

### 8. **Get All Users**

- **URL**: `/users/`
- **Method**: `GET`
- **Description**: Get a list of all users.
- **Example**:
  ```bash
  curl -X GET http://localhost:8000/users/
  ```

### 9. **Get User's Meal Data**

- **URL**: `/get/<str:user>/<str:sheet>/`
- **Method**: `GET`
- **Description**: Get meal data for a specific user from a specific sheet.
- **Parameters**:
  - `user`: The name of the user.
  - `sheet`: The sheet to retrieve the meal data from.
- **Example**:
  ```bash
  curl -X GET http://localhost:8000/get/john/Sheet1/
  ```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/home-api.git
   ```
