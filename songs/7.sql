-- SELECT id FROM artists WHERE name = 'Drake'; (to get 23)
-- SELECT AVG(energy) FROM songs WHERE id = 23;
SELECT AVG(energy)
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = 'Drake';
