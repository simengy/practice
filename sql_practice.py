TABLES:
EMP - EmpId(Primary Key), EmpSal, DeptId(FK), EmpName, MgrId
DEPT - DeptId(Primary Key), DeptLoc(has data like US, India, China...list of countries), DeptName


Q: Employeename who has the 2nd highest salary


select EmpName from EMP
order by EmpSal DESC
limit 2


100
100
90
90
80
80

Select EmpName from EMP
Where EmpSal in
(
Select distinct EmpSal from EMP
order by EmpSal DESC
limit 2
)


Q: DeptName and 2nd highest salary within that Dept

Select DeptName, EmpID, EmpSal from
(
EMP A
inner join
DEPT B
on A.DeptId=B.DeptId
) C
rank() over(partition by C.DepName, C.EmpID order by C.EmpSal) as rank
where rank = 2


-- INPUT DATA
-- table t1
-- date  product_name   quantity_sold
-- 1 / 1 / 2013 A   100
-- 1 / 1 / 2013 B   200
-- 1 / 1 / 2013 C   300
-- 1 / 2 / 2013 A   101
-- 1 / 2 / 2013 C   301
-- 1 / 3 / 2013 A   102
-- 1 / 3 / 2013 B   202
-- 1 / 3 / 2013 C   302
--------------------------------------------------------------------------------------------------------
-- QUESTION
--  # you have a table t1 with 3 columns showing quantity sold per product per day, as shown above
--  # there are only 3 possible products in the table: A, B, and C
--  # write SQL code to reformat the data as shown below
# the resulting data should be in 4 columns: {date, quantity of product A sold,
--
-- quantity of product B sold, and quantity of product C sold}
- -------------------------------------------------------------------------------------------------------
-- DESIRED OUTPUT
- - date  qty_prod_a  qty_prod_b  qty_prod_c
- - 1 / 1 / 2013 100    200          300
- - 1 / 2 / 2013 101      0      301
- - 1 / 3 / 2013 102    202      302

select date, * from
t1
group by
date
