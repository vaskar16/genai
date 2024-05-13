ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Taherpur@123'; 

CREATE DATABASE IF NOT EXISTS employeedb;

USE employeedb;

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Department VARCHAR(50),
    Designation VARCHAR(50),
    Joining_Date DATE,
    Salary DECIMAL(10, 2)

);

INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, Department, Designation, Joining_Date, Salary)
VALUES 
(1, 'John', 'Doe', 'john.doe@example.com', 'HR', 'HR Manager', '2023-01-10', 60000.00),
(2, 'Jane', 'Smith', 'jane.smith@example.com', 'Finance', 'Accountant', '2022-12-15', 50000.00),
(3, 'Michael', 'Johnson', 'michael.johnson@example.com', 'IT', 'Software Developer', '2023-02-20', 65000.00),
(4, 'Emily', 'Williams', 'emily.williams@example.com', 'Marketing', 'Marketing Manager', '2023-03-05', 70000.00),
(5, 'David', 'Brown', 'david.brown@example.com', 'Operations', 'Operations Manager', '2023-04-15', 75000.00),
(6, 'Jessica', 'Miller', 'jessica.miller@example.com', 'Sales', 'Sales Executive', '2023-05-20', 55000.00),
(7, 'Daniel', 'Taylor', 'daniel.taylor@example.com', 'Finance', 'Financial Analyst', '2023-06-10', 60000.00),
(8, 'Olivia', 'Anderson', 'olivia.anderson@example.com', 'IT', 'Systems Administrator', '2023-07-05', 58000.00),
(9, 'William', 'Martinez', 'william.martinez@example.com', 'Marketing', 'Marketing Specialist', '2023-08-15', 62000.00),
(10, 'Sophia', 'Garcia', 'sophia.garcia@example.com', 'HR', 'HR Assistant', '2023-09-20', 45000.00),
(11, 'Ethan', 'Lopez', 'ethan.lopez@example.com', 'Sales', 'Sales Manager', '2023-10-10', 68000.00),
(12, 'Ava', 'Hernandez', 'ava.hernandez@example.com', 'Operations', 'Operations Coordinator', '2023-11-05', 52000.00),
(13, 'Alexander', 'Hill', 'alexander.hill@example.com', 'IT', 'Software Engineer', '2023-12-15', 67000.00),
(14, 'Mia', 'Young', 'mia.young@example.com', 'Finance', 'Financial Controller', '2024-01-20', 80000.00),
(15, 'James', 'King', 'james.king@example.com', 'HR', 'Recruitment Specialist', '2024-02-10', 48000.00),
(16, 'Charlotte', 'Scott', 'charlotte.scott@example.com', 'Marketing', 'Marketing Coordinator', '2024-03-05', 53000.00),
(17, 'Benjamin', 'Adams', 'benjamin.adams@example.com', 'Sales', 'Sales Representative', '2024-04-15', 56000.00),
(18, 'Amelia', 'Campbell', 'amelia.campbell@example.com', 'Operations', 'Operations Analyst', '2024-05-20', 59000.00),
(19, 'Lucas', 'Parker', 'lucas.parker@example.com', 'IT', 'Database Administrator', '2024-06-10', 62000.00),
(20, 'Isabella', 'Evans', 'isabella.evans@example.com', 'Finance', 'Accounts Payable Clerk', '2024-07-05', 48000.00);
