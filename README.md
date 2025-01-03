# 0x02. AirBnB Clone - MySQL

## Description

This project is a continuation of the AirBnB clone project, focusing on integrating a MySQL database into the application. The goal is to replace the file-based storage system with a more robust and scalable database solution using MySQL. This involves using Object-Relational Mapping (ORM) with SQLAlchemy to interact with the database.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the differences between file-based storage and database storage.
- Connect to a MySQL database from a Python script.
- Use SQLAlchemy to map Python classes to MySQL tables.
- Perform CRUD (Create, Read, Update, Delete) operations using SQLAlchemy.
- Handle database transactions safely.
- Implement relationships between tables (one-to-many, many-to-many).
- Write unit tests for database operations.

## Requirements

- **OS**: Ubuntu 20.04 LTS
- **Python**: Version 3.8.5
- **MySQLdb**: Version 2.0.x
- **SQLAlchemy**: Version 1.4.x
- **Code Style**: Pycodestyle (version 2.8.*)
- All files should be executable and end with a new line.
- The first line of all scripts should be exactly `#!/usr/bin/python3`.
- All modules, classes, and functions must have proper documentation.

## Setup

### Install and Activate Virtual Environment

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb

```bash
$ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
$ pip3 install mysqlclient
$ python3 -c "import MySQLdb; print(MySQLdb.version_info)"
```

### Install SQLAlchemy

```bash
$ pip3 install SQLAlchemy
$ python3 -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

## Project Tasks

| **Task**                         | **Description**                                                         | **File**                        |   
| -------------------------------- | ----------------------------------------------------------------------- | ------------------------------- |  
| **0. Fork me if you can!**       | Fork the existing AirBnB_clone repository and update the README.md.     | `README.md`                     |   
| **1. Bug free!**                 | Ensure all unittests pass without errors.                               | `tests/`                        |    
| **2. Console improvements**      | Update the console to allow object creation with parameters.            | `console.py`                    |    
| **3. MySQL setup development**   | Prepare a MySQL server for development.                                 | `setup_mysql_dev.sql`           |    
| **4. MySQL setup test**          | Prepare a MySQL server for testing.                                     | `setup_mysql_test.sql`          |    
| **5. Delete object**             | Add a method to delete objects from storage.                            | `models/engine/file_storage.py` |    
| **6. DBStorage - States and Cities** | Implement DBStorage for States and Cities.                          | `models/base_model.py`, `models/city.py`, `models/state.py`, `models/engine/db_storage.py`, `models/__init__.py` |    
| **7. DBStorage - User**          | Implement DBStorage for Users.                                          | `models/user.py`                |    
| **8. DBStorage - Place**         | Implement DBStorage for Places.                                         | `models/place.py`               |    
| **9. DBStorage - Review**        | Implement DBStorage for Reviews.                                        | `models/review.py`              |    
| **10. DBStorage - Amenity**      | Implement DBStorage for Amenities and many-to-many relationships.       | `models/amenity.py`, `models/place.py` |    

## General Guidelines

- Follow best practices for SQL and Python integration.
- Avoid hardcoding sensitive information like database credentials.
- Test your scripts with various input values, including edge cases.
- Use proper error handling for database operations.
- Always close database connections after use.

## SQL Scripts

- All SQL scripts should be executable on Ubuntu 20.04 LTS using MySQL 8.0.
- SQL queries should have comments explaining their purpose.
- SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`).

## More Info

### Comments for SQL Files

```sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### How to Test with MySQL

1. Create a specific database for testing.
2. Use MySQLdb to interact with the database directly.
3. Execute the console command.
4. Validate the changes in the database.

## Repositories

- [AirBnB_clone_v2](https://github.com/Achrafsadeq/AirBnB_clone_v2)

## Files

- `README.md`
- `console.py`
- `models/`
- `tests/`
- `setup_mysql_dev.sql`
- `setup_mysql_test.sql`
- `models/engine/file_storage.py`
- `models/base_model.py`
- `models/city.py`
- `models/state.py`
- `models/engine/db_storage.py`
- `models/__init__.py`
- `models/user.py`
- `models/place.py`
- `models/review.py`
- `models/amenity.py`
## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq & Elhoucine Smaili

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
