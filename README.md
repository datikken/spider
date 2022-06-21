 ```docker exec -it django_web_1 python manage.py makemigrations```

 ```docker exec -it django_web_1 python manage.py migrate```
 
```docker exec -it django_web_1 django-admin shell -i python```

```docker exec -it django_web_1 python -m playwright install --with-deps```