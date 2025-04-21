
-- SELECT id FROM artists WHERE name = 'Post Malone';
-- to find out the id from post malone (54)
-- Or SELECT name FROM songs WHERE artist_id = (SELECT id FROM artists WHERE name = 'Post Malone');
SELECT name FROM songs WHERE artist_id = 54
