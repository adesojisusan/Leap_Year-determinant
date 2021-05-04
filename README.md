A simple todo app using postgres db and flask

Teminal commands
create todoapp
$ FLASK_APP=app.py FLASK_DEBUG=true flask run
psql todoapp
>>> \dt
>>> \d todos
>>> INSERT INTO todos (description) VALUES ('Do a thing 1');
>>> INSERT INTO todos (description) VALUES ('Do a thing 2');
>>> INSERT INTO todos (description) VALUES ('Do a thing 3');
>>> INSERT INTO todos (description) VALUES ('Do a thing 4');
>>> select * from todos;
