-- -- -- SQLite
-- create table company (
--     id integer primary key autoincrement,
--     name text not null,
--     address text not null,
--     callNumber text not null,
--     FAX text not null
-- );

-- insert into company (name, address, callNumber, FAX) 
-- values ('케이엠이', '경기도 부천시 소사본동 364-2', '032-613-5852', '032-613-5853');


-- alter table material drop blueprint_id;
-- insert into company (name, address, callNumber, FAX)
-- VALUES('C', 'C_address', 'C_callNumber', 'C_FAX');

-- create table blueprint(
--     bid integer primary key autoincrement,
--     name text not null,
--     company_id integer not null,
--     foreign key(company_id) references company(id)
-- );

-- ALTER table blueprint rename COLUMN name to bName;

-- INSERT INTO blueprint (bName, company_id)
-- VALUES('blueprint3', 4);

-- DELETE FROM blueprint WHERE bid = 4;

-- create table blueprint(
--     bid integer primary key autoincrement,
--     name text not null,
--     cid integer not null,
--     foreign key(cid) references company(cid)
-- );

-- SELECT *
-- from blueprint, company
-- where blueprint.cid = company.cid;

-- alter table material rename COLUMN mID to mid;
-- create table need(
--     bid integer,
--     mid integer,
--     primary key (bid, mid),
--     foreign key(bid) references blueprint(bid) 
--     on delete cascade on update cascade,
--     foreign key(mid) references material(mid) 
--     on delete cascade on update cascade);

-- insert into company (cname, address, callNumber, FAX)
-- values('D', 'D_address', 'D_callNumber', 'D_FAX'),
--     ('E', 'E_address', 'E_callNumber', 'E_FAX');

-- insert into need (bid, mid)
-- values
--     (1, 645001014),
--     (1, 645001015),
--     (1, 645001016),
--     (2, 645001017),
--     (2, 645002023),
--     (2, 645005004),
--     (3, 645001001),
--     (3, 645001002),
--     (3, 645002001),
--     (4, 645002002),
--     (4, 645003002),
--     (4, 645003003),
--     (5, 645003004),
--     (5, 645090339),
--     (5, 645090340);


-- SELECT material.mid, need.bid, mName, description
-- from material, need
-- where material.mid = need.mid;
-- insert into blueprint (bName, cid)
-- values('blueprint1', 1),
--     ('blueprint2', 2),
--     ('blueprint3', 3),
--     ('blueprint4', 4),
--     ('blueprint5', 5);
-- DROP TABLE blueprint;
-- CREATE TABLE blueprint(
--     bid integer primary key autoincrement,
--     bName text not null,
--     cid integer not null,
--     foreign key(cid) references company(id)
-- );

-- insert into blueprint (bName, cid)
-- values('blueprint1', 1),
--     ('blueprint2', 2),
--     ('blueprint3', 3),
--     ('blueprint4', 4),
--     ('blueprint5', 5);
-- SELECT need.mid, bid, material.mName, description, price
-- from need, material
-- where need.mid = material.mid;

-- SELECT material.mid, need.mid
-- from need, material
-- WHERE need.mid = material.mid;
-- CREATE TABLE need (
--     bid integer,
--     mid integer,
--     primary key (bid, mid),
--     foreign key(bid) references blueprint(bid) on delete cascade on update cascade,
--     foreign key(mid) references material(mid) on delete cascade on update cascade
-- );

-- INSERT INTO need (bid, mid) VALUES
-- (1, 645001014),
-- (1, 645001015),
-- (1, 645001016),
-- (2, 645001017),
-- (2, 645002023),
-- (2, 645005004),
-- (3, 655001001),
-- (3, 655001002),
-- (3, 655002001),
-- (4, 655002002),
-- (4, 655003002),
-- (4, 655003003),
-- (5, 655003004),
-- (5, 655009339),
-- (5, 655009340);

-- SELECT material.mid, need.bid, mName, description
-- FROM material, need
-- WHERE material.mid = need.mid;

-- CREATE TABLE tmp (
--     mid integer primary key ,
--     mName text not null,
--     description text,
--     price integer not null,
--     bid integer,
--     FOREIGN KEY (bid) REFERENCES blueprint(bid) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- INSERT into tmp (mid, mName, description, price, bid)
-- SELECT mid, mName, description, price, bid
-- FROM material

-- CREATE TABLE tmp (
--     mid integer,
--     mName text not null,
--     description text,
--     price integer,
--     bid integer,
--     PRIMARY KEY (mid),
--     FOREIGN KEY (bid) REFERENCES blueprint(bid) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- alter table tmp rename to material;

-- select DISTINCT material.mid, blueprint.bname, material.mname, material.description, material.price
-- from material, blueprint, need
-- where material.bid = blueprint.bid;

-- select DISTINCT material.mid, blueprint.bName, material.mname, material.description, material.price
-- from material, blueprint
-- where material.bid = blueprint.bid and blueprint.bid = 2;

-- create table orderlist (
--     oid integer primary key autoincrement,
--     odate text not null);

-- alter table orderlist add COLUMN cName text not null;

-- DROP table orderlist;
-- create table orderlist (
--     oid integer primary key autoincrement,
--     odate text not null,
--     cName text not null
-- );

-- insert into orderlist (odate, cName)
-- VALUES  ('2021-06-01', 'A'),
--         ('2021-06-02', 'B'),
--         ('2021-06-03', 'C'),
--         ('2021-06-04', 'D'),
--         ('2021-06-05', 'E');

delete
from orderlist
where oid = 6;