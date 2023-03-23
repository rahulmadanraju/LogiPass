FROM python:3.8

COPY . /logipass
WORKDIR /logipass

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "logipass/app.py"]
