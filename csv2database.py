import csv 
import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

WINDOW_DESKTOP_PATH = "/mnt/c/Users/yuwan/Desktop/"

def main():
    csv2database(os.path.join(WINDOW_DESKTOP_PATH,'honhyo.csv'))


"""
SQLAlchemyを用いて、データベースのテーブルを作成する。
"""
conn = sa.create_engine('sqlite:///honhyo.sqlite3',)
Base = declarative_base()
class Honhyo(Base):
    __tablename__ = "Honhyo"

    id = sa.Column("id",sa.Integer, primary_key = True)
    prefecture = sa.Column("prefecture",sa.String )
    incident = sa.Column('incident', sa.Integer )
    dead = sa.Column('dead', sa.Integer  )
    injured = sa.Column('injured', sa.Integer  )
    year = sa.Column('year', sa.Integer  )
    month = sa.Column('month', sa.Integer  )
    day = sa.Column('day', sa.Integer  )
    hours = sa.Column('hours', sa.Integer  )
    minutes = sa.Column('minutes', sa.Integer  )
    latitude = sa.Column('latitude', sa.Float  )
    longitude = sa.Column('longitude', sa.Float  )
    age_partyA = sa.Column("age_partyA",sa.String )
    age_partyB = sa.Column("age_partyB",sa.String )
    day_and_night = sa.Column("day_and_night",sa.String )
    weather = sa.Column("weather",sa.String )
    topograpy = sa.Column("topograpy",sa.String )
    road_surface = sa.Column("road_surface",sa.String )
    road_shape = sa.Column("road_shape",sa.String )
    traffic_light = sa.Column("traffic_light",sa.String )
    
    def __init__(self,prefecture,incident,dead,injured,year,month,day,hours,minutes,latitude,longitude,
                age_partyA,age_partyB,day_and_night,weather,topograpy,road_surface
                ,road_shape,traffic_light):
        self.prefecture = prefecture
        self.incident = incident
        self.dead = dead
        self.injured = injured
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.latitude = latitude
        self.longitude = longitude
        self.age_partyA = age_partyA
        self.age_partyB = age_partyB
        self.day_and_night = day_and_night
        self.weather = weather
        self.topograpy = topograpy
        self.road_surface = road_surface
        self.road_shape = road_shape
        self.traffic_light =traffic_light
        
    def __repr__(self):  
            return "<Honhyo({},{},{},{},{},{},{},{},{},{})>".format(self.prefecture,self.incident,
                                        self.dead,self.injured,self.year,self.month,self.day,
                                        self.hours,self.minutes,self.latitude,self.longitude)

Base.metadata.create_all(conn)

"""
windowsのデスクトップにあるCSVファイルをデータベースに変換する。

DBにデータを格納するためには、

first_instance = Honhyo(prefecture1,incident1,......)
second_instance = Honhyo(prefecture2,incident2,......)
third_instance = Honhyo(prefecture3,incident3,......)
として、

session.add(インスタンス)か
session.add_all([インスタンス1、インスタンス2、インスタンス3.....])
のように入力する必要がある。

以下の処理ではinstance_listを定義し、
instance_list = [firsr_instance, second_instance,........]
session.add_all(instance_list)
"""


def csv2database(filepath):
    with open(filepath, "r",encoding="Shift-JIS") as csvfile :
        s =  csv.reader(csvfile)
        instance_list = []
        for row in s :
            honhyo = Honhyo(row[0],row[1],int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7]),
                            int(row[8]),float(row[9]),float(row[10]),row[11],row[12],row[13],row[14],row[15],
                            row[16],row[17],row[18])
            instance_list.append(honhyo)
    Session = sessionmaker(bind = conn)
    session = Session()
    session.add_all(instance_list)
    session.commit()

if __name__ == "__main__":
    main()


