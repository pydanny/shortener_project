# Some helpful utility commands

all: 
	heroku pgbackups:capture --expire
	git push heroku master
	heroku run python shortener/manage.py syncdb --noinput  --settings=shortener.settings.production
	heroku run python shortener/manage.py migrate --settings=shortener.settings.production
	heroku run python shortener/manage.py collectstatic --noinput --settings=shortener.settings.production

deploy:
	heroku pgbackups:capture --expire
	git push heroku master
	heroku run python shortener/manage.py syncdb --noinput  --settings=shortener.settings.production
	heroku run python shortener/manage.py migrate --settings=shortener.settings.production

style:
	git push heroku master
	heroku run python shortener/manage.py collectstatic --noinput --settings=shortener.settings.production

restoredata:
	heroku pgbackups:capture --expire
	curl -o latest.dump `heroku pgbackups:url`
	dropdb shortener
	createdb shortener
	pg_restore --verbose --clean --no-acl --no-owner -d shortener latest.dump

shell:
	heroku run python shortener/manage.py shell_plus --settings=shortener.settings.production

createsite:
	heroku create --stack cedar
	heroku addons:add sendgrid:starter
	heroku addons:add heroku-postgresql:dev
	heroku addons:add pgbackups
	git push heroku master
	heroku ps:scale web=1
	heroku run python manage.py syncdb --noinput  --settings=shortener.settings.production
	heroku run python manage.py migrate --settings=shortener.settings.production