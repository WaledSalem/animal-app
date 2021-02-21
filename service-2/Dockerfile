From python:3.9-slim-buster

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT ["python", "app.py"]
