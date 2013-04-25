create table if not exists reputation (
  company char(20) not null,
  day date not null,
  value integer not null
);
