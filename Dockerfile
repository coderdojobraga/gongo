# base image for python
FROM python:3.10-alpine3.16

# working directory
WORKDIR /app

# set the required dependencies
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# run the command to start the bot
CMD [ "python3", "-m", "bot"]
