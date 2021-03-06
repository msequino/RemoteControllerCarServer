
from gpio import Gpio

class MessagePayload:
	def __init__(self, action, timestamp):
		self.action = action
		self.timestamp = timestamp

	@staticmethod
	def builder(message):
		parts = message.split(";")
		timestamp = -1
		action = None
		if parts[0].lower() == "throttle":
			action = Throttle(parts[1], parts[2])
			timestamp = parts[3]
		elif parts[0].lower() == "reverse":
			action = Reverse(parts[1], parts[2])
			timestamp = parts[3]
		elif parts[0].lower() == "steer":
			action = Steer(parts[1], parts[2])
			timestamp = parts[3]
		elif parts[0].lower() == "slowdown":
			action = SlowDown()
			timestamp = parts[1]
			
		return MessagePayload(action, timestamp)

	def execute(self):
		print("executing " + self.action.type + ", ts " + self.timestamp)
		self.action.execute()
		return True

class Throttle:
	type = "Throttle"
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def execute(self):
		print("executing throttle command")
		Gpio.throttle(self.x, self.y)

class SlowDown:
	type = "SlowDown"
	def execute(self):
		print("executing slowdown command")
		Gpio.slowdown()

class Reverse:
	type = "Reverse"
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def execute(self):
		print("executing reverse command")
		Gpio.reverse(self.x, self.y)

class Steer:
	type = "Steer"
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def execute(self):
		print("executing steer command")
		Gpio.steer(self.x, self.y)

