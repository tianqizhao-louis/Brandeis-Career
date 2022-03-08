create table company
(
    company_id   int auto_increment
        primary key,
    company_name varchar(255) not null,
    constraint company_company_id_uindex
        unique (company_id),
    constraint company_company_name_uindex
        unique (company_name)
);

create table concentration
(
    concentration_id   int auto_increment
        primary key,
    concentration_name varchar(255) not null,
    constraint concentration_concentration_id_uindex
        unique (concentration_id),
    constraint concentration_concentration_name_uindex
        unique (concentration_name)
);

create table gender
(
    gender_text varchar(255) not null
        primary key,
    constraint gender_gender_text_uindex
        unique (gender_text)
);

create table job
(
    job_id   int auto_increment
        primary key,
    job_name varchar(255) not null,
    constraint job_job_id_uindex
        unique (job_id),
    constraint job_job_name_uindex
        unique (job_name)
);

create table professor
(
    professor_id int auto_increment
        primary key,
    first_name   varchar(255) not null,
    last_name    varchar(255) not null,
    constraint professor_professor_id_uindex
        unique (professor_id)
);

create table alumni
(
    alumni_id        int auto_increment
        primary key,
    referred_prof_id int           null,
    first_name       varchar(255)  not null,
    last_name        varchar(255)  not null,
    gender           varchar(64)   not null,
    class_year       int           not null,
    linkedin_profile varchar(2083) null,
    constraint alumni_alumni_id_uindex
        unique (alumni_id),
    constraint alumni_gender_gender_text_fk
        foreign key (gender) references gender (gender_text),
    constraint alumni_professor_professor_id_fk
        foreign key (referred_prof_id) references professor (professor_id)
);

create table concentrate
(
    alumni_id        int not null,
    concentration_id int not null,
    constraint concentrate_alumni_alumni_id_fk
        foreign key (alumni_id) references alumni (alumni_id),
    constraint concentrate_concentration_concentration_id_fk
        foreign key (concentration_id) references concentration (concentration_id)
);

create table employ
(
    alumni_id        int   not null,
    job_id           int   not null,
    company_id       int   not null,
    years_of_service float null,
    job_seq          int   not null,
    constraint employ_alumni_alumni_id_fk
        foreign key (alumni_id) references alumni (alumni_id),
    constraint employ_company_company_id_fk
        foreign key (company_id) references company (company_id),
    constraint employ_job_job_id_fk
        foreign key (job_id) references job (job_id)
);


