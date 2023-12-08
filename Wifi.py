import nmap
from getmac import get_mac_address
import asyncio
from telegram import Bot

My_IP = '192.168.1.1'
Known_IP = []
Token = '6950245916:AAHx-3ZGwoXZmBOWDlQZw93lhC7HQhZ21Kg'
Chat = '-4079773705'

class WifiScanner:
    def __init__(self, id:str):
        self.id = id
        self.connected = set()

    def scan(self):
        network = f"{self.id}/24"
        nm = nmap.PortScanner()
        while(True):
            nm.scan(hosts=network, arguments='-sn')
            host_list = nm.all_hosts()
            for i in host_list:
                mac = get_mac_address(ip=i)
                print(mac)
                if mac and mac not in self.connected and mac not in Known_IP:
                    print("New Device :")
                    self.new_device(mac)
                    self.connected.add(mac)

    async def message(self, bot, Chat, message):
        await bot.send_message(chat_id= Chat, text=message)

    def new_device(self, mac):
        bot = Bot(token=Token)
        asyncio.run(self.message(bot, Chat, f"New Device MAC : {mac}"))

if __name__ == "__main__":
    Scanner = WifiScanner(My_IP)
    Scanner.scan()