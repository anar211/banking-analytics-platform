-- =========================================================
-- Enterprise Banking Analytics Platform
-- Database Schema
-- =========================================================

CREATE TABLE customers (
    customer_id        INT PRIMARY KEY,
    first_name         VARCHAR(100),
    last_name          VARCHAR(100),
    gender             VARCHAR(20),
    birth_date         DATE,
    country            VARCHAR(100),
    city               VARCHAR(100),
    customer_segment   VARCHAR(50),
    registration_date  DATE
);

CREATE TABLE accounts (
    account_id      INT PRIMARY KEY,
    customer_id     INT,
    account_type    VARCHAR(50),
    balance         DECIMAL(18,2),
    currency        VARCHAR(10),
    opened_date     DATE,
    status          VARCHAR(30),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    transaction_id     INT PRIMARY KEY,
    account_id         INT,
    transaction_date   DATE,
    transaction_type   VARCHAR(50),
    amount             DECIMAL(18,2),
    channel            VARCHAR(50),
    merchant_category  VARCHAR(100),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE loans (
    loan_id        INT PRIMARY KEY,
    customer_id    INT,
    loan_type      VARCHAR(50),
    loan_amount    DECIMAL(18,2),
    interest_rate  DECIMAL(5,2),
    start_date     DATE,
    end_date       DATE,
    loan_status    VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
