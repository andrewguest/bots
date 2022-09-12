FROM python:3.10-bullseye

# Define a HOME_DIR variable
ARG HOME_DIR=/steam-game-picker-bot

# Create the HOME_DIR and logs directories
RUN mkdir -p ${HOME_DIR}/logs

# Add all of the project files
ADD . ${HOME_DIR}

WORKDIR ${HOME_DIR}

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
