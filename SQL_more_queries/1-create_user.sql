-- 1-create_user.sql

-- 1. user_0d_1 mövcud deyilsə yaradılır
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 2. Bütün privileges verilir (root səviyyəsində)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- 3. Dəyişiklikləri dərhal aktivləşdir
FLUSH PRIVILEGES;

