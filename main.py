my_dict = {}
def print_menu():
    print("무엇을 할까요?")
    print("1. 단어 보기")
    print("2. 단어 추가")
    print("3. 단어 삭제")
    print("4. 프로그램 종료")

while True:
    print_menu()
    rst = input()

    if rst == '1': # 단어 보기
        if not my_dict:
            print("단어가 없습니다.")
            continue

        for k, v in my_dict.items():
            print(f'{k} = {v}')
    elif rst == '2': # 단어 추가
        add_key = input("추가할 단어를 입력하세요")
        add_value = input("단어의 뜻을 입력하세요")
        my_dict[add_key] = add_value
    elif rst == '3': # 단어 삭제    
        del_key = input("삭제할 단어를 입력하세요")
        try:
            del my_dict[del_key]
        except:
            print(f"{del_key}의 단어는 없습니다.") 
    elif rst == '4': # 종료
        break
    else:
        print("잘못 입력 하였습니다. 다시 입력해 주세요")
