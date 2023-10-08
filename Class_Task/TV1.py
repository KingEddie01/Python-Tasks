class Tv:

    def __init__(self):
        self.isOn = False
        self.volume_level = 0
        self.channel = 1

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        self.volume_level = volume_level

    def channel_up(self):
        if self.channel < 100:
            self.channel += 1

    def channel_down(self):
        if self.channel > 0:
            self.channel -= 1

    def volume_up(self):
        if self.volume_level < 70:
            self.volume_level += 1

    def volume_down(self):
        if self.volume_level > 0:
            self.volume_level -= 1
