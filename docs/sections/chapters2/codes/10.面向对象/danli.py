class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            # 可以在这里进行额外的初始化操作
        return cls._instance

    def __init__(self):
        # 初始化日志器，这里简化为一个空操作
        # 在现实应用中，这里可以打开一个文件或者初始化一个日志库
        self.log_messages = []

    def log(self, message):
        # 记录日志消息
        self.log_messages.append(message)
        print(f"Log: {message}")


# 创建Logger实例
logger1 = Logger()
logger2 = Logger()

# 检查两个实例是否相同
print(f"Logger1 is Logger2: {logger1 is logger2}")

# 使用第一个logger记录一条消息
logger1.log("This is a test message.")

# 使用第二个logger记录另一条消息
logger2.log("This is another test message.")

# 检查消息是否被记录在同一个logger实例中
print(f"Logged messages: {logger1.log_messages}")
