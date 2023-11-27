import snowflake.connector
import os
import pandas as pd

with snowflake.connector.connect(
    account="XLB86271",
    user="cscutaru",
    password=os.environ["SNOWSQL_PWD"],
    database="EMPLOYEES",
    schema="PUBLIC") as conn:

    with conn.cursor() as cur:
        sql = "select name, path from employee_hierarchy order by path"
        cur.execute(sql)
        for row in cur: print(row)

        df = cur.fetch_pandas_all()
        print(df)

    sql = "call show_tree_simple('employee_manager')"
    df = pd.read_sql(sql, conn)
    print(df)