create sequence currency_id_seq start with 1 increment by 1;

create table if not exists currency(
    id   bigint not null default next value for DEMO.PUBLIC.CURRENCY_ID_SEQ primary key,
    name varchar(255),
    rate float(53)
);
