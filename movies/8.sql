 -- Same result but thats my code bellow
 -- SELECT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE movie_id = '114709');
 
SELECT name
FROM people
WHERE id IN
(
    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id = (

        -- Select Toy Story's ID
        SELECT id
        FROM movies
        WHERE title = 'Toy Story'
    )
);
