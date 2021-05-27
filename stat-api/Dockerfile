FROM python:latest
WORKDIR /stat-api
COPY . .
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python","app.py"]