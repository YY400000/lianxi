import os


def get_reply_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),  'pythonlesson', 'reply.txt')
    return path


def get_yaml_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),  'config_data', 'data.yaml')
    return path


def get_hero_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),  'config_data', 'hero.yaml')
    return path

# print(get_reply_path())
# print(os.getcwd())
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pythonlesson', 'reply.txt'))
# print(r'D:\Program Files (x86)\PyCharm\lianxi\pythonlesson\reply.txt')
# a = r'D:\Program Files (x86)\PyCharm\lianxi\pythonlesson\reply.txt'
# print(a)


if __name__ == '__main__':
    print(get_yaml_path())
