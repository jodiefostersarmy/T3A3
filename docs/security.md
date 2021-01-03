# Security

For the security of this app, there are a few techniques that can be used to ensure security of user information and data. Because this is a Python application, we used **SQLAlchemy** for the ORM and **BCrypt**.

### SQL Alchemy

SQL Alchemy is an object relational mapper that allows the application to communicate with the database using Python language as opposed to SQL. 

**How does this ensure security?**
The ability to write query in Python via an ORM means that there is no chance that we are writing raw SQL, which is a primary concern with SQL databases for the risk of being attacked with SQL injection.

**What is SQL injection?**
SQL injection is where the attacker uses raw SQL as the content for an input field, that can return sensitive information if the program has not used paramaterised queries or created sanitisation of user input.

For example, if a user login page is not properly sanitised for user input and they have a generic login query such as:

```SELECT * FROM users WHERE username='User' AND password='1234';```

The attacker could easily write a raw SQL query that would provide them with the full list of users and passwords for the databse with the request below:

```SELECT * FROM users WHERE username='User' OR 1=1;```

According to some sources, it is estimated that there is around 65% of people that use the same password across multiple sites. 

**How can we prevent SQL injection?**
Using an ORM such as SQLAlchemy, there are baseline security parameters that can be used to minimise security breaches in sensitive data.

Things such as input validation, which can include type, legnth, format, query paramaters - used to determine return values and accepted user input. Using the ORM means we can minimise the chance of human error, by avoiding having to write raw SQL, and having extentions such as **psycopg2** which will escape characters and avoid comment syntax or semicolons.

Using an extension such as **BCrypt**, which provides hashing utilities for the application, allows the password to be stored safely without revealing the actual password, but match the hash with the stored hash.

