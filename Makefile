stop_build_run:
	./dc-down.sh
	./dc-build.sh
	./dc-up.sh 

migration:
	python manage.py makemigrations