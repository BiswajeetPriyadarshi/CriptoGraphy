def criptography():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # auto generating the vaules of strings and last to first
    
    values = keys[-1] + keys[0:-1]

    # creating two dictionaries
    Dict1 = dict(zip(keys, values))
    Dict2 = dict(zip(values, keys))

    # user input
    message = input("Enter your secret message: ")
    mode = input("Enter Mode : Encode(E) OR Decode(D): ")

    #encode and decode
    if mode.upper() == 'E':
        newMessage = ''.join([Dict1[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([Dict2[letter]
                              for letter in message.lower()])
    else:
        print("Please enter Right Mode !  ")

    return newMessage.capitalize()


print(criptography())
