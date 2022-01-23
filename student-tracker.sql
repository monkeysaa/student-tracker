--
-- PostgreSQL database dump
--

-- Dumped from database version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: prefixes; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.prefixes (
    prefix character varying(10) NOT NULL,
    origin character varying(10)
);


ALTER TABLE public.prefixes OWNER TO vagrant;

--
-- Name: students; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.students (
    id integer NOT NULL,
    first_name character varying(30),
    last_name character varying(30),
    grade integer,
    root_level character varying(10),
        -- Root: CVC ("bat"), CCVC / CVCC, CCVCC
    prefixes boolean,
    suffixes boolean
);


ALTER TABLE public.students OWNER TO vagrant;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO vagrant;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: suffixes; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.suffixes (
    suffix character varying(10) NOT NULL,
    origin character varying(15)
);


ALTER TABLE public.suffixes OWNER TO vagrant;

--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Data for Name: prefixes; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.prefixes (prefix, origin) FROM stdin;
pre	Latin
re	Latin
mis	Latin
un	Latin
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.students (id, first_name, last_name, grade, reading_level) FROM stdin;
1	Mark	Park	4	O
2	Ava	Mol	3	N
3	Matt	Grito	5	N
5	Emmy	Student	5	U
6	Syd	Sharisse	5	S
4	Cory	Creator	5	P
\.


--
-- Data for Name: suffixes; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.suffixes (suffix, origin) FROM stdin;
tion	Latin
tive	Latin
ture	Latin
ing	inflectional
ed	inflectional
er	inflectional
s	inflectional
es	inflectional
est	inflectional
\.


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.students_id_seq', 6, true);


--
-- Name: prefixes prefixes_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.prefixes
    ADD CONSTRAINT prefixes_pkey PRIMARY KEY (prefix);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: suffixes suffixes_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.suffixes
    ADD CONSTRAINT suffixes_pkey PRIMARY KEY (suffix);


--
-- PostgreSQL database dump complete
--

