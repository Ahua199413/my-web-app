FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# 網頁通常跑在 5000 埠
EXPOSE 5000
CMD ["python", "app.py"]