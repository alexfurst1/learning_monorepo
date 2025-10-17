CREATE TABLE weather (
    city    varchar(80), -- string of 80 characters max
    temp_lo int, -- int is int
    temp_hi int,
    prcp    real, -- real means float
    the_date    date -- date is a datatype for some reason (YYYY-MM-DD)
);

CREATE TABLE cities (
    name varchar(80),
    location point 
)

-- DROP TABLE 'tablename' 
-- lets you drop whatever table (duh)

INSERT INTO weather VALUES (
    'San Francisco', 46, 50, 0.25, '1994-11-27'
)

