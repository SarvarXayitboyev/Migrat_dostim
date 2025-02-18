FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Faqat requirements.txt faylini yuklaymiz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Keyin boshqa fayllarni yuklaymiz
COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
