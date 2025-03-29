# Write your MySQL query statement below
WITH COUNTS AS (
    SELECT *, COUNT(*) OVER(PARTITION BY dep_id) AS dep_count
    FROM Employees
)

SELECT emp_name AS manager_name, dep_id
FROM COUNTS
WHERE position = 'Manager'
AND dep_count = (SELECT MAX(dep_count) FROM COUNTS)
ORDER BY dep_id;

-- select emp_name, dep_id from (select *, count(*) over (partition by dep_id) as dep_count from employees) where position='Manager' and dept_count= (select max(dept_count) from (select *, count(*) over (partition by dep_id)) as dept_count from employees) order by dep_id;