from snowflake.snowpark.functions import udtf, lit
from snowflake.snowpark.types import IntegerType, StructType, StructField
import utils

session = utils.getSession()

# UDTF implementation class
class GetTwo:
  def process(self, n):
    yield(1, )
    yield(n, )

# registered (unnamed, temporary) UDTF
get_two = udtf(GetTwo, 
  output_schema=StructType([StructField("number", IntegerType())]),
  input_types=[IntegerType()])

ret = session.table_function(get_two(lit(3))).collect()
print(f"get_two: {ret}")
