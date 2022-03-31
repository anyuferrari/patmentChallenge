from pymongo import MongoClient
import datetime

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db = client['club']
socios = db['socios']
planes = db['planes']
descuentos = db['descuentos']

socios_data = [
    {'_id': 1, 'plan_id': 1, 'descuentos': [1], 'status': 'active',
     'validity': datetime.datetime(2022, 3, 1).strftime("%m/%y")},
    {'_id': 2, 'plan_id': 2, 'descuentos': [1, 2], 'status': 'inactive',
     'validity': datetime.datetime(2022, 5, 1).strftime("%m/%y")},
    {'_id': 3, 'plan_id': 3, 'descuentos': [1, 3], 'status': 'active',
     'validity': datetime.datetime(2022, 8, 1).strftime("%m/%y")},
    {'_id': 4, 'plan_id': 4, 'descuentos': [1, 2, 4], 'status': 'inactive',
     'validity': datetime.datetime(2022, 2, 1).strftime("%m/%y")},
    {'_id': 5, 'plan_id': 2, 'descuentos': [1, 2, 5], 'status': 'active',
     'validity': datetime.datetime(2023, 1, 1).strftime("%m/%y")},
]

planes_data = [{'_id': 1, 'precio': 100},
               {'_id': 2, 'precio': 150},
               {'_id': 3, 'precio': 200},
               {'_id': 4, 'precio': 300},
               ]
descuentos_data = [{"_id": 1, "monto": 0.1, "aplicaciones": 4},
                   {"_id": 2, "monto": 0.2, "aplicaciones": 0},
                   {"_id": 3, "monto": 0.3, "aplicaciones": 3},
                   {"_id": 4, "monto": 0.4, "aplicaciones": 2},
                   {"_id": 5, "monto": 0.5 , "aplicaciones": 1},

]

if socios.count_documents({}) == 0:
    socios.insert_many(socios_data)
if planes.count_documents({}) == 0:
    planes.insert_many(planes_data)
if descuentos.count_documents({}) == 0:
    descuentos.insert_many(descuentos_data)