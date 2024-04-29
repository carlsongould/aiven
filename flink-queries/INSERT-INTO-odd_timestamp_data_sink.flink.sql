--Insert into sink from source table query based on whether the time seconds is odd or even.
INSERT INTO odd_timestamp_data_sink
SELECT * 
FROM financial_transactions
WHERE EXTRACT(second FROM payment_timestamp) % 2 <> 0;