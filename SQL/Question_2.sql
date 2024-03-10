use ritam;


create table test_a(id numeric);
create table test_b(id numeric);
insert into test_a(id) values
(10),
(20),
(30),
(40),
(50);
insert into test_b(id) values
(10),
(30),
(50);

SELECT test_a.id
FROM test_a
LEFT JOIN test_b ON test_a.id = test_b.id
WHERE test_b.id IS NULL;
