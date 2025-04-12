CREATE TABLE IF NOT EXISTS respondents (
    id SERIAL PRIMARY KEY,
    date VARCHAR,
    respondent INTEGER,
    sex INTEGER,
    age INTEGER,
    weight FLOAT
);

COPY respondents(date, respondent, sex, age, weight)
FROM '/docker-entrypoint-initdb.d/data.csv'
DELIMITER ',' CSV HEADER;
