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
    FOREIGN KEY (userid) REFERENCES users(id)
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    submissiontime TIMESTAMP,
    userid INT,
    FOREIGN KEY (userid) REFERENCES users(id)
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    videoid INT,
    userid INT,
    content TEXT,
    submissiontime TIMESTAMP,
    FOREIGN KEY (videoid) REFERENCES videos(id),
    FOREIGN KEY (userid) REFERENCES users(id)
);

-- Example data

INSERT INTO users (username, password)
VALUES ('Herra', 'Password');

INSERT INTO videos(
    audioaddress,
    videoaddress,
    userid,
    title,
    description,
    viewcount,
    submissiontime
)
VALUES (
    'ZeBKgxqfvN0',
    'nwfCoKNI5hs',
    (SELECT id FROM users WHERE username='Herra'),
    'My Foggy Valentine Breakdown',
    'bojojoing',
    0,
    NOW()
);

INSERT INTO videos(
    audioaddress,
    videoaddress,
    userid,
    title,
    description,
    viewcount,
    submissiontime
)
VALUES (
    'LB9lObWclFQ',
    'fdGWRq1dVBA',
    (SELECT id FROM users WHERE username='Herra'),
    'Ka-chow',
    'This is a video description',
    0,
    NOW()
);

INSERT INTO videos(
    audioaddress,
    videoaddress,
    userid,
    title,
    description,
    viewcount,
    submissiontime
)
VALUES (
    'upbwQPeGm0Q',
    '6Maq5IyHSuc',
    (SELECT id FROM users WHERE username='Herra'),
    'Educational',
    'Nice components!',
    0,
    NOW()
);