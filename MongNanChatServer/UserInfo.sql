SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";

DROP TABLE IF EXISTS entries;
CREATE TABLE entries(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL REFERENCES users(username),
    ip_address VARCHAR(100) NOT NULL
    add_port VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    public_key VARCHAR(100) NOT NULL
);