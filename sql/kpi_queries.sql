-- =========================================================
-- Enterprise Banking Analytics Platform
-- KPI Queries
-- =========================================================

-- 1. Total number of customers
SELECT 
    COUNT(*) AS total_customers
FROM customers;

-- 2. Active accounts
SELECT 
    COUNT(*) AS active_accounts
FROM accounts
WHERE status = 'Active';

-- 3. Total account balance
SELECT 
    SUM(balance) AS total_balance
FROM accounts;

-- 4. Average account balance
SELECT 
    AVG(balance) AS average_balance
FROM accounts;

-- 5. Total transaction volume
SELECT 
    SUM(amount) AS total_transaction_volume
FROM transactions;

-- 6. Number of transactions
SELECT 
    COUNT(*) AS total_transactions
FROM transactions;

-- 7. Monthly transaction volume
SELECT 
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(amount) AS monthly_transaction_volume
FROM transactions
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY month;

-- 8. Loan portfolio value
SELECT 
    SUM(loan_amount) AS total_loan_portfolio
FROM loans;

-- 9. Average interest rate
SELECT 
    AVG(interest_rate) AS average_interest_rate
FROM loans;

-- 10. Loan status distribution
SELECT 
    loan_status,
    COUNT(*) AS number_of_loans,
    SUM(loan_amount) AS total_amount
FROM loans
GROUP BY loan_status
ORDER BY total_amount DESC;
GROUP BY loan_status
ORDER BY total_amount DESC;
