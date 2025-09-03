# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if it exists)
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application's code
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the development server
CMD ["npm", "run", "dev"]
