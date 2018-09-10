#!bin/bash

mysql -uroot -proot -hlocalhost -e "
CREATE DATABASE fresco_segment;
use fresco_segment;

CREATE TABLE customer_segments (
  party_id VARCHAR(20),
  fresco13_mseg  VARCHAR(3),
  fresco13_seg  VARCHAR(3),
  fresco13_sseg VARCHAR(3),
  match_flag CHAR(1)
);

LOAD DATA INFILE './DatasetGenerated.csv' 
INTO TABLE customer_segments 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;"