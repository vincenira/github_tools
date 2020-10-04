FROM python:3.7-slim-stretch 

WORKDIR /app

ADD app app/.
COPY application.py .
COPY .flaskenv .
COPY requirements.txt . 
RUN pip install -r requirements.txt
EXPOSE 5000 
CMD ["flask", "run", "--host=0.0.0.0"]