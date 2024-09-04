--- creates the database hbtn_0d_usa 
--- creates the table states
CREATE DATABASE IF NOT EXIST 'hbtn_0d_usa '
CREATE TABLE IF NOT EXIST 'states ' ( PRIMARY KEY ('id'), 'id' INT NOT NULL AUTO_INCREMENT , 'name' VARCHAR(256) NOT NULL)
);
