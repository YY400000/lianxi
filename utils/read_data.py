from utils.get_filepath import get_yaml_path
from utils.get_filepath import get_hero_path
import yaml

path1 = get_yaml_path()
path2 = get_hero_path()


def read_yaml():
    with open(path1, 'r', encoding='gbk') as f:
        data = yaml.safe_load(f)
        return data


def read_hero():
    with open(path2, 'r', encoding='gbk') as f:
        data = yaml.safe_load(f)
        return data



# with open('D:\Program Files (x86)\PyCharm\lianxi\config_data\hero.yaml') as file1:
#     data = yaml.safe_load(file1)
#     print(data)
#     print('hero1', data['hero1'])
#     print('hero11', data['hero11'])
#     print('hero2', data['hero2'])
#     print('heros_name1', data['heros_name1'])
#     print('heros_name2', data['heros_name2'])
#     print('hero_name_list1', data['hero_name_list1'])
#     print('hero_name_list2', data['hero_name_list2'])
#     print('hero_name_list3', data['hero_name_list3'])
#     print('hero3', data['hero3'])
#     print('heros_name3', data['heros_name3'])


if __name__ == '__main__':
    print(read_hero())
