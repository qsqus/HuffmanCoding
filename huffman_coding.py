from tree_node import TreeNode


class HuffmanCoding:
    def create_probability_dict(self, text: str) -> dict:
        self.check_for_invalid_data(text)

        prob_dict = {}

        # Count occurrences of each character
        for i in text:
            if i not in prob_dict:
                prob_dict[i] = 0
            prob_dict[i] += 1

        # Calculate the probability of each character
        for key in prob_dict:
            prob_dict[key] /= len(text)

        return prob_dict

    def create_huffman_tree(self, text: str) -> TreeNode:
        self.check_for_invalid_data(text)

        prob_dict = self.create_probability_dict(text)
        # Convert probability dictionary to list
        tree_node_list = [TreeNode(key, val) for key, val in prob_dict.items()]

        # Sort list in descending order by value
        tree_node_list.sort(key=lambda x: -x.value)

        while len(tree_node_list) > 1:
            tn1 = tree_node_list.pop()  # Smaller
            tn2 = tree_node_list.pop()  # Greater
            tn_new = TreeNode(tn1.label + tn2.label, tn1.value + tn2.value, tn1, tn2)

            # Insert new TreeNode in correct place
            i = 0
            while i < len(tree_node_list) and tn_new.value < tree_node_list[i].value:
                i += 1

            tree_node_list.insert(i, tn_new)

        return tree_node_list[0]

    def create_huffman_dict(self, text: str) -> dict:
        self.check_for_invalid_data(text)

        huffman_tree = self.create_huffman_tree(text)

        huffman_dict = {}
        stack = [(huffman_tree, '')]

        # Text consists of only one character type
        if all(child is None for child in huffman_tree):
            huffman_dict[huffman_tree.label] = '1'
            return huffman_dict

        while len(stack) > 0:
            node, code = stack.pop()

            if all(child is None for child in node):
                huffman_dict[node.label] = code
            else:
                for i in range(len(node)):
                    if node[i] is not None:
                        stack.append((node[i], code + str(i)))

        return huffman_dict

    def encode(self, text: str, huffman_dict: dict) -> str:
        self.check_for_invalid_data(text)

        encoded_text = ''.join(huffman_dict[i] for i in text)
        return encoded_text

    def decode(self, text: str, huffman_dict: dict) -> str:
        self.check_for_invalid_data(text)

        swapped_huffman_dict = {val: key for key, val in huffman_dict.items()}

        decoded_text = ''
        code = ''

        for i in text:
            code += i
            if code in swapped_huffman_dict:
                decoded_text += swapped_huffman_dict[code]
                code = ''

        return decoded_text

    def check_for_invalid_data(self, text: str) -> None:
        if len(text) == 0:
            raise ValueError('Text must be longer than 0!')
