# Deploying the bot:

[Option 1: As a Linux service](#option-1-as-a-linux-service)

[Option 2: As a Docker container](#option-2-as-a-docker-container)

[Option 3: As a Kubernetes pod](#option-3-as-a-kubernetes-pod)

---

## Option 1: As a Linux service

You need a Discord token for this bot to work. This bot only needs the **Send Message** permission.

1. Create a **config.yaml** file:
   1. `cp config/config.yaml.template config/config.yaml`

2. Update the values in the new **config.yaml** file to match your needs.

    |Environment variable|Description|
    |---|---|
    |STEAM_GAME_PICKER_DISCORD_TOKEN|Your Discord auth token for this bot.|
    |STEAM_GAME_PICKER_LOGGING_DIR|The directory to store the logs for this bot.|
    |STEAM_GAME_PICKER_LOGFILE_NAME_FORMAT|Format for the filename of the log file.|

3. Install the required packages:
   1. `pip install -r requirements.txt`

4. Create a service file to run the bot as a Linux service:
   1. `cp deploy/linux-service/steam-game-picker-bot.service.template /etc/systemd/system/steam-game-picker-bot.service`

        |Field|Description|
        |---|---|
        |User|The OS user to run the service as. If you don't specify a user, the service will run as root.|
        |Group|The OS group to run the service as.|
        |ExecStart|Command(s) to run.|

5. Start the new service:
   1. `systemctl enable steam-game-picker-bot && systemctl start steam-game-picker-bot`

---

## Option 2: As a Docker container

You need a Discord token for this bot to work. This bot only needs the **Send Message** permission.

1. Create a **config.yaml** file:
   1. `cp config/config.yaml.template config/config.yaml`

2. Update the values in the new **config.yaml** file to match your needs.

    |Environment variable|Description|
    |---|---|
    |STEAM_GAME_PICKER_DISCORD_TOKEN|Your Discord auth token for this bot.|
    |STEAM_GAME_PICKER_LOGGING_DIR|The directory to store the logs for this bot.|
    |STEAM_GAME_PICKER_LOGFILE_NAME_FORMAT|Format for the filename of the log file.|

3. Build the image:
   1. `docker build -f deploy/Docker/Dockerfile -t steam-game-picker-bot .`

4. Run the container:
   1. `docker run -d steam-game-picker-bot`

---

## Option 3: As a Kubernetes pod

You need a Discord token for this bot to work. This bot only needs the **Send Message** permission.

1. Copy the `config.yaml.template` template file:
    `cp config/config.yaml.template config/config.yaml`

2. Update the `config/config.yaml` file with the appropriate values.

    |Environment variable|Description|
    |---|---|
    |STEAM_GAME_PICKER_DISCORD_TOKEN|Your Discord auth token for this bot.|
    |STEAM_GAME_PICKER_LOGGING_DIR|The directory to store the logs for this bot.|
    |STEAM_GAME_PICKER_LOGFILE_NAME_FORMAT|Format for the filename of the log file.|

3. Build the Docker image:
   1. `docker build -f deploy/Docker/Dockerfile -t steam-game-picker-bot:latest .`

4. Apply the Kubernetes files:
    ```bash
    kubectl apply -f deploy/Kubernetes/namespace.yaml  # Create the custom namespace
    kubectl apply -f deploy/Kubernetes/deployment.yaml  # Create the deployment
    ```
