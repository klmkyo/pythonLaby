class TV:
  def __init__(self, max_vol: int = 100, max_channels: int = 128, vol: int = 50, channel: int = 1, powered_on = False):
    self.max_vol = max_vol
    self.max_channels = max_channels
    
    # set volume and channel
    self.set_volume(vol)
    self.set_channel(channel)
    self.powered_on = powered_on
    
  def __str__(self) -> str:
    return f"TV(channel={self.channel}, vol={self.vol}, powered_on={self.powered_on})"
  
  def increase_volume(self):
    if not self.powered_on: return None
    if self.vol < self.max_vol:
      self.vol += 1
    return self.vol
  def decrease_volume(self):
    if not self.powered_on: return None
    if self.vol > 0:
      self.vol -= 1
    return self.vol
  def set_volume(self, vol):
    if not self.powered_on: return None
    if vol > self.max_vol:
      self.vol = self.max_vol
    elif vol < 0:
      self.vol = 0
    else:
      self.vol = vol
    return self.vol
  
  def increase_channel(self):
    if not self.powered_on: return None
    if self.channel + 1 > self.max_channels:
      self.channel = 1
    else:
      self.channel += 1
    return self.channel
  def decrease_channel(self):
    if not self.powered_on: return None
    if self.channel - 1 < 1:
      self.channel = self.max_channels
    else:
      self.channel -= 1
    return self.channel
  def set_channel(self, channel):
    if not self.powered_on: return None
    if channel > self.max_channels:
      self.channel = self.max_channels
    elif channel < 1:
      self.channel = 1
    else:
      self.channel = channel
    return self.channel
  # można użyć modulo
    
  def turn_on(self):
    if self.powered_on:
      return False
    else:
      self.powered_on = True
      return True
  def turn_off(self):
    if self.powered_on:
      self.powered_on = False
      return False
    else:
      return False
  def toggle_power(self):
    self.powered_on = not self.powered_on
    return self.powered_on
  
# Making the code above better, smarter, more effecient, more readable, more pythonic
class TVBetter:
  def __init__(self, max_vol: int = 100, max_channels: int = 128, vol: int = 50, channel: int = 1, powered_on = False):
    self.max_vol = max_vol
    self.max_channels = max_channels
    
    # set volume and channel
    self.set_volume(vol)
    self.set_channel(channel)
    self.powered_on = powered_on
    
  def __str__(self) -> str:
    return f"TV(channel={self.channel}, vol={self.vol}, powered_on={self.powered_on})"
  
  def increase_volume(self):
    if not self.powered_on: return None
    self.vol = min(self.vol + 1, self.max_vol)
    return self.vol
  def decrease_volume(self):
    if not self.powered_on: return None
    self.vol = max(self.vol - 1, 0)
    return self.vol
  def set_volume(self, vol):
    if not self.powered_on: return None
    self.vol = max(min(vol, self.max_vol), 0)
    return self.vol
  
  def increase_channel(self):
    if not self.powered_on: return None
    self.channel = self.channel % self.max_channels + 1
    return self.channel
  def decrease_channel(self):
    if not self.powered_on: return None
    self.channel = (self.channel - 2) % self.max_channels + 1
    return self.channel
  def set_channel(self, channel):
    if not self.powered_on: return None
    self.channel = min(max(channel, 1), self.max_channels)
    return self.channel
  # można użyć modulo
    
  def turn_on(self):
    if self.powered_on:
      return False
    else:
      self.powered_on = True
      return True
  def turn_off(self):
    if self.powered_on:
      self.powered_on = False
      return False
    else:
      return False
  def toggle_power(self):
    self.powered_on = not self.powered_on
    return self.powered_on