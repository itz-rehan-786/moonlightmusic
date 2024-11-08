import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8125428412:AAE5kFCQO8JA9A1Wgrb3F4Wi3Y1_FWRNJzU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLoBuyYipvzAsfDDCexH6pbcWOnLoI3MrI3uTG0iRiEuVEoIELyvxP7oS4jFpjFW-NnMvr0caSB42saK675yFCA3pHNEAUerHrTfJkslTKxfvCMwuGmJAOpOofrShMnZfnypxLa_d97BG1LEeeYiuUUnVNcHVh-JGw5wjflvtlalhqWjbXl6XYugx97dh-spjX3wLhb2epZM2Suu0SwV43tzR8Ap_dbJdYxwTqW6dB1tnRUhybIoiphJpsQb3lfNv8fr9GaFjPrektEmIIosjvKywV6sVi7GWuZuhKxKf817impEffiLX61-ZG5f3UOXv-rMl356NXfLbOaAxGLtqehMOpk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "moonlight_musicxbot")
    SUPPORT = os.environ.get("SUPPORT", "land_of_hunters") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "sungupdate") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7355509359")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
