# SQL Basics for PostgreSQL

**A quick reference guide for basic SQL commands in PostgreSQL.**

---

## 1. PostgreSQL Meta Commands (psql)

These commands are specific to the `psql` tool and start with `\`:

| Command      | Description                         |
| ------------ | ----------------------------------- |
| `\l`         | List all databases                  |
| `\c db_name` | Connect to a database               |
| `\dt`        | List all tables in current database |
| `\d table`   | Describe a table's structure        |
| `\du`        | List all users/roles                |
| `\q`         | Quit psql                           |

---

## 2. Database Operations

### Create a Database

```sql
CREATE DATABASE my_database;
```

### Delete (Drop) a Database

```sql
DROP DATABASE my_database;
```

> ⚠️ **Warning**: This permanently deletes the database and all its data!

### Connect to a Database

```sql
\c my_database
```

---

## 3. Table Operations

### Create a Table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Common Data Types:**
| Type | Description |
|---------------|--------------------------------|
| `SERIAL` | Auto-incrementing integer |
| `INTEGER` | Whole numbers |
| `VARCHAR(n)` | Variable-length string (max n) |
| `TEXT` | Unlimited length string |
| `BOOLEAN` | TRUE or FALSE |
| `DATE` | Date (YYYY-MM-DD) |
| `TIMESTAMP` | Date and time |
| `DECIMAL(p,s)`| Decimal number (precision, scale) |

### Delete (Drop) a Table

```sql
DROP TABLE students;
```

### Rename a Table

```sql
ALTER TABLE students RENAME TO learners;
```

---

## 4. Column Operations

### Add a Column

```sql
ALTER TABLE students ADD COLUMN phone VARCHAR(20);
```

### Delete a Column

```sql
ALTER TABLE students DROP COLUMN phone;
```

### Rename a Column

```sql
ALTER TABLE students RENAME COLUMN name TO full_name;
```

### Change Column Data Type

```sql
ALTER TABLE students ALTER COLUMN age TYPE SMALLINT;
```

---

## 5. INSERT - Adding Data

### Insert a Single Row

```sql
INSERT INTO students (name, email, age)
VALUES ('Alice', 'alice@email.com', 20);
```

### Insert Multiple Rows

```sql
INSERT INTO students (name, email, age) VALUES
    ('Bob', 'bob@email.com', 22),
    ('Charlie', 'charlie@email.com', 21),
    ('Diana', 'diana@email.com', 23);
