-- List all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, IFNULL(SUM(tsr.rate), 0) AS rating_sum
FROM tv_shows ts
LEFT JOIN tv_show_ratings tsr ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY rating_sum DESC;
