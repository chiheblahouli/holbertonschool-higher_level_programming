-- displays the max temperature of states.
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ASC;
