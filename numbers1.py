import string
# a programme to generate password
from random import *

characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(8, 16)))
print(password)

characters = string.ascii_letters + string.digits
password = "".join(choice(characters) for y in range(randint(8, 16)))
print(password)
