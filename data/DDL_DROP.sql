SET FOREIGN_KEY_CHECKS = 0;
SELECT
    table_name
FROM
    information_schema.tables
WHERE
    table_schema = 'fblaquiz';
    
DROP TABLE IF EXISTS student_score;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS answer;

SET FOREIGN_KEY_CHECKS = 1;

COMMIT;