-- run from current folder: snowsql -c demo_conn -f create-script.sql
use schema employees.public;

-- create test target table, stage and pipe
create or replace table emp_pipe like emp;

create or replace stage mystage_pipe;

create or replace pipe mypipe
  auto_ingest = false
as
  copy into emp_pipe from @mystage_pipe;

-- upload both CSV files from the local data folder into the internal stage
put file://C:\Projects\snowflake-tests\snowpipe-api\data\*.csv @mystage_pipe
  overwrite=true auto_compress=false;

-- should show the two uploaded CSV files
list @mystage_pipe;

-- after the transfer, check again if properly populated
select * from emp_pipe;
