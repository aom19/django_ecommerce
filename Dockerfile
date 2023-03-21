FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r req.txt

COPY /drfecommerce/db.sqlite3 /app/


EXPOSE 8000

CMD ["python","manage.py", "runserver" ,"0.0.0.0:8000"]


