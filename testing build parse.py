

exp = input("enter: ")
tokens = []
i = 0
while i < len(exp):
    cur_tok = ""
    if exp[i].isalpha() != True and exp[i].isalnum() != True:
        cur_tok += exp[i]
        tokens.append(cur_tok)
        cur_tok = ""
        i += 1
    else:
        while exp[i].isalpha() == True or exp[i].isalnum() == True:
            cur_tok += exp[i]
            i += 1
            # if exp[i].isalpha == True:  # if letter
            #     cur_tok += exp[i]  # add it to ""
            #     i += 1
            # if exp[i].isalnum() == True:
            #     cur_tok += exp[i]
            #     i += 1
    tokens.append(cur_tok)
    cur_tok = ""

for i in tokens:
    if i == ' ':
        tokens.remove(i)
    print(i, end='')