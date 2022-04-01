import unittest
from app import calculate_payment
from datetime import datetime


class TestCalculatePayment(unittest.TestCase):
    def test_payment(self):
        # Different plans without discounts
        self.assertAlmostEqual(calculate_payment([{'_id': 1, 'plan_id': 1, 'descuentos': [], 'status': 'active',
                                                   'validity': datetime(2022, 3, 1)}]), 100)
        self.assertAlmostEqual(calculate_payment([{'_id': 1, 'plan_id': 2, 'descuentos': [], 'status': 'active',
                                                   'validity': datetime(2022, 3, 1)}]), 150)
        self.assertAlmostEqual(calculate_payment([{'_id': 1, 'plan_id': 3, 'descuentos': [], 'status': 'active',
                                                   'validity': datetime(2022, 3, 1)}]), 200)
        self.assertAlmostEqual(calculate_payment([{'_id': 1, 'plan_id': 4, 'descuentos': [], 'status': 'active',
                                                   'validity': datetime(2022, 3, 1)}]), 300)
        # Some discounts, total sum lesser than 1

        self.assertAlmostEqual((calculate_payment(
            [{'_id': 1, 'plan_id': 1, 'descuentos': [{'id': 1, 'aplicaciones': 2}], 'status': 'active',
              'validity': datetime(2022, 3, 1)}])), 90)
        self.assertAlmostEqual((calculate_payment(
            [{'_id': 1, 'plan_id': 1, 'descuentos': [{'id': 1, 'aplicaciones': 2}, {'id': 5, 'aplicaciones': 2}],
              'status': 'active',
              'validity': datetime(2022, 3, 1)}])), 40)
        self.assertAlmostEqual((calculate_payment(
            [{'_id': 1, 'plan_id': 1,
              'descuentos': [{'id': 1, 'aplicaciones': 2}, {'id': 2, 'aplicaciones': 2}, {'id': 3, 'aplicaciones': 2}],
              'status': 'active',
              'validity': datetime(2022, 3, 1)}])), 40)

        # Discounts which sum is greater than 1

        self.assertAlmostEqual((calculate_payment(
                [{'_id': 1, 'plan_id': 1,
                  'descuentos': [{'id': 5, 'aplicaciones': 2}, {'id': 2, 'aplicaciones': 2},
                                 {'id': 3, 'aplicaciones': 2}],
                  'status': 'active',
                  'validity': datetime(2022, 3, 1)}])), 0)
        self.assertAlmostEqual((calculate_payment(
            [{'_id': 1, 'plan_id': 1,
              'descuentos': [{'id': 5, 'aplicaciones': 2}, {'id': 2, 'aplicaciones': 2},
                             {'id': 4, 'aplicaciones': 2}],
              'status': 'active',
              'validity': datetime(2022, 3, 1)}])), 0)
