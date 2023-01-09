FROM python:3.8

COPY . /logipass
WORKDIR /logipass

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install .

CMD ["python", "logipass/app.py"]