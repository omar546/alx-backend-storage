-- creates a view need_meeting that of all students with <80 SC not meet for 1 mon.
CREATE VIEW need_meeting AS
SELECT name from students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
