FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && pip install pymysql
ENV DATABASE_URI=${DATABASE_URI}
EXPOSE 5000
ENTRYPOINT ["python","app.py"]