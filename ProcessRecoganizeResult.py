#!/usr/bin/python
# coding: utf-8
# python version: Python2.7.5

import re
import os


def FormateXml(xmlPath, writeFile):
    # 列出目标目录中的全部文件
    for dirPath, dirName, files in os.walk(xmlPath):
        for fileName in files:
            if fileName.endswith('xml'):
                # 拼接xml文件绝对路径
                xmlName = dirPath +'/'+ fileName
                print('xml name: %s' % xmlName)
                with open(xmlName, 'rb') as fd:
                    lines = fd.readlines()
                    for line in lines:
                        # 正则匹配识别结果中的wav的Uri
                        matchObj = re.search(r'Uri="(.*)\/(.*?)\.wav"', line, re.I)
                        if matchObj is not None:
                            wavName = matchObj.group().split('"')[1]
                            print('    Uri: %s\n\r' % wavName)
                            txtName = './'+ matchObj.group(2) +'.txt'
                        # 匹配识别结果的正则
                        matchObj  = re.findall(r'<Text>(.*?)</Text>', line, re.I)
                        if len(matchObj) > 0:
                            # fw = open(txtName, 'w')
                            # fw.write(wavName +'\n')       # 把每个xml的处理结果写到对应的每个txt中
                            writeFile.write(wavName +'\n')    # 把每个xml的处理结果写到同一个txt中
                            for i in matchObj:
                                # 去除识别结果中的标点
                                # fw.write(i.replace(' ', '').replace('，', '').replace('。', '').replace('！', '').replace('？', ''))
                                writeFile.write(i.replace(' ', '').replace('，', '').replace('。', '').replace('！', '').replace('？', ''))

                                # 保留识别结果中的标点
                                # fw.write(i.replace(' ', ''))
                                writeFile.write(i.replace(' ', ''))
                            # fw.write('\n')
                            # fw.flush()
                            # fw.close()
                            writeFile.write('\n\n')




if __name__ == '__main__':
    fileAll = open('./all.txt', 'w')
    xmlFilePath = ['/pachira/data-source/speech/Sub/2018-02-11/file',
                   '/pachira/data-source/speech/Sub/2018-02-12/file',
                   '/pachira/data-source/speech/Sub/2018-02-13/file',
                   '/pachira/data-source/speech/Sub/2018-02-14/file',
                   # '/pachira/data-source/speech/Sub/2018-02-15/file',
                   # '/pachira/data-source/speech/Sub/2018-02-16/file'
                   ]
    for i in xmlFilePath:
        FormateXml(i, fileAll)

    fileAll.flush()
    fileAll.close()
