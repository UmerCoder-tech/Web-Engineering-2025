CREATE DATABASE bewerbungsdatenbank CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
"""
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '12345';
EXIT;
"""
CREATE DATABASE IF NOT EXISTS bewerbungsdatenbank;
GRANT ALL PRIVILEGES ON bewerbungsdatenbank.* TO 'root'@'localhost' IDENTIFIED BY '12345';
FLUSH PRIVILEGES;


