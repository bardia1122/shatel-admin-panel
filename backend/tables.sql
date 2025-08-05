-- Active: 1754394573846@@127.0.0.1@5434@appdb
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    permissions TEXT NOT NULL
);

drop Table users

CREATE TABLE kbs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL 
);