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

"""
CREATE TEMPORARY PROCEDURE  "SNOWPARK_PYTHON"."PUBLIC".SNOWPARK_TEMP_PROCEDURE_AKVX7KYLAY(arg1 INT)
RETURNS INT
LANGUAGE PYTHON 
VOLATILE
RUNTIME_VERSION=3.9

PACKAGES=('snowflake-snowpark-python','cloudpickle==2.0.0')


HANDLER='compute'
EXECUTE AS OWNER


AS $$
import pickle
func = pickle.loads(bytes.fromhex('800...52302e'))
def compute(session,arg1):
    return func(session,arg1)
$$
"""
