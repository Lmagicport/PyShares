'''
in this moudle you can get shares’s data from internet
'''

# get shares list from money.163

import numpy as np
import pandas as pd
from pandas import concat


class SpySharesData:

    def __init__(self, f=0):
        'f means which market you need to get data'
        self.flag = f
    
    # 数据来自上海交易所和深圳交易所官方网站，如果没有找到需要的股票代码，可以自行对代码进行补充，补充后的文件欢迎上传至项目中
    def spydatalist(self, shares_code) -> pd.DataFrame:
        # flag=1 表示股票数据来自上海股票交易所中的A股列表，本方法只返回股票的代码和名称
        if self.flag == 1:

            try:
                # 读取需要的列的信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sh_a.csv'))
                if type(data_csv) == pd.DataFrame:
                    self.CompanyName = data_csv.iloc[:, 1]
                    self.CompanyCode = data_csv.iloc[:, 2]
                    self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName], axis=1)
                    return self.CompanyInfo

            except Exception as e:
                print(e)

        elif self.flag == 2:
            # flag =2 表示股票数据来自上海股票交易所中的B股列表
            try:
                # 读取所需信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sh_b.csv'))
                if type(data_csv) == pd.DataFrame:
                    self.CompanyName = data_csv.iloc[:,1]
                    self.CompanyCode = data_csv.iloc[:, 2]
                    self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName],axis = 1)
                    return self.CompanyInfo
            except Exception as e:
                print(e)
        
        elif self.flag == 3:
            # flag = 3 表示 股票数据来自深圳股票交易所中的A股列表
            try:
                # 读取所需信息
                data_csv = pd.DataFrame(pd.read_csv(r'shares_data\sz_a', converters={u'A股简称':str,u'A股代码':str}))
                self.CompanyName = data_csv.iloc[:,3]
                self.CompanyCode = data_csv.iloc[:,4]
                self.CompanyInfo = pd.concat([self.CompanyCode, self.CompanyName], axis=1)
                return self.CompanyInfo
            except Exception as e:
                print(e)
        
        elif self.flag == 4:
            # flag = 4 表示股票数据来自于深圳交易所中的B股列表

                    
