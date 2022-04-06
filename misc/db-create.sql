SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS professor;
DROP TABLE IF EXISTS gender;
DROP TABLE IF EXISTS social_media;
DROP TABLE IF EXISTS concentration;
DROP TABLE IF EXISTS concentrate;
DROP TABLE IF EXISTS job_merged_table;
DROP TABLE IF EXISTS job_merge_relationship;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS job;
DROP table if exists employ;
DROP TABLE IF EXISTS alumni;
SET FOREIGN_KEY_CHECKS = 1;

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




INSERT INTO professor (first_name, last_name)
VALUES ('Antonella', 'Di Lillio');

INSERT INTO gender (gender_text)
VALUES ('male');

INSERT INTO social_media (type, link, last_updated_date)
VALUES ('LinkedIn', 'https://www.linkedin.com/in/ztianqi/', '2022-04-05');

INSERT INTO concentration (concentration_name, concentration_type)
VALUES ('Computer Science', 'major');

INSERT INTO company (company_name, company_city, company_state)
VALUES ('Google', 'New York', 'NY');

INSERT INTO job (job_name)
VALUES ('Junior Software Engineer');

INSERT INTO job_merged_table (job_name)
VALUES ('Software Engineer');

INSERT INTO job_merge_relationship (job_id, job_merged_id)
VALUES ((SELECT job_id FROM job WHERE job_name = 'Junior Software Engineer'),
        (SELECT job_merged_id FROM job_merged_table WHERE job_name = 'Software Engineer'));

INSERT INTO alumni (referred_prof_id,
                    gender,
                    social_media_id,
                    first_name,
                    last_name,
                    class_year,
                    email,
                    current_location_city,
                    current_location_state,
                    alumni_type,
                    last_updated_date)
VALUES ((SELECT professor_id FROM professor WHERE professor.first_name='Antonella' AND professor.last_name='Di Lillio'),
        (SELECT gender_text FROM gender WHERE gender_text='male'),
        (SELECT social_media_id FROM social_media WHERE type='LinkedIn'),
        'Tianqi',
        'Zhao',
        '2023',
        'tianqizhao@brandeis.edu',
        'New York',
        'NY',
        'undergraduate',
        DATE '2022-04-05');

INSERT INTO concentrate (alumni_id, concentration_id)
VALUES ((SELECT alumni_id FROM alumni WHERE alumni.first_name='Tianqi' AND alumni.last_name='Zhao'),
        (SELECT concentration_id FROM concentration WHERE concentration.concentration_name='Computer Science'));

INSERT INTO employ (alumni_id, job_id, company_id, start_date, end_date, sequence)
VALUES ((SELECT alumni_id FROM alumni WHERE alumni.first_name='Tianqi' AND alumni.last_name='Zhao'),
        (SELECT job_id FROM job WHERE job.job_name='Junior Software Engineer'),
        (SELECT company_id FROM company WHERE company.company_name='Google'),
        DATE '2018-02-03',
        DATE '2019-07-06',
        1);

SELECT alumni.alumni_id AS 'alumni_id',
       alumni.first_name AS 'first_name',
       alumni.last_name AS 'last_name',
       gender.gender_text AS 'gender',
       alumni.class_year AS 'class_year',
       alumni.email AS 'email',
       alumni.current_location_city AS 'city',
       alumni.current_location_state AS 'state',
       alumni.alumni_type AS 'alumni_type',
       alumni.last_updated_date AS 'last_updated_by'
FROM alumni
INNER JOIN gender ON alumni.gender = gender.gender_text;
