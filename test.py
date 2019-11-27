
with open(FILE_OUTPUT_NAME, 'asdf') as f_out:
        for c in text:
            ascii = ord(c)
            if ascii == PIPE_ASCII:
                f_out.write('I')
            elif ascii in ACCEPTED_ASCII_LIST:
                f_out.write[c]
            else:
                f_out.write(' ')
