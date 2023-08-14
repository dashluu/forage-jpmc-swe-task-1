import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            expected = (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']),
                        (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)
            self.assertEquals(getDataPoint(quote), expected)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            expected = (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']),
                        (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)
            self.assertEquals(getDataPoint(quote), expected)

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_priceBZero(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        quote_ABC = quotes[0]
        quote_DEF = quotes[1]
        price_ABC = (float(quote_ABC['top_bid']['price']) + float(quote_ABC['top_ask']['price'])) / 2
        price_DEF = (float(quote_DEF['top_bid']['price']) + float(quote_DEF['top_ask']['price'])) / 2
        self.assertEquals(getRatio(price_ABC, price_DEF), None)

    def test_getRatio_zeroPrices(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        quote_ABC = quotes[0]
        quote_DEF = quotes[1]
        price_ABC = (float(quote_ABC['top_bid']['price']) + float(quote_ABC['top_ask']['price'])) / 2
        price_DEF = (float(quote_DEF['top_bid']['price']) + float(quote_DEF['top_ask']['price'])) / 2
        self.assertEquals(getRatio(price_ABC, price_DEF), None)

    def test_getRatio_ratioOver1(self):
        quotes = [
            {'top_ask': {'price': 130.714, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 125.52, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 120.45, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 115.14, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        quote_ABC = quotes[0]
        quote_DEF = quotes[1]
        price_ABC = (float(quote_ABC['top_bid']['price']) + float(quote_ABC['top_ask']['price'])) / 2
        price_DEF = (float(quote_DEF['top_bid']['price']) + float(quote_DEF['top_ask']['price'])) / 2
        expected = price_ABC / price_DEF
        self.assertEquals(getRatio(price_ABC, price_DEF), expected)


if __name__ == '__main__':
    unittest.main()
