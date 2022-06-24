from music import Music
music = Music()

Morse_Alphabets = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", " ": "/"
}

# This class is responsible for encoding our message.
class Encode:

    @staticmethod
    def encode(msg):
        encoded_msg = ""
        try:
            sound_list = []
            for letter in msg.upper():
                encoded_msg += Morse_Alphabets[letter] + " "
                for each in Morse_Alphabets[letter]:
                    sound_list.append(each)
                sound_list.append(" ")
            print(f'Your encoded message is: {encoded_msg}\n')
            print(f"{sound_list}\n")
            for each in sound_list:
                if each == ".":
                    music.dot()
                if each == "/":
                    music.slash()
                if each == "-":
                    music.bar()
                if each == " ":
                    music.space()

        except KeyError:
            print("Please insert correct message")