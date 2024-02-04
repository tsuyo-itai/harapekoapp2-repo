FROM python:3.11-slim-bullseye

WORKDIR /fastapiapp

COPY . /fastapiapp

ENV LANG=C.UTF-8 \
    TZ=Asia/Tokyo

# 一旦動かなくなるのもめんどくさいので「--upgrade」は行わない
# RUN pip3 install --no-cache-dir --upgrade -r /fastapiapp/requirements.txt
RUN pip3 install --no-cache-dir -r /fastapiapp/requirements.txt && \
    apt update && apt install -y zip unzip netcat default-mysql-client

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]