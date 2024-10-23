-- create user
SELECT * 
FROM cities 
WHERE state_id = (
    SELECT id 
    from states 
    WHERE name = "California"
    );