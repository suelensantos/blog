setup: 
	$ pip install -r requirements.txt

run: 
	$ python manage.py runserver

create-superuser-admin:
	$ python manage.py createsuperuser

db-migrate: 
	$ python manage.py migrate

create-db: 
	$ mysql -u root -e "create database db_blog"; 

python-shell:
	$ python manage.py shell

test:
	$ python manage.py test

