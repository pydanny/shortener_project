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
	heroku run python shortener/manage.py syncdb --noinput  --settings=shortener.settings.production
	heroku run python shortener/manage.py migrate --settings=shortener.settings.production

firefox:
	curl --header 'Host: www.2scoops.co' --header 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8' --header 'Accept-Language: en-US,en;q=0.98,de-DE;q=0.96,de;q=0.94,pt-BR;q=0.93,pt;q=0.91,en-en;q=0.89,uk-UA;q=0.87,uk;q=0.85,en-gb;q=0.83,fr-FR;q=0.81,fr;q=0.8,utf-8;q=0.78,utf;q=0.76,ja-JP;q=0.74,ja;q=0.72,en-UK;q=0.7,en-ca;q=0.69,de-formal;q=0.67,en-au;q=0.65,es-ES;q=0.63,es;q=0.61,zh-CN;q=0.59,zh;q=0.57,en-US.UTF-8;q=0.56,da-DK;q=0.54,da;q=0.52,en-local;q=0.5,cs-CZ;q=0.48,cs;q=0.46,de-DE.UTF-8;q=0.44,de-CH;q=0.43,ko-KR;q=0.41,ko;q=0.39,sk-SK;q=0.37,sk;q=0.35,it-IT;q=0.33,it;q=0.31,lv-LV;q=0.3,lv;q=0.28,ru-RU;q=0.26,ru;q=0.24,he-IL;q=0.22,he;q=0.2,tr-TR;q=0.19,tr;q=0.17,nl-NL;q=0.15,nl;q=0.13,es-CL;q=0.11,en-EU;q=0.09,en-us;q=0.07,en-GB;q=0.06,de-de;q=0.04,zh-hk;q=0.02' --header 'Content-Type: application/x-www-form-urlencoded' --header 'Cookie: csrftoken=huOzGbdXWdy5GpxmuLDcZGPHGiTMof7D' 'http://127.0.0.1:8000/1.6-errata/' -J -L > test.html