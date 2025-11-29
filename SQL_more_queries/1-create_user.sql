-- user_0d_1 yarat və root privileges ver
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- privileges-i yoxla
SHOW GRANTS FOR 'user_0d_1'@'localhost';

