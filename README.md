# Huffman Coding

This repository contains my implementation of Huffman coding in Python, which is used for lossless data compression.

## Key Files

- `huffman_coding.py`: Implementation of the `HuffmanCoding` class.
- `tree_node.py`: Implementation of the `TreeNode` class used for constructing the Huffman Tree.
- `huffman_usage.py`: Contains an example usage of the Huffman Coding implementation.
- `example_text.txt`: A sample text file used to demonstrate Huffman Coding.
- `test_huffman_coding.py`: Unit tests for the Huffman Coding class.

## Huffman Coding Class

The class `HuffmanCoding` provides methods to perform the following operations:

- **`create_huffman_dict(text)`**: Generates a dictionary of Huffman codes for the given text.
- **`encode(text, huffman_dict)`**: Encodes the given text into its Huffman binary representation using given Huffman Dictionary.
- **`decode(text, huffman_dict)`**: Decodes the given binary Huffman-encoded text back to its original form using given Huffman Dictionary.

The class also contains other methods meant for internal use, which are responsible for constructing the Huffman tree and generating the probability dictionary.
