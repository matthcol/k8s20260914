create table person (
	id serial constraint pk_stars primary key,
	name varchar(150) not null,
	birthdate date null
);