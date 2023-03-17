# base image for python
FROM python:3.10-alpine3.16

# set the required dependencies
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt

# install dependencies
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

# copy the content of the local src directory to the working directory
COPY . .

# run the command to start the bot
CMD [ "python3", "-m", "bot"]
