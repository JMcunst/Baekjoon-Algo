SELECT BRANCH_ID, COUNT(CNT) AS '계약 건수'
FROM EMPLOYEES
JOIN (SELECT EMPLOYEE_ID, COUNT(EMPLOYEE_ID) AS CNT FROM SELLINGS GROUP BY EMPLOYEE_ID) AS B
ON EMPLOYEES.ID = B.EMPLOYEE_ID
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID ASC