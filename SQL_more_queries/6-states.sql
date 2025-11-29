-- 1. Verilənlər bazasını yaradın (mövcuddursa error verməsin)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Verilənlər bazasını istifadə edin
USE hbtn_0d_usa;

-- 3. states cədvəlini yaradın (mövcuddursa error verməsin)
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

