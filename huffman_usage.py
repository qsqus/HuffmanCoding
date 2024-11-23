from huffman_coding import HuffmanCoding


if __name__ == '__main__':
    file_path = 'example_text.txt'

    # Load text from the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    huffman_coding = HuffmanCoding()

    # Create the Huffman Dictionary, print it out
    huffman_dict = huffman_coding.create_huffman_dict(file_content)
    print('Huffman dictionary:')
    for i in huffman_dict.items():
        print(f'\'{i[0]}\': {i[1]}')

    # Encode the text, write the encoded result to a file
    encoded_text = huffman_coding.encode(file_content, huffman_dict)
    with open('example_encoded.txt', 'w') as file:
        file.write(encoded_text)

    # Decode the encoded text, write the decoded result to a file
    decoded_text = huffman_coding.decode(encoded_text, huffman_dict)
    with open('example_decoded.txt', 'w') as file:
        file.write(decoded_text)

    # Compare the decoded text with the original text
    print(f'\nIs decoded text the same as original: {file_content == decoded_text}')
