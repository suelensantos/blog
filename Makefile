setup: 
	@pip install -r requirements.txt

run: 
	@python manage.py runserver

create-superuser-admin:
	@python manage.py createsuperuser

db-migrations:
	@python manage.py makemigrations meu_blog

db-migrate: db-migrations
	@python manage.py migrate

create-db: 
	@mysql -u root -e "create database db_blog"; 

python-shell:
	@python manage.py shell

test:
	@python manage.py test

pep8:
	@pep8 --ignore=E501 .

pep8-total:
	@pep8 --ignore=E501 . | wc -l

css:
	sass --sourcemap=none --watch meu_blog/static/meu_blog/scss:meu_blog/static/meu_blog/css
