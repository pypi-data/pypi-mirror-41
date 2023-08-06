# SmartNinja SQL

## About

SmartNinja SQL is a simple wrapper for SQLite database (support for others might be added in the future).

The purpose of this tool is to simplify connecting to SQLite and getting relevant data from it.

**Important:** This is not an object-relational mapper (ORM). You still need to write SQL queries.

## Installation

This is a pip package:

	pip install smartninja-sql

The package does not have any dependencies. It is compatible with Python 3 only.

## Usage

Take a look at this basic usage example:

```python
from smartninja_sql.sqlite import SQLiteDatabase
	
db = SQLiteDatabase()
	
db.query("""CREATE TABLE IF NOT EXISTS User (
            id integer PRIMARY KEY AUTOINCREMENT, 
            name text NOT NULL, 
            age integer);""")
	
db.print_tables(verbose=True)
```

If you open the connection with a database like this: `db = SQLiteDatabase()`, the database will be created in-memory only. When the program will finish, the database will be lost.

If you want a persistent database, enter a database name:

```python
db = SQLiteDatabase(name="my_database.sqlite")
```

If this database does not yet exist, Python will create it for you. If it does exist, it will connect to it.

### Print table data (name & fields)

This method prints the data about the tables in a database. By default the `verbose` parameter is `False` - in this case the method prints the names of the tables only:

```python
# same result in both cases
db.print_tables()
db.print_tables(verbose=False)
```

But if you set `verbose` as `True`, the method will also print out all the **field names** in each table and their respective **types**:

```python
db.print_tables(verbose=True)
```

### Queries

Database queries are done using the `.query()` method:

```python
# create table
db.query("""CREATE TABLE IF NOT EXISTS User (
            id integer PRIMARY KEY AUTOINCREMENT, 
            name text NOT NULL, 
            age integer);""")

db.print_tables(verbose=True)

# alter (edit) table
db.query("ALTER TABLE User ADD email TEXT;")
db.print_tables(verbose=True)  # the table has a new field: email

# insert data into a table
db.query("INSERT INTO User (name, age, email) VALUES ('Matt', 31, 'matt@example.org')")
db.query("INSERT INTO User (name, age, email) VALUES ('Nina', 25, 'nina@example.org')")

# get data (select) and print it
print(db.query("SELECT * FROM User;"))
print(db.query("SELECT * FROM User WHERE age=25;"))
print(db.query("SELECT * FROM User WHERE age=26;"))
```

If you're familiar with the `sqlite3` library, the `query()` method returns the `.fetchall()` result.

### Connection and cursor

The SmartNinja SQL wrapper is designed to simplify work with the `sqlite3` library. But if you'd want to access the **connection** and **cursor** variables **directly**, you definitely can:

```python
connection = db.conn
cursor = db.cursor
```

But you most likely won't have to.

### Closing the cursor and connection

You can simply close the cursor and connection with a single method:

```python
db.close()
```

## TODO

- tests
- CI pipeline