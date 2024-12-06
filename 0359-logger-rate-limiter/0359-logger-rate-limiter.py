class Logger:

    def __init__(self):
        self.message_storage={}
        #self.message_lock=""


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.message_storage and timestamp-self.message_storage[message]<10:
                return False
        else:
                self.message_storage[message]=timestamp
                return True
        # else:
        #     if self.message_lock!=message:
        #         return False
        #     else:
        #         if message_time<=timestamp<=message_time+10:
        #             return False
        #         else:
        #             self.message_lock=message
        #             return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)