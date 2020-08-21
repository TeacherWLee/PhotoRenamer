import os
# import sys
import time
import re
# import shutil
# import exifread
# import json
# import urllib.request

# 获取当前模块路径
path = os.getcwd()

# 支持的扩展名类型
extensions = ['.JPG', '.jpg', '.MOV', '.mov', '.mp4', '.MP4', '.PNG', '.png', 'GIF', 'gif']

# 遍历路径下的所有文件和文件夹
for root, dir, files in os.walk(path):
    for file in files:

        # 获取文件创建时间
        full_path = os.path.join(root, file)
        mtime = os.stat(full_path).st_mtime
        file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        pattern = '[-:]'
        file_modify_time = re.sub(pattern, '', file_modify_time)
        pattern = '[ ]'
        file_modify_time = re.sub(pattern, '_', file_modify_time)

        # 获取文件扩展名
        (filename, extension) = os.path.splitext(file)

        # 如果扩展名不在制定序列中，跳出循环
        if extension not in extensions:
                continue

        # 生成新文件名
        new_file = file_modify_time + extension
        new_path = root + '\\' + new_file

        # 判定文件是否存在
        i = 0
        while os.path.exists(new_path):
                new_file = '{0}({1}){2}'.format(file_modify_time, str(i), extension) 
                new_path = root + '\\' + new_file
                i += 1

        # 修改文件名
        os.rename(full_path, new_path)
        # shutil.move(full_path, new_path)

        print("{0} 修改为: {1}".format(full_path, new_path))

print('done')
