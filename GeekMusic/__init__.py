#
# Copyright (C) 2021-2022 by GeekMusik@Github, < https://github.com/GeekMusik >.
#
# This file is part of < https://github.com/GeekMusik/GeekMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/GeekMusik/GeekMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from GeekMusic.core.bot import GeekBot
from GeekMusic.core.dir import dirr
from GeekMusic.core.git import git
from GeekMusic.core.userbot import Userbot
from GeekMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = GeekBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
