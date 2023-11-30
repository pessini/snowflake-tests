from snowflake.snowpark import Session
import os

# connect to Snowflake with Snowpark
pars = {
    "account": "XLB86271",
    "user": "cscutaru",
    "password": os.environ["SNOWSQL_PWD"],
    "database": "EMPLOYEES",
    "schema": "PUBLIC" }
session = Session.builder.configs(pars).create()

"""
select dname, sum(sal)
  from emp join dept on emp.deptno = dept.deptno
  where dname <> 'RESEARCH'
  group by dname
  order by dname;
"""
emps = session.table("EMP").select("DEPTNO", "SAL")
depts = session.table("DEPT").select("DEPTNO", "DNAME")
q = emps.join(depts, emps.deptno == depts.deptno)

q = q.filter(q.dname != 'RESEARCH')
(q.select("DNAME", "SAL")
  .group_by("DNAME")
  .agg({"SAL": "sum"})
  .sort("DNAME")
  .show())

"""
SELECT  *  FROM ( SELECT "DNAME", sum("SAL") AS "SUM(SAL)" 
FROM ( SELECT "DNAME", "SAL" FROM ( SELECT  *  
FROM (( SELECT "EMPNO" AS "EMPNO", "DEPTNO" AS "l_nl70_DEPTNO", 
"SAL" AS "SAL" FROM EMP) AS SNOWPARK_LEFT 
INNER JOIN ( SELECT "DEPTNO" AS "r_zfpz_DEPTNO", "DNAME" AS "DNAME" FROM DEPT) 
AS SNOWPARK_RIGHT ON ("l_nl70_DEPTNO" = "r_zfpz_DEPTNO"))) 
WHERE ("DNAME" != 'RESEARCH')) GROUP BY "DNAME") ORDER BY "DNAME" ASC NULLS FIRST LIMIT 10
"""