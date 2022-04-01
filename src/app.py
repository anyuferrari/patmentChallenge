from pymongo import MongoClient
from datetime import datetime
from dateutil.relativedelta import relativedelta

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db = client['club']
socios = db['socios']
planes = db['planes']
descuentos = db['descuentos']
pagos = db['pagos']


def get_payment_due():
    query = {'validity': {"$lt": datetime.now()}}
    return socios.find(query)


def calculate_payment(socios_list):
    payment = []
    for socio in socios_list:
        current_payment = {}
        applied_discounts = []
        plan = socio['plan_id']
        price = planes.find_one(plan)['precio']
        total_discount = 0
        discounts = socio['descuentos']
        for discount in discounts:
            if discount['aplicaciones'] > 0:
                applied_discounts.append(discount['id'])
                discount_proportion = descuentos.find_one({'_id': discount['id']})['monto']
                total_discount += discount_proportion
                discount['aplicaciones'] -= 1
        socios.update_one({'_id': socio['_id']}, {'$set': {'descuentos': discounts}})
        if total_discount >= 1:
            total_discount = 1
        final_price = price * (1 - total_discount)
        date = socio['validity']
        current_payment['periodo cobrado'] = date.strftime('%m/%y')
        current_payment['monto'] = final_price
        current_payment['socio_id'] = socio['_id']
        current_payment['descuentos aplicados'] = applied_discounts

        new_date = date + relativedelta(months=1)
        socios.update_one({'_id': socio['_id']}, {'$set': {'validity': new_date}})
        payment.append(current_payment)
    pagos.insert_many(payment)
    return final_price


a = calculate_payment([{'_id': 1, 'plan_id': 1, 'descuentos': [], 'status': 'active',
     'validity': datetime(2022, 3, 1)}])
print(a)