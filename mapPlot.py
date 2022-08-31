import folium 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from excel2database import WIN_DESKTOP_PATH, Honhyo

#databaseとつなぐ

engine = sa.create_engine("sqlite:///honhyo.db")
Session = sessionmaker(engine)
session = Session()

#databaseのから、特定の条件で、経度緯度を取り出す

"""
SELECT 
    latitude ,
    longitude
FROM
    honhyo
WHERE
    dead >= 1,
    prefecture == "北海道",
    year ==2021
;
"""
q = session.query(Honhyo.latitude,Honhyo.longitude).filter(Honhyo.prefecture == "北海道"
                                ,Honhyo.dead >= 1,Honhyo.year == 2021 )




#マップの中心をq[10]にして、マップを設定
map = folium.Map(location=q[10],zoom_start=18)
#プロットする。
for row in q:
    folium.Marker(location=row,icon=folium.Icon(color='red')).add_to(map)
#マップをセーブ
map.save(WIN_DESKTOP_PATH + f"accident_plot_{Honhyo.prefecture}.html")
