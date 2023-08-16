-- List all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, SUM(tsr.rate) AS rating_sum
FROM tv_shows ts
JOIN tv_show_ratings tsr ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY rating_sum DESC;
