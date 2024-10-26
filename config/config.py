#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get it from my.telegram.org

API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH")


## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")


# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", None)


CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "18000")
)  # Remember to give value in Seconds


# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "3000")
)  # Remember to give value in Minutes


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    "True",
)

# Fill True if you want to load extra plugins


EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/Choco-criminal/Extra-Plugin",
)
# Fill here the external plugins repo where plugins that you want to load


EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

# Your folder name in your extra plugins repo where all plugins stored


# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000")
)  # Remember to give value in Minutes


# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002400130574"))


# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1266240012").split())
)  # Input type must be interger


# make your bots privacy from telegra.ph and put your url here

PRIVACY_LINK = getenv(
    "PRIVACY_LINK", "https://telegra.ph/%F0%9D%90%82%F0%9D%90%80%F0%9D%90%94%F0%9D%90%93%F0%9D%90%88%F0%9D%90%8E%F0%9D%90%8D-10-19"
)


# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")


# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://envs.sh/pi0.jpg",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    "",
)

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting.
AUTO_GCAST = os.getenv("AUTO_GCAST", "on")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/Choco_for_u"
)  # Example:- https://t.me/VIP_CREATORS
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/ANIME_CHAT_ANG"
)  # Example:- https://t.me/TG_FRIENDSS

SUPPORT_CHAT = getenv(
    "SUPPORT_GROUP", "https://t.me/ANIME_CHAT_ANG"
)  # Example:- https://t.me/TG_FRIENDSS
# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", 1800)
)  # Remember to give value in Seconds


# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorize command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")


# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))


# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://envs.sh/pi0.jpg")


# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes


# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", "False")


# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @VIPStringBot
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

#    __      _______ _____    ___  __ _    _  _____ _____ _____   _____   ____ ________
#    \ \    / /_   _|  __ \   |  \/  | |  | |/ ____|_   _/ ____|  |  _ \ / __ \__   __/
#     \ \  / /  | | | |__) |  | \  / | |  | | (___   | || |       | |_) | |  | | | |
#      \ \/ /   | | |  ___/   | |\/| | |  | |\___ \  | || |       |  _ <| |  | | | |
#       \  /   _| |_| |       | |  | | |__| |____) |_| || |____   | |_) | |__| | | |
#        \/   |_____|_|       |_|  |_|\____/|_____/|_____\_____|  |____/ \____/  |_|


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "VIPlogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://envs.sh/pYG.mp4",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://envs.sh/pYY.mp4",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://envs.sh/pC3.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://envs.sh/pFS.mp4",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://envs.sh/pC0.mp4",
)

COUPLE_IMG_URL = getenv(
    "COUPLE_IMG_URL",
    "https://envs.sh/Abq.mp4",
)
    
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://graph.org/vTelegraphBot-10-21-11",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://graph.org/file/4d42f55061642f9a8603e-d77d37f92dc5d4a4f7.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://graph.org/file/71e0135e5e048aabb33b2-53a3c917628ee25346.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://graph.org/file/0ad0744744eb72696f7be-3f096131603c528e0f.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://graph.org/file/c7ea15528fc9816e05141-0a5598ac2585dae36f.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://graph.org/vTelegraphBot-10-19-20",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://envs.sh/pC4.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://envs.sh/pCl.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )


if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )


if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "https://envs.sh/pYY.mp4":
        if not re.match("(?:http|https)://", PING_mp4_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://envs.sh/0-U.jpg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://envs.sh/pFS.mp4":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://envs.sh/pC0.mp4":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://graph.org/vTelegraphBot-10-21-11":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://graph.org/file/71e0135e5e048aabb33b2-53a3c917628ee25346.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://graph.org/file/0ad0744744eb72696f7be-3f096131603c528e0f.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://envs.sh/0-U.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://graph.org/file/99c2b5a447a51cea148b1.mp4":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
)
