# Joutube

Joutube is a video platform that allow it's users to mix 2 youtube videos together to create a new holistic video experience. The mixing happens by selecting one video for visuals and other for audio. The creations are saved to a database for other users amusement.

### Implemented features

- User profiles
- Video creation and saving
- Video playback
- View count
- Primitive video search
- Primitive home page
- Primitive UI

### Possible features

- User profile pages
- Video editing
- Video fullscreen support
- Video commenting
- Chat
- Advanced video search
- Advanced recommendation algorithm
- Enjoyable UI
- Moderation tools

### Instructions for testing locally (no fly.io)

- Navigate to the folder where you cloned this repository
- Create a .env file and paste the following there:
```
DATABASE_URL=<the-address-of-your-database>
SECRET_KEY=<your-secret-key>
```
- Activate virtual environment and install dependencies:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
- Define the schema of your database:
```
$ psql < schema.sql
```
- Start the application:
```
$ flask run
```

### Some notes

- The application is still vulnerable to attacks, this will be fixed