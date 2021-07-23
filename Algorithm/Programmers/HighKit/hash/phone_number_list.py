def solution(phone_book):
    dic = {}
    for phone_number in phone_book:
        dic[hash(phone_number)] = True
        
    for phone_number in phone_book:
        part_of_number = ""
        for number in phone_number:
            part_of_number += number
            if hash(part_of_number) in dic and part_of_number != phone_number:
                return False
    return True

print(solution(["12", "123", "1235", "567", "88"]))
