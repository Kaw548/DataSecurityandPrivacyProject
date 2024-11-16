CREATE TABLE healthcare (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender BOOLEAN,
    age INT,
    weight FLOAT,
    height FLOAT,
    health_history TEXT
);
