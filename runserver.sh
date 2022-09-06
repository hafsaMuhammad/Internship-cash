echo "Waiting for SQL..."
while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done
echo "SQL started"
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@domain.com', 'P@ssw0rd')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000