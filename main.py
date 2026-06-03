from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api import AstrBotConfig
import random
import astrbot.api.message_components as Comp

@register("掷骰子", "EndlessAttackUnderMoon", "随机发出一张骰子的图片。", "1.1")
class PluginRollDice(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""

    @filter.command("掷骰子")
    async def helloworld(self, event: AstrMessageEvent):
        """这是一个AstrBot的 掷骰子 指令，可随机发出一张骰子的图片。""" # handler描述
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)

        index = random.randint(0, 5)
        path = ""
        if index == 0:
            path = self.config['image1Url']
        elif index == 1:
            path = self.config['image2Url']
        elif index == 2:
            path = self.config['image3Url']
        elif index == 3:
            path = self.config['image4Url']
        elif index == 4:
            path = self.config['image5Url']
        else:
            path = self.config['image6Url']

        chain = [
            Comp.Image.fromURL(path)
        ]

        yield event.chain_result(chain) # 发送一条富媒体消息
