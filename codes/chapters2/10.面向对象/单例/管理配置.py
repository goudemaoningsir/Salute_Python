import json


class ConfigurationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(
                cls, *args, **kwargs
            )
            # 初始化配置
            cls._instance.config = {}
        return cls._instance

    def load_config(self, config_file):
        # 从文件中加载配置
        with open(config_file, "r") as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config

    def update_config(self, new_config):
        self.config.update(new_config)


# 使用示例
if __name__ == "__main__":
    # 获取配置管理器实例
    config_manager = ConfigurationManager()
    # 加载配置文件
    config_manager.load_config("config.json")
    # 获取配置
    config = config_manager.get_config()
    print(config)

    # 更新配置
    new_config = {"new_key": "new_value"}
    config_manager.update_config(new_config)
    updated_config = config_manager.get_config()
    print(updated_config)
