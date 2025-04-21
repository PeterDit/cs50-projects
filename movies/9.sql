SELECT people.name
FROM stars
JOIN movies ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
-- JOIN 2 tables to get access to birth and year
WHERE movies.year = 2004
ORDER BY people.birth;
