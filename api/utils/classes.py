import os


def get_classes(_path='./labels/train'):
    dirs = os.listdir(_path)
    result = []
    temp = {}
    for dir in dirs:
        with open(os.path.join(_path, dir), 'r') as f:
            line = f.readline()
            classes = line.split(' ')[0]
            if classes == '':
                print(dir)
                print(line)
            try :
                _t = temp[classes]
            except Exception as e:
                temp[classes] = 0
                result.append(classes)
    return result