drop table if exists users;
drop table if exists words;
drop table if exists game;

create table users
  (
    uid serial primary key,
    user_name  varchar(200) not null,
    user_score integer null
);

create table words
  (
    wid serial primary key,
    word varchar(200) not null,
    word_score integer null,
    level integer null 
);

create table game
  (
    gid serial primary key,
    uid integer REFERENCES users,
    wid integer REFERENCES words,
    result bool null,
    total_time integer null
);


insert into users (user_name, user_score) values
    ('arun', 100)
    ('bhargav', 90)
    ('sagar', 110)