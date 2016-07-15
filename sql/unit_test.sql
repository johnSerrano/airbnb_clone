create user 'airbnb_user_test'@'%' identified by 'default airbnb_test pass';
create database airbnb_test;
grant all privileges on airbnb_test.* to airbnb_user_test;
