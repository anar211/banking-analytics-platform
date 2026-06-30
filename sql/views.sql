-- =========================================================
-- Enterprise Banking Analytics Platform
-- Analytical Views
-- =========================================================

-- Customer portfolio overview
CREATE VIEW customer_portfolio_view AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.customer_segment,
    c.country,
    c.city,
    COUNT(DISTINCT a.account_id) AS total_accounts,
    COALESCE(SUM(a.balance), 0) AS total_balance,
    COUNT(DISTINCT l.loan_id) AS total_loans,
    COALESCE(SUM(l.loan_amount), 0) AS total_loan_amount
FROM customers c
LEFT JOIN accounts a ON c.customer_id = a.customer_id
LEFT JOIN loans l ON c.customer_id = l.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.customer_segment,
    c.country,
    c.city;


-- Monthly transaction summary
CREATE VIEW monthly_transaction_summary AS
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_transaction_amount
FROM transactions
GROUP BY DATE_TRUNC('month', transaction_date);


-- Loan portfolio summary
CREATE VIEW loan_portfolio_summary AS
SELECT
    loan_type,
    loan_status,
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount,
    AVG(interest_rate) AS average_interest_rate
FROM loans
GROUP BY loan_type, loan_status;
