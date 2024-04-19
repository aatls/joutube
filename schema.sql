CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    audioaddress TEXT,
    videoaddress TEXT,
    userid INT,
    title TEXT,
    description TEXT,
    viewcount INT,
    submissiontime TIMESTAMP,
    FORGEIN KEY (userid) REFERENCES users(id)
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    submissiontime TIMESTAMP,
    userid INT,
    FORGEIN KEY (userid) REFERENCES users(id)
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    videoid INT,
    userid INT,
    content TEXT,
    submissiontime TIMESTAMP,
    FORGEIN KEY (videooi) REFERENCES videos(id),
    FORGEIN KEY (userid) REFERENCES users(id)
);