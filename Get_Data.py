'''
in this moudle you can get shares’s data from internet
'''

# get shares list from money.163

from requests_html import HTMLSession


class SpySharesData:

    def __init__(self,f):
        'f means which market you need to get data'
        self.flag = f
    
    # spy share's list from ifeng.com
    def spydatalist(self):
        if self.flag == 1:
            session = HTMLSession()
            r = session.get('')
