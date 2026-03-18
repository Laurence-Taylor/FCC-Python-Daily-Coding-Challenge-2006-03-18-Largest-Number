def largest_number(s):
    # Create a set of separators
    separator_set = set(',!?:;')
    # create variable of larg_number and initialize
    larg_number = float('-inf')
    # init prev_pos
    prev_pos = 0
    # iterate over each caracter of the string
    for i in range(len(s)):
        # if found a new number
        if s[i] in separator_set:
            # if number is the largest then swap larg_number variable
            if float(s[prev_pos:i]) > larg_number: larg_number = float(s[prev_pos:i])
            # update prev_pos
            prev_pos = i + 1
        # if reached the end of string
        if i == len(s)-1:
            # compare last number and if number is the largest then swap larg_number variable
            if float(s[prev_pos:len(s)]) > larg_number: larg_number = float(s[prev_pos:len(s)])
    # return largest number
    return larg_number

if __name__ == '__main__':
    print(largest_number("1,2"))
    print('-----')
    print(largest_number("4;15:60,26?52!0"))
    print('-----')
    print(largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"))
    print('-----')
    print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))