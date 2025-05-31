# Enkel voor het serveren van de reeds gebouwde frontend
FROM node:18

WORKDIR /app
COPY dist/ .

RUN npm install -g serve

CMD ["serve", "-s", ".", "-l", "4173"]
