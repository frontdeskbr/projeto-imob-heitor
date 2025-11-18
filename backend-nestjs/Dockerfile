FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci || npm i
COPY . .
ENV PORT=3000
EXPOSE 3000
RUN npx prisma generate
CMD ["sh","-c","npx prisma migrate deploy && npm run start:dev"]
