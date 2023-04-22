# ! ./usr/bin/bash

def cipher(k, m, method)->None:
    res: str = ""
    mod: int = 0
    LETTERS = [ chr(i) for i in range(32, 126)]  # A -- Z
    if method.lower() == 'e':
        """ Vignère Encryption by my approach  """
        """
            1[Bjr, je vois tous par mes yeux!]
            2[ABCDEFGHIJKLMNOPQRSTUVWXYZABCDE]
            res = [nb([1]+[2])].append([nb(k)+nb([2]+ (jxi) )])
            
            
            => 'len(res)' == 'len[1] + len([1])*len(k)'
        """
        for i in range(len(m)):
            mod %= len(LETTERS)            
            for j in range(len(k)):
                res += chr(ord(k[j]) + ord(LETTERS[mod])+j*i)            
            res += chr(ord(m[i]) + ord(LETTERS[mod])) # concatenation 
        with open(f'crypting.odt', 'a', encoding='utf-8') as f:
            f.writelines(f'{k}\n{res}')
        f.close()
    else:
        """ Decryption  """
        for i in range(0, len(m)):
            mod %= len(LETTERS)            
            j = i % (len(k)+1)
            if j==len(k):
                res += chr(ord(m[i]) - ord(LETTERS[mod]))
            else:
                continue
        name_file:str = input('Rename your file: ')
        with open(f'{name_file}.odt', 'a', encoding='utf-8') as f:
            f.writelines(f'\n{k}\n{res}')
        f.close()
    return 0


while True:
    method = str(input('What do u want, (e)ncrypt or (d)ecrypt? (q)uit\n >'))
    if method.lower()=='e':
        key:str = input('Key: ')
        message:str = input('The message: ')
        cipher(key, message, method)
        break
    elif method.lower() == 'd':
        key:str = input('Key: ')
        message:str = input('The message: ')
        cipher(key, message, method)
        break
    elif method.lower() == 'q':
        break
        print('Bye bye!')
