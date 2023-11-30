from snowflake.snowpark.functions import sproc
from snowflake.snowpark.types import IntegerType
import utils

session = utils.getSession();

# named SP (with lambda)
add_two = sproc(
  lambda session, x: session.sql(f"select {x} + 2").collect()[0][0],
  input_types=[IntegerType()], return_type=IntegerType(),
  name="add_two_proc", replace=True,
  packages=["snowflake-snowpark-python"])

ret = session.call("add_two_proc", 1)
print(f"add_two: {ret}")
