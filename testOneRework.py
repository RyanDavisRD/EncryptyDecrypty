from cryptography.fernet import Fernet


key1 = b'2-PeU4_a6BFdaHBdsf85Euxw4SOT4TSs4gfEQC80SIw='

cipher = Fernet(key1)

e_file = input("Type Name of File or Drag and Drop File. Type Close to close! Remove \" if needed. ")

with open(e_file, 'rb') as ef:
    data = ef.read()

while e_file != 'Close':
    en_de = input("Do you want to encrypt or decrypt? (E/D): ")
    if en_de == "E":
        edata = cipher.encrypt(data)

        with open(e_file + ".encrypted", 'wb') as ef:
            ef.write(edata)

    elif en_de == "D":
        ddata = cipher.decrypt(data)
        with open(e_file + ".decrypted", 'wb') as df:
            df.write(ddata)


    else:
        print("Enter Valid Input! (E/D)")

    if en_de == 'E':
        input("Your file has been encrypted! Press Enter to continue! ")
    elif en_de == 'D':
        input("Your file has been decrypted! Press Enter to continue! ")

    e_file = input("Type Name of File or Drag and Drop File. Type Close to close! Remove \" if needed. ")






