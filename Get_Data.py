'''
in this moudle you can get shares’s data from internet
'''

# get shares list from money.163

import numpy as np
import pandas as pd


class SpySharesData:

    def __init__(self, f=0):
        'f means which market you need to get data'
        self.flag = f
        self.SharesFilePath = None
    
    def set_shares_marcket(self, flag):
        # 更换股票市场
        self.flag = flag

    # 数据来自上海交易所和深圳交易所官方网站，如果没有找到需要的股票代码，可以自行对代码进行补充，补充后的文件欢迎上传至项目中
    def spy_data_list(self) -> pd.DataFrame:
        # flag=1 表示股票数据来自上海股票交易所中的A股列表，本方法只返回股票的代码和名称
        print(self.flag)
        if self.flag == 1:

            try:
                # 读取需要的列的信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sh_a.csv'))
                if type(data_csv) == pd.DataFrame:
                    self.CompanyName = data_csv.iloc[:, 1]
                    self.CompanyCode = data_csv.iloc[:, 2]
                    self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName], axis=1)
                    print(self.CompanyInfo)
                    return self.CompanyInfo

            except Exception as e:
                raise e

        elif self.flag == 2:
            # flag =2 表示股票数据来自上海股票交易所中的B股列表
            try:
                # 读取所需信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sh_b.csv'))
                if type(data_csv) == pd.DataFrame:
                    self.CompanyName = data_csv.iloc[:, 1]
                    self.CompanyCode = data_csv.iloc[:, 2]
                    self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName], axis=1)
                    return self.CompanyInfo
            except Exception as e:
                raise e
        
        elif self.flag == 3:
            # flag = 3 表示 股票数据来自深圳股票交易所中的A股列表
            try:
                # 读取所需信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sz_a.csv', converters={u'A股简称': str, u'A股代码': str}))
                self.CompanyName = data_csv.iloc[:, 3]
                self.CompanyCode = data_csv.iloc[:, 4]
                self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName], axis=1)
                return self.CompanyInfo
            except Exception as e:
                raise e
        
        elif self.flag == 4:
            # flag = 4 表示股票数据来自于深圳交易所中的B股列表
            try:
                # 读取所需信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sz_b.csv', converters={u'B股代码': str, u'B股简称': str}))
                self.CompanyName = data_csv.iloc[:, 7]
                self.CompanyCode = data_csv.iloc[:, 6]
                self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName], axis=1)
                return self.CompanyInfo
            except Exception as e:
                raise e
       
        else:
            raise 'get wrong market info'

    # get shares code
    def get_shares_code(self, SharesName='Null', ShaeresMacket=0):
        if self.SharesName == 'Null':
            return '0000000'
        else:
            if ShaeresMacket == 1:
                try:
                    self.CompanyInfo = self.get_shares_code(1)
                    self.FindResult = self.CompanyInfo[self.CompanyInfo['公司简称'] == SharesName]
                    if self.FindResult.empty is True:
                        return 'there is no code by your index please rechack your share name and retry or use other function'
                    else:
                        return self.FindResult
                except Exception as e:
                    raise e
            
            elif ShaeresMacket == 2:
                try:
                    self.CompanyInfo = self.get_shares_code(2)
                    print(self.CompanyInfo)
                    self.FindResult = self.CompanyInfo[self.CompanyInfo['公司简称' == SharesName]]
                    if self.FindResult.empty is True:
                        return 'there is no code by your index please rechack your share name and retry or use other function'
                    else:
                        return self.FindResult
                except Exception as e:
                    raise e
            
            elif ShaeresMacket == 3:
                try:
                    self.CompanyInfo = self.get_shares_code(3)
                    self.FindResult = self.CompanyInfo[self.CompanyInfo['A股简称' == SharesName]]
                    if self.FindResult.empty is True:
                        return 'there is no code by your index please rechack your share name and retry or use other function'
                    else:
                        return self.FindResult
                except Exception as e:
                    raise e
            
            elif ShaeresMacket == 4:
                try:
                    self.CompanyInfo = self.get_shares_code(4)
                    self.FindResult = self.CompanyInfo[self.CompanyInfo['B股简称' == SharesName]]
                    if self.FindResult.empty is True:
                        return 'there is no code by your index please rechack your share name and retry or use other function'
                    else:
                        return self.FindResult
                
                except Exception as e:
                    raise e

    # spy data from money.163.com


if __name__ == '__main__':
    test = SpySharesData(2)
    result = test.get_shares_code('黄山旅游', 2)
    print(result)