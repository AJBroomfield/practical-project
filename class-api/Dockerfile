FROM python:latest
WORKDIR /class-api
COPY . .
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python","app.py"]