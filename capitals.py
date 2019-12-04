def count_letters(string):
    count_upper = 0
    count_lower = 0

    for i in string:
        if (i.islower()):
            count_lower = count_lower + 1 
        elif (i.isupper()):
            count_upper = count_upper + 1

    return (count_upper, count_lower)

def main():
    print('Please write your text')
    input_text = input()

    results = count_letters(input_text)
    
    print('There are {} uppercase letters'.format(results[0]))
    print('There are {} lowercase letters'.format(results[1]))

if __name__ == "__main__":
    main()