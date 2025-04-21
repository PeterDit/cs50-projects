-- Order BY DESC = Descending order (from 10 to 1.1) With JOIN you can add one table ON another
SELECT rating,title FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2010 ORDER BY rating DESC, title;
