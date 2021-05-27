FROM python:latest
WORKDIR /race-api
COPY . .
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python","app.py"]