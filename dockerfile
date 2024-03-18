FROM ubuntu:latest as TomDemo
COPY tom.py tom.py
RUN apt-get update
RUN apt-get install python3-pip -y
RUN apt install python3 -y
# COPY requirements.txt requirements.txt
RUN pip install fastapi
RUN pip install requests        
RUN pip install uvicorn
ENTRYPOINT ["uvicorn", "tom:app", "--host", "0.0.0.0"]