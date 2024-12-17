FROM python:3.12.8

ENV PYTHONUNBUFFERED=1

WORKDIR /CODE

COPY requirements.txt .

RUN  pip install -r requirements.txt

COPY . .

CMD ["python","manage.py", "runserver" ]
