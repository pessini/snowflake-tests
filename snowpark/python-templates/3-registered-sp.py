from snowflake.snowpark import Session
from snowflake.snowpark.functions import sproc
import utils

session = utils.getSession()

session.add_packages("snowflake-snowpark-python", "pandas")
# session.add_import(...)
# session.add_requirements(...)

# registered SP
@sproc(name="add_three", replace=True,
  is_permanent=True, stage_location="@mystage")
def add_three(session: Session, x: int) -> int:
  return session.sql(f"select {x} + 3").collect()[0][0]

ret = session.sql("call add_three(1)").collect()[0][0]
print(f"add_three: {ret}")
