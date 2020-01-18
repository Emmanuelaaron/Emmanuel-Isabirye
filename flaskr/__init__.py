from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
farmers = [
{"district": "Kalangala", "number": 944}, 
{"district": "Buikwe", "number": 925},
 {"district": "Buvuma", "number": 1087}, 
 {"district": "Namayingo", "number": 181}, 
 {"district": "Katakwi", "number": 651}, 
 {"district": "Nakapiripirit", "number": 1136}, 
 {"district": "Kamwenge", "number": 754}, 
 {"district": "Mbarara", "number": 575},
 {"district": "Kotido", "number": 1920},
 {"district": "Agago", "number": 1492}, 
 {"district": "Bulambuli", "number": 1309}, 
 {"district": "Kween", "number": 1775}, 
 {"district": "Amudat", "number": 1822}, 
 {"district": "Kaberamaido", "number": 174}, 
 {"district": "Amolatar", "number": 1188}, 
 {"district": "Kaliro", "number": 1780}, 
 {"district": "Namutumba", "number": 355}, 
 {"district": "Kitgum", "number": 1754}, 
 {"district": "Lamwo", "number": 1535}, 
 {"district": "Pader", "number": 129}, 
 {"district": "Sironko", "number": 701}, 
 {"district": "Mbale", "number": 1882},
 {"district": "Bugiri", "number": 566}, 
 {"district": "Busia", "number": 405}, 
 {"district": "Butaleja", "number": 1355}, 
 {"district": "Mayuge", "number": 30}, 
 {"district": "Manafwa", "number": 220}, 
 {"district": "Tororo", "number": 1418}, 
 {"district": "Masaka", "number": 1540}, 
 {"district": "Kasese", "number": 1093}, 
 {"district": "Ntungamo", "number": 398}, 
 {"district": "Bushenyi", "number": 38}, 
 {"district": "Rukungiri", "number": 100},
 {"district": "Ibanda", "number": 243}, 
 {"district": "Mbarara", "number": 1766},
 {"district": "Kabale", "number": 1573}, 
 {"district": "Kanungu", "number": 1798}, 
 {"district": "Nebbi", "number": 1448}, 
 {"district": "Zombo", "number": 1936}, 
 {"district": "Ngora", "number": 287}, 
 {"district": "Bukedea", "number": 194}, 
 {"district": "Budaka", "number": 1335}, 
 {"district": "Kibuku", "number": 1059}, 
 {"district": "Pallisa", "number": 316}, 
 {"district": "Serere", "number": 1184}, 
 {"district": "Kalungu", "number": 602}, 
 {"district": "Gomba", "number": 594}, 
 {"district": "Amuru", "number": 1209},
 {"district": "Amuria", "number": 360}, 
 {"district": "Otuke", "number": 180},
 {"district": "Oyam", "number": 1906}, 
 {"district": "Kiryandongo", "number": 123},
 {"district": "Kibale", "number": 713}, 
 {"district": "Ntoroko", "number": 1562},
 {"district": "Kyegegwa", "number": 1065},
 {"district": "Napak", "number": 1526}, 
 {"district": "Moroto", "number": 9},
 {"district": "Bukwa", "number": 1384}, 
 {"district": "Bukomansimbi", "number": 1370},
 {"district": "Lwengo", "number": 1471}, 
 {"district": "Lyantonde", "number": 585},
 {"district": "Butambala", "number": 25}, 
 {"district": "Rubirizi", "number": 1181}, 
 {"district": "Sheema", "number": 625}, 
 {"district": "Mitooma", "number": 1845}, 
 {"district": "Buhweju", "number": 984}, 
 {"district": "Bududa", "number": 1259}, 
 {"district": "Jinja", "number": 256}, 
 {"district": "Kayunga", "number": 1331},
 {"district": "Iganga", "number": 126},
 {"district": "Alebtong", "number": 916}, 
 {"district": "Soroti", "number": 268},
 {"district": "Buyende", "number": 1664}, 
 {"district": "Kumi", "number": 1432},
 {"district": "Mpigi", "number": 156},
 {"district": "Adjumani", "number": 1921},
 {"district": "Yumbe", "number": 1595}, 
 {"district": "Kampala", "number": 43}, 
 {"district": "Mukono", "number": 1367},
 {"district": "Wakiso", "number": 1344}, 
 {"district": "Sembabule", "number": 1821},
 {"district": "Mityana", "number": 1178},
 {"district": "Nakaseke", "number": 545}, 
 {"district": "Dokolo", "number": 855}, 
 {"district": "Lira", "number": 1801}, 
 {"district": "Gulu", "number": 1338}, 
 {"district": "Nwoya", "number": 799}, 
 {"district": "Masindi", "number": 1753}, 
 {"district": "Apac", "number": 839},
 {"district": "Buliisa", "number": 1179},
 {"district": "Hoima", "number": 1134}, 
 {"district": "Kabarole", "number": 1479},
 {"district": "Kapchorwa", "number": 1915}, 
 {"district": "Kaabong", "number": 223}, 
 {"district": "Abim", "number": 779}, 
 {"district": "Rakai", "number": 186}, 
 {"district": "Isingiro", "number": 1079},
 {"district": "Kisoro", "number": 148}, 
 {"district": "Luuka", "number": 1974},
 {"district": "Kamuli", "number": 1954}, 
 {"district": "Arua", "number": 1129},
 {"district": "Koboko", "number": 960},
 {"district": "Moyo", "number": 9}, 
 {"district": "Luweero", "number": 698}, 
 {"district": "Mubende", "number": 1755}, 
 {"district": "Nakasongola", "number": 338},
 {"district": "Bundibugyo", "number": 1038}, 
 {"district": "Kyankwanzi", "number": 945},
 {"district": "Kole", "number": 1270}, 
 {"district": "Maracha", "number": 612}, 
 {"district": "Kiboga", "number": 501}, 
 {"district": "Kyenjojo", "number": 1855}
 ]

@app.route("/")
def index():
    return jsonify(farmers)