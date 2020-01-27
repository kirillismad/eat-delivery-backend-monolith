CREATE DATABASE app;
CREATE USER app_user WITH PASSWORD 'password123';
ALTER ROLE app_user SET client_encoding TO 'utf8';
ALTER ROLE app_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE app_user SET timezone TO 'UTC';
GRANT ALL ON DATABASE app TO app_user;
ALTER USER app_user CREATEDB;

