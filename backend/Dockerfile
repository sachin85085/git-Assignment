FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask flask-cors pymongo
EXPOSE 5000
CMD ["python", "app.py"]