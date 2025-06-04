FROM python:3.12-slim

# install dependencies needed for tkinter GUI # \ does is split command into different lines 
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*  

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir helps removing cache after install to lower image size

COPY . .

CMD ["python3", "main.py", "--cli", "--url", "https://www.youtube.com/watch?v=c0FiKIAF2HQ&pp=ygUPMTAgc2Vjb25kIHZpZGVv"]