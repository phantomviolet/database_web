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
