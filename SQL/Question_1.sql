use ritam;

drop table runners;

create table runners(
id int,
name varchar(30)
);

insert into runners values(1,"John Doe"),
(2,"Jane Doe"),
(3,"Alice Jones"),
(4,"Bobby Louis"),
(5,"Lisa Romero")
;

select * from runners;

create table races(
id int,
event varchar(30),
winner_id int
);

insert into races values(1,"100 meter dash",2),
(2,"500 meter dash",2),
(3,"cross-country",2),
(4,"triathalon",null)
;

select * from races;


SELECT * FROM runners WHERE id NOT IN (SELECT winner_id FROM races);
/*This query uses a subquery to find the winner_id values from the "races" table and selects the runners whose IDs are not in that list, indicating they have not won any races.*/

SELECT *
FROM runners
WHERE NOT EXISTS (
    SELECT 1
    FROM races
    WHERE winner_id IS NOT NULL
    AND winner_id = runners.id
);

