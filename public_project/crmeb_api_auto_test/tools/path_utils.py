import os
class DataPath:
    # 获取源文件目录
    @staticmethod
    def get_source_data_dir():
        source_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data','source_data')
        # print(source_data_dir)
        return source_data_dir
    # 获取源文件路径
    @staticmethod
    def get_source_data_file(file_name):
        source_data_file = os.path.join(DataPath.get_source_data_dir(), file_name)
        # print(source_data_file)
        return source_data_file
    @staticmethod
    def get_pytest_config_dir():
        config_file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
        return config_file_dir
    @staticmethod
    def get_pytest_config_file():
        config_file = os.path.join(DataPath.get_pytest_config_dir(), 'config.ini')
        return config_file

