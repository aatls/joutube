CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);
CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    audioaddress TEXT,
    videoaddress TEXT,
    title TEXT,
    description TEXT,
    viewcount INT,
    submissiontime TIMESTAMP
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    submissiontime TIMESTAMP
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    videoid INT,
    content TEXT,
    submissiontime TIMESTAMP
);