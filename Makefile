stop_build_run:
	./dc-down.sh
	./dc-build.sh
	./dc-up.sh 

migration:
	python manage.py makemigrations

pgadmin:
	docker run -p 32180:80     \
	-e 'PGADMIN_DEFAULT_EMAIL=hoainam.nv34@gmail.com' \
	-e 'PGADMIN_DEFAULT_PASSWORD=123456a@' \
	-d dpage/pgadmin4