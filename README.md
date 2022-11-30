# Passenger Project - Django Practice Project


### MySQL passengerDb Database creation and adding sample data
create database passengerDb;

use passengerDb;

show tables;

select * from passengerapp_passenger;

insert into passengerapp_passenger(fname, lname, travel_points) values ('Zahid', 'Hussain', 145);

insert into passengerapp_passenger(fname, lname, travel_points) values ('Salman', 'Khan', 176);