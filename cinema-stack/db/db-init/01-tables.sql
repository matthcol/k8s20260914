create table movie (
	id serial constraint pk_movie primary key,
	title varchar(300) not null,
	year smallint not null,
	duration smallint null
);