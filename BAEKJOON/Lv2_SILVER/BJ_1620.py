book, test = map(int, input().split())
book_dict = {}
for i in range(book):
    p_number = i+1
    p_name = input()
    book_dict[p_name] = f'{p_number}'
    book_dict[f'{p_number}'] = p_name
for _ in range(test):
    print(book_dict[input()])

    