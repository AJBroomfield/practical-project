FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && pip install pymysql
EXPOSE 5000
ENTRYPOINT ["python","app.py"]