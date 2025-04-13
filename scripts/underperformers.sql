-- Get stats per store
WITH store_stats AS (
    SELECT
        Store,
        COUNT(*) AS total_days,
        SUM(Open) AS open_days,
        AVG(Sales) AS avg_sales,
        AVG(Customers) AS avg_customers,
        ROUND(100.0 * SUM(Open) / COUNT(*), 2) AS open_rate
    FROM rossman
    GROUP BY Store
)
SELECT
    Store,
    avg_sales,
    avg_customers,
    open_rate,
    RANK() OVER (ORDER BY avg_sales ASC) AS sales_rank
FROM store_stats
WHERE open_days > 600;