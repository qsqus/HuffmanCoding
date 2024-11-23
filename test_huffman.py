import unittest
from huffman import HuffmanCoding


class TestHuffman(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.huffman_coding = HuffmanCoding()

    def test_create_probability_dict(self):
        frequency_dict = self.huffman_coding.create_probability_dict('aabc')
        correct_dict = {
            'a': 0.5,
            'b': 0.25,
            'c': 0.25
        }
        self.assertDictEqual(frequency_dict, correct_dict)

        with self.assertRaises(ValueError):
            self.huffman_coding.create_probability_dict('')

        frequency_dict = self.huffman_coding.create_probability_dict('\n \t')
        correct_dict = {
            '\n': 1/3,
            ' ': 1/3,
            '\t': 1/3
        }
        self.assertDictEqual(frequency_dict, correct_dict)

        frequency_dict = self.huffman_coding.create_probability_dict('12345')
        correct_dict = {
            '1': 0.2,
            '2': 0.2,
            '3': 0.2,
            '4': 0.2,
            '5': 0.2
        }
        self.assertDictEqual(frequency_dict, correct_dict)

    def test_create_huffman_dict(self):
        huffman_dict = self.huffman_coding.create_huffman_dict('aaaabcc')
        correct_dict = {
            'a': '1',
            'b': '00',
            'c': '01'
        }
        self.assertDictEqual(huffman_dict, correct_dict)

        huffman_dict = self.huffman_coding.create_huffman_dict('nnn')
        correct_dict = {
            'n': '1'
        }
        self.assertDictEqual(huffman_dict, correct_dict)

        with self.assertRaises(ValueError):
            self.huffman_coding.create_huffman_dict('')

    def test_encode(self):
        text = 'aaacbb'
        huffman_dict = {'a': '1', 'b': '01', 'c': '00'}
        encoded = self.huffman_coding.encode(text, huffman_dict)
        self.assertEqual(encoded, '111000101')

        with self.assertRaises(ValueError):
            self.huffman_coding.encode('', huffman_dict)

        text = 'abc1'
        huffman_dict = {'a': '1', 'b': '01', 'c': '000', '1': '001'}
        encoded = self.huffman_coding.encode(text, huffman_dict)
        self.assertEqual(encoded, '101000001')

        text = '''f f\nf g'''
        huffman_dict = {'f': '1', ' ': '01', '\n': '000', 'g': '001'}
        encoded = self.huffman_coding.encode(text, huffman_dict)
        self.assertEqual(encoded, '1011000101001')

    def test_decode(self):
        text = 'abcascas ascasbcbagsd sdgsdg'
        huffman_dict = self.huffman_coding.create_huffman_dict(text)
        encoded = self.huffman_coding.encode(text, huffman_dict)
        decoded = self.huffman_coding.decode(encoded, huffman_dict)
        self.assertEqual(text, decoded)

        with self.assertRaises(ValueError):
            self.huffman_coding.decode('', huffman_dict)

        text = '1'
        huffman_dict = self.huffman_coding.create_huffman_dict(text)
        encoded = self.huffman_coding.encode(text, huffman_dict)
        decoded = self.huffman_coding.decode(encoded, huffman_dict)
        self.assertEqual(text, decoded)


if __name__ == '__main__':
    unittest.main()
