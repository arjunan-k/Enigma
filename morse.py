# Importing the classes and calling the methods.
from encode import Encode
from decode import Decode
encrypt = Encode()
decrypt = Decode()

# Looping the program until we turn it off.
is_on = True
while is_on:
    user_need = input("Do you want to encode or decode the message: ").lower()
    if user_need == "encode":
        encode_msg = input("Type the message you want to encode: \n")
        encrypt.encode(encode_msg)
    elif user_need == "decode":
        decode_msg = input("Type the message you want to decode: \n")
        decrypt.decode(decode_msg)
    elif user_need == "off":
        is_on = False
    else:
        print("Enter a valid cipher direction for the message.")