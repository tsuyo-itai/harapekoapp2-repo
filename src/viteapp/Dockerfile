FROM node:20.11.0-slim

WORKDIR /viteapp

COPY . /viteapp

ENV LANG=C.UTF-8 \
    TZ=Asia/Tokyo

RUN npm install

# 必要なときにdocker-compose execから起動すれば良いので一旦マスク
# CMD ["npm", "run", "dev"]