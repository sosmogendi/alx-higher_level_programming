-- Convert the hbtn_0c_0 database to UTF8
USE hbtn_0c_0;
-- Convert the first_table table to UTF8
ALTER TABLE first_table
-- Convert the name field in the first_table to UTF8
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
