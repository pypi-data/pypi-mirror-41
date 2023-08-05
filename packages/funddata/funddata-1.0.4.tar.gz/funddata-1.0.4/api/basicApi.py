#coding=gbk
__author__ = 'pw.guo'
import pymysql
import pandas as pd
class BasicApi:


    def __init__(self,userName):
        self.__userName=userName
        try:
              self._db = pymysql.connect(host='rm-uf677c3h27sq7cnaojo.mysql.rds.aliyuncs.com',port=3306, user=self.__userName, passwd = "r1@funddata" , db='funddata', charset='utf8')
              self._cursor =  self._db.cursor()
        except pymysql.err.OperationalError:
            print("�������Ӵ���")

    def __del__(self):
        self._cursor.close()
        self._db.close()


    def stock_basic(self,exchange="", list_status="",ts_codes=(), fields=""):
        try:

            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from stockBasic where 1=1"
            if  list_status.strip():
                 sql=sql +" and list_status='"+list_status+"'"
            if  exchange.strip():
                 sql=sql +" and exchange='"+exchange+"'"
            if  len(ts_codes):
                 sql=sql +" and ts_code in "+str(ts_codes)
            print(sql)
            df = pd.read_sql( sql,self._db)
            return df;
        except pymysql.err.OperationalError:
            print("�������Ӵ���")
        except Exception as err:
            print(err )
        return []

    def daily(self,ts_codes=(),start_date="", end_date="", fields=""):
        try:
            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from daily where 1=1"
            if  start_date.strip():
                 sql=sql +" and trade_date>='"+start_date+"'"
            if  end_date.strip():
                 sql=sql +" and trade_date<='"+end_date+"'"
            if  len(ts_codes):
                 sql=sql +" and ts_code in "+str(ts_codes)
            print(sql)
            df = pd.read_sql( sql,self._db)
            return df;
        except pymysql.err.OperationalError:
            print("�������Ӵ���")
        except Exception as err:
            print(err )
        return []

    def tradeCal(self,start_date="", end_date=""):
        try:
            sql="select *"+ \
                " from trade_cal where 1=1"
            if  start_date.strip():
                 sql=sql +" and cal_date>='"+start_date+"'"
            if  end_date.strip():
                 sql=sql +" and cal_date<='"+end_date+"'"

            print(sql)
            df = pd.read_sql( sql,self._db)
            return df;
        except pymysql.err.OperationalError:
            print("�������Ӵ���")
        except Exception as err:
            print(err )
        return []

    def weekly(self,ts_codes=(),start_date="", end_date="", fields=""):
        try:
            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from weekly where 1=1"
            if  start_date.strip():
                 sql=sql +" and trade_date>='"+start_date+"'"
            if  end_date.strip():
                 sql=sql +" and trade_date<='"+end_date+"'"
            if  len(ts_codes):
                 sql=sql +" and ts_code in "+str(ts_codes)

            print(sql)
            df = pd.read_sql( sql,self._db)
            return df;
        except pymysql.err.OperationalError:
            print("�������Ӵ���")
        except Exception as err:
            print(err )
        return []

    def monthly(self,ts_codes=(),start_date="", end_date="", fields=""):
        try:
            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from monthly where 1=1"
            if  start_date.strip():
                 sql=sql +" and trade_date>='"+start_date+"'"
            if  end_date.strip():
                 sql=sql +" and trade_date<='"+end_date+"'"
            if  len(ts_codes):
                 sql=sql +" and ts_code in "+str(ts_codes)

            print(sql)
            df = pd.read_sql( sql,self._db)
            return df;
        except pymysql.err.OperationalError:
            print("�������Ӵ���")
        except Exception as err:
            print(err )
        return []

    def dailyBasic(self,ts_codes=(),start_date="", end_date="", fields=""):
        try:
            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from daily_basic where 1=1"
            if  start_date.strip():
                 sql=sql +" and trade_date>='"+start_date+"'"
            if  end_date.strip():
                 sql=sql +" and trade_date<='"+end_date+"'"
            if  len(ts_codes):
                 sql=sql +" and ts_code in "+str(ts_codes)
            print(sql)
            df = pd.read_sql( sql,self._db)
            return df;
        except pymysql.err.OperationalError:
            print("�������Ӵ���")
        except Exception as err:
            print(err )
        return []