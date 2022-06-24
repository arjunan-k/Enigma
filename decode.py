# Reversing the encoding morse alphabet is easy.
# We can use dictionary comprehension.
# inverse = dict((a, b) for (b, a) in Morse_Alphabets.items())
# print(inverse)

Morse_Alphabets_Reverse = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '/': ' '
}

# This class is responsible for decoding our message.
class Decode:

    @staticmethod
    def decode(msg):
        decoded_msg = ""
        try:
            text_input = msg.split(" ")
            for word in text_input:
                decoded_msg += Morse_Alphabets_Reverse[word]
            print(f'Your encoded message is: {decoded_msg.lower()}')
        except KeyError:
            print("Please insert correct message")