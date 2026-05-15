import os.path

import pandas as pd
import yaml
from tools.path_utils import DataPath
from configparser import ConfigParser
class LoadData:
    @staticmethod
    def loader_from_excel(file_name, sheet_name='Sheet1'):
        source_data_file = DataPath.get_source_data_file(file_name)
        # print(source_data_file)
        df = pd.read_excel(source_data_file, sheet_name=sheet_name).fillna('')
        return df.to_dict(orient='records')
    @staticmethod
    def loader_from_yaml(file_name):
        source_data_file = DataPath.get_source_data_file(file_name)
        with open(source_data_file,'r',encoding='utf-8') as fp:
            data = yaml.safe_load(fp)
            return data
    @staticmethod
    def loader_from_ini(sectionname, varname):
        config_file = DataPath.get_pytest_config_file()
        config = ConfigParser()
        config.read(config_file, encoding='utf-8')
        return config[sectionname][varname]