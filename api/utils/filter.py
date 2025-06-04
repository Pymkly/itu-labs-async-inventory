import os


def remove_void(_remove_dirs):
    _path_ref = './labels/train'
    dirs = os.listdir(_path_ref)

    result = []
    for dir in dirs:
        with open(os.path.join(_path_ref, dir), 'r') as f:
            line = f.readline()
            if line == '\n' or line == '':
                result.append(dir[:-4])
    _dicts = {}
    for _dir in _remove_dirs:
        dirs = os.listdir(_dir)
        _dicts[_dir] = {}
        for _d in dirs:
            _dicts[_dir][_d[:-4]] = _d
    for dir in result:
        for _remove_dir in _remove_dirs:
            _path = _dicts[_remove_dir][dir]
            _path = os.path.join(_remove_dir, _path)
            os.remove(_path)
    return result
