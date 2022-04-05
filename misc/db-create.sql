create table company
(
    company_id    int auto_increment
        primary key,
    company_name  varchar(128) not null,
    company_city  varchar(64)  null,
    company_state varchar(64)  null,
    constraint company_company_id_uindex
        unique (company_id)
);

create table concentration
(
    concentration_id   int auto_increment
        primary key,
    concentration_name varchar(64) not null,
    concentration_type varchar(16) not null,
    constraint concentration_concentration_id_uindex
        unique (concentration_id)
);

create table gender
(
    gender_text varchar(16) not null
        primary key,
    constraint gender_gender_text_uindex
        unique (gender_text)
);

create table job
(
    job_id   int auto_increment
        primary key,
    job_name varchar(128) not null,
    constraint job_job_id_uindex
        unique (job_id),
    constraint job_job_name_uindex
        unique (job_name)
);

create table job_merged_table
(
    job_merged_id int auto_increment
        primary key,
    job_name      varchar(128) not null,
    constraint job_merged_table_job_merged_id_uindex
        unique (job_merged_id),
    constraint job_merged_table_job_name_uindex
        unique (job_name)
);

create table job_merge_relationship
(
    job_id        int not null,
    job_merged_id int not null,
    constraint job_merge_relationship_job_job_id_fk
        foreign key (job_id) references job (job_id),
    constraint job_merge_relationship_job_merged_table_job_merged_id_fk
        foreign key (job_merged_id) references job_merged_table (job_merged_id)
);

create table professor
(
    professor_id int auto_increment
        primary key,
    first_name   varchar(64) not null,
    last_name    varchar(64) not null,
    constraint professor_professor_id_uindex
        unique (professor_id)
);

create table social_media
(
    social_media_id   int auto_increment
        primary key,
    type              varchar(32)   not null,
    link              varchar(2083) not null,
    last_updated_date date          not null,
    constraint social_media_social_media_id_uindex
        unique (social_media_id)
);

create table alumni
(
    alumni_id              int auto_increment
        primary key,
    referred_prof_id       int          null,
    gender                 varchar(16)  null,
    social_media_id        int          null,
    first_name             varchar(64)  not null,
    last_name              varchar(64)  not null,
    class_year             year         not null,
    email                  varchar(320) null,
    current_location_city  varchar(64)  null,
    current_location_state varchar(64)  null,
    alumni_type            varchar(32)  null,
    last_updated_date      date         null,
    constraint alumni_alumni_id_uindex
        unique (alumni_id),
    constraint alumni_gender_gender_text_fk
        foreign key (gender) references gender (gender_text),
    constraint alumni_professor_professor_id_fk
        foreign key (referred_prof_id) references professor (professor_id),
    constraint alumni_social_media_social_media_id_fk
        foreign key (social_media_id) references social_media (social_media_id)
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
    alumni_id  int           not null,
    job_id     int           not null,
    company_id int           not null,
    start_date date          null,
    end_date   date          null,
    sequence   int default 1 not null,
    constraint employ_alumni_alumni_id_fk
        foreign key (alumni_id) references alumni (alumni_id),
    constraint employ_company_company_id_fk
        foreign key (company_id) references company (company_id),
    constraint employ_job_job_id_fk
        foreign key (job_id) references job (job_id)
);

