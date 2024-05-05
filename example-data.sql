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
    'Bojojoing',
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
    'Educational video',
    'Nice components!',
    0,
    NOW()
);