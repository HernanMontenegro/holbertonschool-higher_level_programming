-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title != 'Dexter' AND tv_genres.id NOT IN (
    SELECT tv_genres.id FROM tv_genres
    INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
GROUP BY tv_genres.name;
