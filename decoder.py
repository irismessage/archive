# Different decoder modules
import base64
import base128

# Functions for decoding (in a list)
encodings = [lambda x: base64.b64decode(x),
             lambda x: base64.b16decode(x),
             lambda x: base64.b32decode(x),
             lambda x: base64.a85decode(x),
             lambda x: base64.b85decode(x),
             lambda x: base128.decode(x),
             ]

# Run forever
while True:
    # Get the ciphertext
    encoded = input()

    # Run it agaisnt all the different encodings and print
    for f in encodings:
        decoded = f(encoded)
        print(decoded)
