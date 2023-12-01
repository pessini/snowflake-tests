!set variable_substitution=true

CREATE OR REPLACE DATABASE stage_upload;
CREATE STAGE mystage;

-- transfer files
!define CRT_DIR=file://C:\Projects\snowflake-tests\var-substitution
PUT &CRT_DIR\file-upload.sql @mystage;
PUT &CRT_DIR\create-multi-tenant.sql @mystage;
PUT &CRT_DIR\cleanup-multi-tenant.sql @mystage;

LIST @mystage;