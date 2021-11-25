pip install virtualenv        
virtualenv projectenv


source projectenv/bin/activate
pip install django
pip install djangorestframework django-cors-headers





migrate 

python manage.py makemigrations todo
python manage.py migrate todo  


python manage.py runserver