
-- JOIN combines rows from two or more tables, based on a related column between them

SELECT AVG(rating) FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2012;
