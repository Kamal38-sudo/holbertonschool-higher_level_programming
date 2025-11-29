-- 1. Verilənlər bazasını yaradın (mövcuddursa error verməsin)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 2. user_0d_2 mövcud deyilsə yaradın
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- 3. user_0d_2-ə yalnız SELECT icazəsi verin
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- 4. Dəyişiklikləri aktivləşdirin
FLUSH PRIVILEGES;
