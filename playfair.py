xor = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
xor = set([i.upper() for i in xor])

w, h = 5, 5;
table = [['*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*']]


def playfair_encrypt(key, plaintext):
    k = set([i.upper() for i in key])
    k.discard('J')
    k.discard(' ')
    x = xor.difference(k)


    for row in range(5):
        for col in range(5):
            if len(k) is not 0:
               table[row][col] = k.pop()
            elif len(x) is not 0:
                table[row][col] = x.pop()

    plaintext = plaintext.upper()

    plaintext = [i for i in plaintext if i != " "]

    plaintext = ''.join(map(str,plaintext))



    n = len(plaintext)
    plain = plaintext
    for i in range(n):
        if plaintext[i] == plaintext[i-1]:
            plain = plaintext[:i] + 'X' + plaintext[i:]


    plaintext = plain

    if len(plaintext)%2 is not 0:
        plaintext = plaintext + 'X'

    print(plaintext)
    cipher = ""
    for i in range(0, len(plaintext) - 1, 2):
        a = ""
        b = ""
        p,q = plaintext[i:i+2]

        row1,col1 = find_letter(p)
        row2,col2 = find_letter(q)



        if row1 == row2 & col1 == col2:
            print("ERROR: letters to encode_pair must be distinct")
        elif row1 == row2:
            col1 = col1+1
            col2 = col2+1
            col1 = col1 % 5
            col2 = col2 % 5
            a = table[row1][col1]
            b = table[row2][col2]
        elif col1 == col2:
            row1 = row1+1
            row2 = row2+1
            row1 = row1 % 5
            row2 = row2 % 5
            a = table[row1][col1]
            b = table[row2][col2]
        else:
            a = table[row1][col2]
            b = table[row2][col1]
        cipher = cipher + a + b
    return(cipher)





def find_letter(letter): #to find index of letters
    for row in range(5):
        for col in range(5):
            if letter == table[row][col]:
                return (row,col)


def print_table():   #to print table content
    for row in range(5):
        for col in range(5):
            print(table[row][col],end="")
        print("")


if __name__ == "__main__":
    s = input("Enter the secret key: ")
    p = input("Enter the plaintext: ")
    print()
    print("Encrypted cipher: ",playfair_encrypt(s, p))
    print()

    print_table()
