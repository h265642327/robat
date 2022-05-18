#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


# Custom your logger
#
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)


nonebot.load_builtin_plugins("echo")
nonebot.load_plugin('nonebot_plugin_gocqhttp')  # 管理插件
nonebot.load_plugin('nonebot_plugin_remake')  # 重生
# nonebot.load_plugin("nonebot_plugin_heweather")天气一号
nonebot.load_plugin('nonebot_plugin_weather_lite')  # 天气二号
nonebot.load_plugin('nonebot_plugin_simplemusic')  # 点歌
# nonebot.load_plugin("nonebot_plugin_heisi")#黑丝
nonebot.load_plugin("nonebot_plugin_setu")  # 瑟瑟
nonebot.load_plugin("nonebot_plugin_answersbook")  # 答案之书
# nonebot.load_plugin("nonebot_plugin_read_60s")#每日60s    3.9新特性搞得我真难受，只改了一个list的使用
# nonebot.load_plugin("nonebot_plugin_autohelp")#菜单
nonebot.load_plugin("nonebot_plugin_pixivrank_search")#p站排行榜

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
# nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
#
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
