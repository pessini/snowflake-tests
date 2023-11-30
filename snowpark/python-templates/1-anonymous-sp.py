from snowflake.snowpark.functions import sproc
from snowflake.snowpark.types import IntegerType
import utils

session = utils.getSession();

# anonymous SP (with lambda)
add_one = sproc(
  lambda session, x: session.sql(f"select {x} + 1").collect()[0][0],
  input_types=[IntegerType()], return_type=IntegerType(),
  packages=["snowflake-snowpark-python"])

ret = add_one(1)
print(f"add_one: {ret}")
