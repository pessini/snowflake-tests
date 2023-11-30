from snowflake.snowpark.functions import udf
from snowflake.snowpark.types import IntegerType
import utils

session = utils.getSession();

# named UDF (with lambda)
add_six = udf(lambda x: x+6,
  input_types=[IntegerType()], return_type=IntegerType(),
  name="add_six_proc", replace=True)

ret = session.sql("select add_six_proc(1)").collect()[0][0]
print(f"add_six: {ret}")
