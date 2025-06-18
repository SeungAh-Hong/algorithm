def solution(phone_book):
    answer = True
    hash_map = {}
    phone_book = sorted(phone_book, key=len, reverse=True)
    # print(phone_book)
    
    for p in phone_book:
        hash_map[p] = True
    
    for number in phone_book:
        prefix = ""
        for char in number[:-1]:
            prefix += char
            if prefix in hash_map:
                return False
    
    return answer