```

---

## 6. SELECT - Reading Data

### Select All Columns

```sql
SELECT * FROM students;
```

### Select Specific Columns

```sql
SELECT name, email FROM students;
```

### Select with Condition (WHERE)

```sql
SELECT * FROM students WHERE age > 20;
```

### Select with Multiple Conditions

```sql
SELECT * FROM students WHERE age >= 20 AND name LIKE 'A%';
```

### Select with Sorting (ORDER BY)

```sql
SELECT * FROM students ORDER BY name ASC;   -- Ascending
SELECT * FROM students ORDER BY age DESC;   -- Descending
```

### Limit Results

```sql
SELECT * FROM students LIMIT 5;
```

### Count Rows

```sql
SELECT COUNT(*) FROM students;
```

---

## 7. UPDATE - Modifying Data

### Update a Single Row

```sql
UPDATE students SET age = 21 WHERE name = 'Alice';
```

### Update Multiple Columns

```sql
UPDATE students
SET email = 'alice.new@email.com', age = 22
WHERE name = 'Alice';
```

### Update All Rows (Be Careful!)

```sql
UPDATE students SET age = age + 1;  -- Everyone gets 1 year older
```

---

## 8. DELETE - Removing Data

### Delete Specific Rows

```sql
DELETE FROM students WHERE name = 'Bob';
```

### Delete with Condition

```sql
DELETE FROM students WHERE age < 18;
```

### Delete All Rows (Keep Table Structure)

```sql
DELETE FROM students;
-- or faster:
TRUNCATE TABLE students;
```

---

## 9. Filtering & Operators

### Comparison Operators

| Operator     | Description           |
| ------------ | --------------------- |
| `=`          | Equal                 |
| `<>` or `!=` | Not equal             |
| `<`          | Less than             |
| `>`          | Greater than          |
| `<=`         | Less than or equal    |
| `>=`         | Greater than or equal |

### Logical Operators

```sql
SELECT * FROM students WHERE age > 20 AND name = 'Alice';
SELECT * FROM students WHERE age < 18 OR age > 25;
SELECT * FROM students WHERE NOT age = 20;
```

### LIKE (Pattern Matching)

```sql
SELECT * FROM students WHERE name LIKE 'A%';     -- Starts with A
SELECT * FROM students WHERE name LIKE '%son';   -- Ends with 'son'
SELECT * FROM students WHERE name LIKE '%ali%';  -- Contains 'ali'
```

### IN (Multiple Values)

```sql
SELECT * FROM students WHERE age IN (18, 20, 22);
```

### BETWEEN (Range)

```sql
SELECT * FROM students WHERE age BETWEEN 18 AND 25;
```

### NULL Checks

```sql
SELECT * FROM students WHERE email IS NULL;
SELECT * FROM students WHERE email IS NOT NULL;
```

---

## 10. Aggregate Functions

```sql
SELECT COUNT(*) FROM students;              -- Total count
SELECT AVG(age) FROM students;              -- Average age
SELECT SUM(age) FROM students;              -- Sum of ages
SELECT MAX(age) FROM students;              -- Maximum age
SELECT MIN(age) FROM students;              -- Minimum age
```

### GROUP BY

```sql
SELECT age, COUNT(*) FROM students GROUP BY age;
```

### HAVING (Filter Groups)

```sql
SELECT age, COUNT(*) FROM students
GROUP BY age
HAVING COUNT(*) > 1;
```

---

## 11. Joins (Combining Tables)

### Sample Tables Setup

```sql
-- Teachers table
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Classes table with foreign key
CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    subject VARCHAR(100),
    teacher_id INTEGER REFERENCES teachers(id)
);
```

### INNER JOIN

Returns only matching rows from both tables:

```sql
SELECT classes.subject, teachers.name
FROM classes
INNER JOIN teachers ON classes.teacher_id = teachers.id;
```

### LEFT JOIN

Returns all rows from left table, matching rows from right:

```sql
SELECT classes.subject, teachers.name
FROM classes
LEFT JOIN teachers ON classes.teacher_id = teachers.id;
```

---

## 12. User Management

### Create a User

```sql
CREATE USER app_user WITH PASSWORD 'secure_password';
```

### Grant Permissions

```sql
GRANT ALL PRIVILEGES ON DATABASE my_database TO app_user;
GRANT SELECT, INSERT, UPDATE ON students TO app_user;
```

### Revoke Permissions

```sql
REVOKE DELETE ON students FROM app_user;
```

### Delete a User

```sql
DROP USER app_user;
```

---

## Quick Reference Card

| Action          | SQL Command                                 |
| --------------- | ------------------------------------------- |
| Create database | `CREATE DATABASE name;`                     |
| Delete database | `DROP DATABASE name;`                       |
| Create table    | `CREATE TABLE name (...);`                  |
| Delete table    | `DROP TABLE name;`                          |
| Insert data     | `INSERT INTO table (cols) VALUES (...);`    |
| Read data       | `SELECT cols FROM table WHERE condition;`   |
| Update data     | `UPDATE table SET col=val WHERE condition;` |
| Delete data     | `DELETE FROM table WHERE condition;`        |

---

## Practice Exercises

1. Create a `products` table with columns: `id`, `name`, `price`, `quantity`
2. Insert 5 products into the table
3. Select all products with price > 100
4. Update the quantity of a specific product
5. Delete products where quantity = 0
6. Find the average price of all products
