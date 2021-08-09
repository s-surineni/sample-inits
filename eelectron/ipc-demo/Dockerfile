FROM node
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]
# run with docker run -it -v "$(pwd)":/usr/src/app ssurineni/ipc-demo bash
