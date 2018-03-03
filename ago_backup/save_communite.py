import pickle

#把node-communite的txt文件存储成一个字典保存下来
def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split('\t')
                _dict[key] = value
    except IOError as ioerr:
        print("文件 %s 不存在" % (filepath))
    return _dict


def save_dict_to_file(_dict, filepath):
    try:
        with open(filepath, 'w') as dict_file:
            for (key, value) in _dict.items():
                dict_file.write('%s %s\n' % (key, value))
    except IOError as ioerr:
        print("文件 %s 无法创建" % (filepath))


if __name__ == '__main__':
    _dict = load_dict_from_file('data/biological_tim/biological_tim_communities.txt')
    print (_dict)
    output = open('tmp/comumunites_1.pkl', 'wb')
    pickle.dump(_dict, output)
    output.close()

