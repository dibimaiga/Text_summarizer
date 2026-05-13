FROM python:3.9-slim-bullseye

RUN apt-get update -y && apt-get install -y \
    awscli \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD [ "python3", "app.py" ]