import heapq
import sys

class HeapNode:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		return self.freq < other.freq

	def __eq__(self, other):
		if (other == None):
			return False
		if (not isinstance(other, HeapNode)):
			return False
		return self.freq == other.freq

class HuffmanCoding:
	def __init__(self):
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

	# functions for compression:

	def make_frequency_dict(self, text):
		frequency = {}
		if not text:
			raise TypeError("The text is not valid")
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency

	def make_heap(self, frequency):
		for key in frequency:
			node = HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)


	def make_codes_helper(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")


	def make_codes(self):
		# root stores pointer to root of huffman tree
		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)


	def get_encoded_text(self, text):
		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]
		return encoded_text


	def pad_encoded_text(self, encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


	def get_byte_array(self, padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b


	def compress(self,text):
		frequency = self.make_frequency_dict(text)
		self.make_heap(frequency)
		self.merge_nodes()
		self.make_codes()

		encoded_text = self.get_encoded_text(text)
		padded_encoded_text = self.pad_encoded_text(encoded_text)

		b = self.get_byte_array(padded_encoded_text)



		# print(padded_encoded_text)
		return padded_encoded_text


	""" functions for decompression: """

	def remove_padding(self, padded_encoded_text):
		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:]
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text

	def decode_text(self, encoded_text):
		current_code = ""
		decoded_text = ""

		for bit in encoded_text:
			current_code += bit
			if(current_code in self.reverse_mapping):
				character = self.reverse_mapping[current_code]
				decoded_text += character
				current_code = ""

		return decoded_text


	def decompress(self, text):
		encoded_text = self.remove_padding(text)

		decompressed_text = self.decode_text(encoded_text)



		return decompressed_text

def display(a_great_sentence, bitstring, decoded_data):
	print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print ("The content of the data is: {}\n".format(a_great_sentence))

	print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(bitstring, base=2))))
	print ("The content of the encoded data is: {}\n".format(bitstring))

	print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
	print ("The content of the encoded data is: {}\n".format(decoded_data))


a_great_sentence = "The word is bird"
word = HuffmanCoding()
bitstring = word.compress(a_great_sentence)
decoded_data = word.decompress(bitstring)
display(a_great_sentence,bitstring,decoded_data)

case_2 = "AAAAAAAA"
huffman_2 = HuffmanCoding()
bitstring_2 = word.compress(case_2)
decoded_data_2 = word.decompress(bitstring_2)
display(case_2,bitstring_2,decoded_data_2)

case_3 =""
huffman_3 = HuffmanCoding()
bitstring_3 = word.compress(case_3)
decoded_data_3 = word.decompress(bitstring_3)
display(case_3,bitstring_3,decoded_data_3)
