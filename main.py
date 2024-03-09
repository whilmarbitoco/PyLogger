import socket, time, asyncio
import api

class Main:
    def __init__(self) -> None:
        self.bot = api.Bot()

    def checkhost(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True 
        except OSError:
            return False  
    
    def run(self):
        while True:
            if self.checkhost():
                asyncio.run(self.bot.msg("Internet connection is available."))
                break
            else:
                print("waiting")
                time.sleep(2)

if __name__ == "__main__":
    main = Main()
    main.run()
