## Deploying the bot:

You need a Discord token for this bot to work. This bot only needs the **Send Message** permission.

1. Create a **.env** file: `cp .env.template .env`
2. Update the values in the new **.env** file to match your needs.

    |Environment variable|Description|
    |---|---|
    |STEAM_GAME_PICKER_DISCORD_TOKEN|Your Discord auth token for this bot.|
    |STEAM_GAME_PICKER_LOGGING_DIR|The directory to store the logs for this bot.|
    |STEAM_GAME_PICKER_LOGFILE_NAME_FORMAT|Format for the filename of the log file.|

3. Install the required packages: `pip install -r requirements.txt`

4. [Optional] Create a service file to run the bot as a Linux service: `cp steam-game-picker-bot.service.template /etc/systemd/system/steam-game-picker-bot.service`

    |Field|Description|
    |---|---|
    |User|The OS user to run the service as. If you don't specify a user, the service will run as root.|
    |Group|The OS group to run the service as.|
    |ExecStart|Command(s) to run.|

5. [Optional] Start the new service: `systemctl enable steam-game-picker-bot && systemctl start steam-game-picker-bot`

---