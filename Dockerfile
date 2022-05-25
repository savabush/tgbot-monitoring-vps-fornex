FROM python:3.10

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "bot.py"]