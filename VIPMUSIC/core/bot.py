# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, <https://github.com/THE-VIP-BOY-OP>.
# This file is part of <https://github.com/THE-VIP-BOY-OP/VIP-MUSIC> project,
# and is released under the "GNU v3.0 License Agreement".
# Please see <https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE>
# All rights reserved.

import asyncio
import threading

import uvloop

uvloop.install()

from flask import Flask
from pyrogram import Client, idle
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import (
    BotCommand,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

import config

from ..logging import LOGGER

uvloop.install()

# Flask app initialize
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running"


def run():
    app.run(host="0.0.0.0", port=8000, debug=False)


# VIPBot Class
class VIPBot(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot")
        super().__init__(
            "VIPMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")
        self.mention = get_me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="˹ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ˼",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )

        if config.LOG_GROUP_ID:
            try:
                await self.send_photo(
                    config.LOG_GROUP_ID,
                    photo=config.START_IMG_URL,
                    caption=f"❖ 𝐅𝐮𝐛𝐮𝐤𝐢 𝐢𝐬 𝐡𝐞𝐫𝐞 𝐛𝐚𝐛𝐞𝐬 \n\n❖ 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲\n\n❖ {self.name}\n❖ `{self.id}` \n\n❖ @{self.username} \n\n  𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐦𝐞 𝐂𝐇𝐎𝐂𝐎 \n\n--------------------------༶",
                    reply_markup=button,
                )
            except pyrogram.errors.ChatWriteForbidden as e:
                LOGGER(__name__).error(f"Bot cannot write to the log group: {e}")
                try:
                    await self.send_message(
                        config.LOG_GROUP_ID,
                        f"❖ 𝐅𝐮𝐛𝐮𝐤𝐢 𝐢𝐬 𝐡𝐞𝐫𝐞 𝐛𝐚𝐛𝐞𝐬\n\n❖ 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲\n\n❖ {self.name}\n\n❖ `{self.id}` \n❖ @{self.username} \n\n  𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐦𝐞 𝐂𝐇𝐎𝐂𝐎 \n\n--------------------------༶",
                        reply_markup=button,
                    )
                except Exception as e:
                    LOGGER(__name__).error(f"Failed to send message in log group: {e}")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Unexpected error while sending to log group: {e}"
                )
        else:
            LOGGER(__name__).warning(
                "LOG_GROUP_ID is not set, skipping log group notifications."
            )
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", "Start the bot"),
                        BotCommand("help", "Get the help menu"),
                        BotCommand("ping", "Check if the bot is alive or dead"),
                    ],
                    scope=BotCommandScopeAllPrivateChats(),
                )
                await self.set_bot_commands(
                    commands=[
                        BotCommand("play", "Start playing requested song"),
                        BotCommand("stop", "Stop the current song"),
                        BotCommand("pause", "Pause the current song"),
                        BotCommand("resume", "Resume the paused song"),
                        BotCommand("queue", "Check the queue of songs"),
                        BotCommand("skip", "Skip the current song"),
                        BotCommand("volume", "Adjust the music volume"),
                        BotCommand("lyrics", "Get lyrics of the song"),
                    ],
                    scope=BotCommandScopeAllGroupChats(),
                )
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", " Start the bot"),
                        BotCommand("ping", " Check the ping"),
                        BotCommand("help", " Get help"),                     
                        BotCommand("cancel", " Cancel the tagging"),
                        BotCommand("settings", " Get the settings"),
                        BotCommand("play", " Play the requested song"),
                        BotCommand("vplay", " Play video along with music"),
                        BotCommand("end", " Empty the queue"),
                        BotCommand("playlist", " Get the playlist"),
                        BotCommand("stop", " Stop the song"),
                        BotCommand("song", " Download the requested song"),
                        BotCommand("video", " Download the requested video song"),
                    ],
                    scope=BotCommandScopeAllChatAdministrators(),
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to set bot commands: {e}")

        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error(
                        "Please promote Bot as Admin in Logger Group"
                    )
            except Exception as e:
                LOGGER(__name__).error(f"Error occurred while checking bot status: {e}")

        LOGGER(__name__).info(f"MusicBot Started as {self.name}")


# Define the async boot function
async def anony_boot():
    bot = VIPBot()
    await bot.start()
    await idle()


if __name__ == "__main__":
    LOGGER(__name__).info("Starting Flask server...")

    # Start Flask server in a new thread
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    LOGGER(__name__).info("Starting SUNLIGHTBot...")

    # Run the bot
    asyncio.run(anony_boot())

    LOGGER(__name__).info("Stopping SUNLIGHTBot...")
