import pcqq
from utils import *
from time import sleep

print("本软件仅作为工具软件使用，禁止商用或以此谋利")
bot = pcqq.QQBot()


class FileSave(pcqq.Plugin):
    def match(self) -> bool:
        return self.on_reg_match(r"\[PQ:image,url=(.*)\]")

    def handle(self):
        url = self.state["regex_matched"][0]
        if self.msgBody.FromQQ not in userRecord:
            self.send_msg("请先按照格式‘myself 收集信息 ’设置您的信息备注")
            sleep(0.5)
            self.send_msg("例如 'myself 木昕20201910000'")
        else:
            name = userRecord[self.msgBody.FromQQ]
            SaveImg(url, name)


class CommandHandler(pcqq.Plugin):
    def match(self):
        return self.on_reg_match(r"myself (.*)")

    def handle(self):
        userRecord[self.msgBody.FromQQ] = self.state["regex_matched"][0]
        instance.Save()


instance = UserRecord()
userRecord = instance.Dic
master = userRecord["master"]
bot.RunBot()
