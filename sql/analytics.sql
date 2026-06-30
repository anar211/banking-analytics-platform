-- =========================================================
-- Enterprise Banking Analytics Platform
-- Analytical Queries
-- =========================================================

-- 1. Customers by segment
SELECT 
    customer_segment,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_segment
ORDER BY total_customers DESC;

-- 2. Customers by city
SELECT 
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-- 3. Account balance by account type
SELECT 
    account_type,
    SUM(balance) AS total_balance,
    AVG(balance) AS average_balance
FROM accounts
GROUP BY account_type
ORDER BY total_balance DESC;

-- 4. Transaction volume by channel
SELECT 
    channel,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY channel
ORDER BY total_amount DESC;

-- 5. Top merchant categories by transaction volume
SELECT 
    merchant_category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY merchant_category
ORDER BY total_amount DESC;

-- 6. Loan portfolio by loan type
SELECT 
    loan_type,
    COUNT(*) AS number_of_loans,
    SUM(loan_amount) AS total_loan_amount,
    AVG(interest_rate) AS average_interest_rate
FROM loans
GROUP BY loan_type
ORDER BY total_loan_amount DESC;

-- 7. Customer-level financial overview
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.customer_segment,
    COUNT(DISTINCT a.account_id) AS total_accounts,
    SUM(a.balance) AS total_balance,
    COUNT(DISTINCT l.loan_id) AS total_loans,
    SUM(l.loan_amount) AS total_loan_amount
FROM customers c
LEFT JOIN accounts a ON c.customer_id = a.customer_id
LEFT JOIN loans l ON c.customer_id = l.customer_id
GROUP BY 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.customer_segment
ORDER BY total_balance DESC;
