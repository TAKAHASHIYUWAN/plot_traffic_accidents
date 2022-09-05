import folium 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from csv2database import Honhyo, WINDOW_DESKTOP_PATH

def main():
    dbMatching()
    map_plot()    


#databaseとつなぎ、経度、緯度を取り出す。

def dbMatching():

    engine = sa.create_engine("sqlite:///honhyo.sqlite3")
    Session = sessionmaker(engine)
    session = Session()
    map_query = session.query(Honhyo.latitude,Honhyo.longitude)

    return map_query




#databaseのから、特定の条件で、経度緯度を取り出す

def map_plot():

    db_query = dbMatching()
    q = db_query.filter(
    #ここに条件を入力する
       Honhyo.year == 2021,
       Honhyo.prefecture == "神奈川",
       Honhyo.incident == "死亡",
       Honhyo.road_surface == "舗装-乾燥",
     )

    """
    上の条件は、SQLで記述すると以下のように表される。

    SELECT 
        latitude ,
        longitude
    FROM
        honhyo
    WHERE
        prefecture == "北海道",
        year ==2021 ,
        incident == "死亡",
        road_surface == "舗装-乾燥"
    ;
    """


     
    #マップの中心をq[1]にして、マップを設定
    map = folium.Map(location=q[1])
    #プロットする。
    for row in q:
        folium.Marker(location=row,icon=folium.Icon(color='red')).add_to(map)
    #マップをセーブ
    map.save(WINDOW_DESKTOP_PATH + f"accident_plot.html")

if __name__ == "__main__":
    main()