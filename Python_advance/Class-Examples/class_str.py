class history():
    def __init__(self, time, place):
        self.time = time
        self.place = place
    def __str__(self):
        return f"Time: {self.time}, Place: {self.place}" # 回傳字串
    
h = history("1900", "Taiwan")
print(h)

#FIXME 猜猜看下面這個會印出什麼
'''
class quiz():
    def __str__(self):
        return 500
print(q)
'''