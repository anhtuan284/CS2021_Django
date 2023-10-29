# CS2021_Django

1. Pip install -r requirements.txt
2. py manage.py migrate
3. Check DB user info in settings.py
4. py ./manage.py loaddata courseapp.json

# At the end ./manage.py dumpdata > courseapp.json

- Restore fresh database

When you backup whole database by using dumpdata command, it will backup all the database tables

If you use this database dump to load the fresh database(in another django project), it can be causes IntegrityError (If you loaddata in same database it works fine)

To fix this problem, make sure to backup the database by excluding contenttypes and auth.permissions tables
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json

then

./manage.py loaddata db.json
