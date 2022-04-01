from pymongo import MongoClient
from datetime import datetime

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db = client['club']
socios = db['socios']
planes = db['planes']
descuentos = db['descuentos']
pagos = db['pagos']

socios.drop({})
planes.drop({})
descuentos.drop({})
pagos.drop({})

socios_data = [
    {'_id': 1, 'plan_id': 1, 'discounts': [{'id': 1, 'aplicaciones': 2}], 'status': 'active',
     'vigencia': datetime(2022, 3, 1)},
    {'_id': 2, 'plan_id': 2, 'discounts': [{'id': 1, 'aplicaciones': 1}, {'id': 2, 'aplicaciones': 4}],
     'status': 'inactive',
     'vigencia': datetime(2022, 5, 1)},
    {'_id': 3, 'plan_id': 3, 'discounts': [], 'status': 'active',
     'vigencia': datetime(2022, 8, 1)},
    {'_id': 4, 'plan_id': 4,
     'discounts': [{'id': 1, 'aplicaciones': 5}, {'id': 2, 'aplicaciones': 2}, {'id': 4, 'aplicaciones': 1}],
     'status': 'inactive',
     'vigencia': datetime(2022, 2, 1)},
    {'_id': 5, 'plan_id': 2,
     'discounts': [{'id': 2, 'aplicaciones': 5}, {'id': 4, 'aplicaciones': 1}, {'id': 5, 'aplicaciones': 3}],
     'status': 'active',
     'vigencia': datetime(2023, 1, 1)},
]

planes_data = [{'_id': 1, 'precio': 100},
               {'_id': 2, 'precio': 150},
               {'_id': 3, 'precio': 200},
               {'_id': 4, 'precio': 300},
               ]
descuentos_data = [{"_id": 1, "monto": 0.1},
                   {"_id": 2, "monto": 0.2},
                   {"_id": 3, "monto": 0.3},
                   {"_id": 4, "monto": 0.4},
                   {"_id": 5, "monto": 0.5},
                   ]

socios.insert_many(socios_data)
planes.insert_many(planes_data)
descuentos.insert_many(descuentos_data)
