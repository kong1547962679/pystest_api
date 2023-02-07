import os
import yaml
import pandas as pd
import json

# 写入，追加
def write_yaml(data):
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8',mode='a+') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

# 读取
def read_yaml():
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8',mode='r') as f:
        value = yaml.load(f,yaml.FullLoader)
        return value

# 清空
def clear_yaml():
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8',mode='w') as f:
        f.truncate()

# 读取测试用例
def read_yaml_testcase(yamlpath):
    with open(os.getcwd()+'/testcases'+yamlpath,encoding='utf-8',mode='r') as f:
        value = yaml.load(f,yaml.FullLoader)
        return value

# 获取所有testcases文件下的yaml文件
def yaml_path():
    fileList = []
    for root, subDirs, files in os.walk(os.getcwd() + '/testcases'):
        for fileName in files:
            if fileName.endswith('.yaml'):
                fileList.append(os.path.join(root, fileName).split('/testcases')[1])
    return fileList

# 使用pandas做csv数据驱动
def csv_data(csvpath):
    data = []
    for i in [i for i in pd.read_csv(os.getcwd() + csvpath).T.to_dict().values()]:
        for k, v in i.items():
            if type(v) is str and '{' in v:
                    i[k] = json.loads(v)
        data.append(i)
    return data