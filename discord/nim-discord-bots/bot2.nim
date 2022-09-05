import dimscord, asyncdispatch, strutils
import dotenv
import strformat
import dimscmd
import json
import options
import os


load()  # load the .env file

let discord = newDiscordClient(getEnv("DISCORD_TOKEN"))
var cmd = discord.newHandler()


proc reply(m: Message, msg: string): Future[Message] {.async.} =
    result = await discord.api.sendMessage(m.channelId, msg)


proc reply(i: Interaction, msg: string) {.async.} =
    echo i
    let response = InteractionResponse(
        kind: irtChannelMessageWithSource,
        data: some InteractionApplicationCommandCallbackData(
            content: msg
        )
    )
    await discord.api.createInteractionResponse(i.id, i.token, response)


type Colour = enum
    Red
    Green
    Blue = "bloo" # passport


#################
# Chat commands #
#################
cmd.addChat("hi") do ():
    # Usage: !hi
    discard await msg.reply("Hello")


cmd.addChat("isPog") do (pog: bool): # I hate myself
    # Usage: !isPog <true/false>
    if pog:
        discard msg.reply("poggers")
    else:
        discard msg.reply("pogn't")
#####################
# end chat commands #
#####################


##################
# Slash commands #
##################

cmd.add_slash("add") do (a: int, b: int):
    ## Adds two numbers
    await i.reply(fmt"{a} + {b} = {a + b}")

######################
# end slash commands #
######################


proc onDispatch(s: Shard, evt: string, data: JsonNode) {.event(discord).} =
    echo data.pretty()

# Do discord events like normal
proc onReady (s: Shard, r: Ready) {.event(discord).} =
    await cmd.registerCommands()
    echo "Ready as " & $r.user


proc interactionCreate (s: Shard, i: Interaction) {.event(discord).} =
    discard await cmd.handleInteraction(s, i)


proc messageCreate (s: Shard, msg: Message) {.event(discord).} =
    if msg.author.bot: return
    # Let the magic happen
    discard await cmd.handleMessage("!", s, msg) # Returns true if a command was handled
    # Or you can pass a list of prefixes
    # discard await cmd.handleMessage(["$$", "@"], s, msg)


waitFor discord.startSession()
