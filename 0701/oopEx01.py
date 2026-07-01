class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(f"Channel : {self.channel}")
        print(f"Volume : {self.volume}")
        print(f"On : {self.on}")
    def set_channel(self, channel):
        self.channel = channel
    def set_volume(self):
        return self.channel

tv1 = Television(1, 10, True)
print(tv1)
tv1.show()
tv2 = Television(2, 20, False)
tv2.show()