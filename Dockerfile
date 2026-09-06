From node:18

WORKDIR /app

COPY . .

EXPOSE 3000

RUN pip install -r requirements.txt 

CMD ["node", "app.js"]

