string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0.8.0'
splits = [x.split(',') for x in string.split('\n')]
complete_splits = []


for strings in splits:
    new_strings = []
    for string in strings:
        if string[0] =='"' and string[-1]=='"':
            new_strings.append(string[1:-1])
        elif '.' in string:
            string.split('.')
            for s in string:
                if s != '.' and s != '0':
                    new_strings.append(float(s))
        else:
            new_strings.append(int(string))
    complete_splits.append(new_strings)

print(complete_splits)