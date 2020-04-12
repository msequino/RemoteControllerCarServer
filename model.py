

class MessagePayload:
	def __init__(self, action, timestamp):
                self.action = action
                self.timestamp = timestamp

	@staticmethod
	def builder(message):
		parts = message.split(";")
		timestamp = -1
		if parts[0].lower() == "throttle":
			self.action = Throttle(parts[1], parts[2])
			timestamp = parts[3]
		elif parts[0].lower() == "reverse":
			self.action = Reverse(parts[1], parts[2])
			timestamp = parts[3]
		elif parts[0].lower() == "steer":
			self.action = Steer(parts[1], parts[2])
			timestamp = parts[3]
		elif parts[0].lower() == "slowdown":
			self.action = SlowDown()
			timestamp = parts[1]
			
		self.timestamp = timestamp

	def execute():
		print("executing " + self.action + ", ts " + self.timestamp)
		self.action.execute()
		return true

class Throttle:
	type = "Throttle"
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def execute():
		print("executing throttle command")

class SlowDown:
        type = "SlowDown"
	def execute():
		print("executing slowdown command")

class Reverse:
        type = "Reverse"
        def __init__(self, x, y):
                self.x = x
                self.y = y

	def execute():
		print("executing reverse command")

class Steer:
        type = "Steer"
        def __init__(self, x, y):
                self.x = x
                self.y = y

	def execute():
		print("executing steer command")

