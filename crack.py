# Implement crack in python

import sys
import crypt

FIRST_ALPHA = "A"
LAST_ALPHA = "z"

# Check there are two the command arguments
if not len(sys.argv) == 2:
    print("Usage: ./crack hash")

# Assign argc[1] to a string k
k = sys.argv[1]


#Initialize "salt", which is from first two characters of k
salt = k[0] + k[1]

# Loop through potential passwords by lenth, which can be made of 1 to 5 characters
for i in range(1, 6, 1):
    pw = FIRST_ALPHA * i

    # Loop for the first character of the password
    for j1 in range(ord(FIRST_ALPHA), ord(LAST_ALPHA) + 1, 1):
        pw = chr(j1)
        y = crypt.crypt(pw, salt)

        if y == k:
            print(pw)

        # Compare if the try equals the given hashed password
        if i > 1:
            for j2 in range(ord(FIRST_ALPHA), ord(LAST_ALPHA) + 1, 1):
                pw = chr(j1) + chr(j2)
                y = crypt.crypt(pw, salt)

                if y == k:
                    print(pw)

                # Loop for the second character of the password
                if i > 2:
                    for j3 in range(ord(FIRST_ALPHA), ord(LAST_ALPHA) + 1, 1):
                        pw = chr(j1) + chr(j2) + chr(j3)
                        y = crypt.crypt(pw, salt)

                        if y == k:
                            print(pw)

                        # Loop for the third character of the password
                        if i > 3:
                            for j4 in range(ord(FIRST_ALPHA), ord(LAST_ALPHA) + 1, 1):
                                pw = chr(j1) + chr(j2) + chr(j3) + chr(j4)
                                y = crypt.crypt(pw, salt)

                                if y == k:
                                    print(pw)

                                # Loop for thr forth character of the password
                                if i > 4:
                                    for j5 in range(ord(FIRST_ALPHA), ord(LAST_ALPHA) + 1, 1):
                                        pw = chr(j1) + chr(j2) + chr(j3) + chr(j4) + chr(j5)
                                        y = crypt.crypt(pw, salt)

                                        if y == k:
                                            print(pw)
