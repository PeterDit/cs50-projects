-- Songs with a feature have a 'feat' in their names
-- LIKE is similar or the same as == (equal to)
-- % means some potentional characters
SELECT name FROM songs WHERE name LIKE '%feat.%';
