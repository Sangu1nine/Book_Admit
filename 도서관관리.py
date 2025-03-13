# 도서관 = {'분야':[[식별코드, 도서명, 저자, 대출여부],[],[]]}
# 디스플레이_대출
# 디스플레이_반납
# 디스플레이_검색

display = '''
┌==================================================┐
   1. 추가 2. 검색 3. 대출 4. 반납 5. 목록, 6.종료
└==================================================┘
메뉴 번호를 선택해주세요 >>> '''

# 빈 리스트 선언 (도서 목록)
books = [{"title":"군주론" , "author":"니콜로 마키아벨리" , "quantity":3 , "borrowed": 0},
         {"title":"총,균,쇠", "author":"재러드 다이아몬드", "quantity":4, "borrowed": 0},
         {"title":"아이로봇", "author": "아이작 아시모프", "quantity":3, "borrowed": 0},
         {"title":'거시경제학', "author": '그레고리 맨큐', "quantity":4, "borrowed": 1},
         {"title":'점프 투 파이썬', "author": '박응용', "quantity":9, "borrowed": 5},
         {"title":'깃허브 입문', "author": '고경희', "quantity":5, "borrowed": 0},
         {"title":'사피엔스', "author": '유발 노아 하라리', "quantity":2, "borrowed": 0},
         {"title":'나의 라임 오렌지 나무', "author": '조제 마우루 지 바스콘셀루스', "quantity":1, "borrowed": 0},
         {"title":'해리포터', "author": '제이케이롤링', "quantity":4, "borrowed": 0},
         {"title":'지킬 박사와 하이드', "author": '로버트 루이스 스티븐슨', "quantity":2, "borrowed": 0}]

while True:
    menu = input(display).strip()

    # 1. 도서 추가
    if menu == '1':
        title = input(" 책 제목: ").strip(" ,.:").lower()
        author = input(" 저자: ").strip(" ,.:").lower()
        quantity = int(input(" 수량을 숫자만 입력해주세요 : ").strip())
        if quantity.isnumeric():  # 숫자인지 확인
            break
        print("숫자만 입력해주세요!")  # 숫자가 아니면 다시 입력 요청
        found = False  # 우선적으로 책 검색
        for book in books: # 도서관에 있는 도서명과 
            if book["title"] == title:
                book["quantity"] += quantity
                print(f" '{title}'의 수량이 {quantity}권 추가되었습니다. (총 {book['quantity']}권)")
                found = True
                break
        if not found:
            books.append({"title": title, "author": author, "quantity": quantity, "borrowed": 0})
            print(f" 새로운 도서 '{title}'이(가) 추가되었습니다. ({quantity}권)")

    # 2. 도서 검색
    elif menu == '2':
        keyword = input(" 검색어 (제목 또는 저자): ").strip()
        results = [book for book in books if keyword in book["title"] or keyword in book["author"]]

        if results:
            print("검색 결과 (띄어쓰기 지켜주세요!!):")
            for book in results:
                available = book["quantity"] - book["borrowed"]
                print("┌--------------------------------┐")
                print(f" 제목: {book['title']}")
                print(f" 저자: {book['author']}")
                print(f" 남은 수량: {available}")
                print("└--------------------------------┘")
        else:
            print(" 검색 결과가 없습니다.")

    # 3. 도서 대출
    elif menu == '3':
        
        if books:

            print("# 대출 가능한 도서 목록 #")
            print("┌----------------------------------------------------┐")
            for book in books:
                available = book["quantity"] - book["borrowed"]
                print(f" * 제목: {book['title']}, 저자: {book['author']}, 남은 수량: {available}")
            print("└----------------------------------------------------┘")
        else:
            print(" 도서관에 책이 없습니다.")

        title = input(" 대출할 책 제목 : ").strip()

        for book in books:
            if book["title"] == title:
                available = book["quantity"] - book["borrowed"]
                if available > 0:
                    book["borrowed"] += 1
                    print(f" '{title}'을(를) 대출했습니다. 남은 수량: {available - 1}")
                else:
                    print(f" '{title}'은(는) 현재 모두 대출 중입니다.")
                break
        else:
            print(" 해당 도서는 도서관에 없습니다.")

    # 4. 도서 반납
    elif menu == "4":
        title = input(" 반납할 책 제목 (띄어쓰기 지켜주세요!!): ").strip()
        for book in books:
            if book["title"] == title and book["borrowed"] > 0:
                book["borrowed"] -= 1
                print(f" '{title}'을(를) 반납했습니다. 현재 남은 대출 가능 수량: {book['quantity'] - book['borrowed']}")
                break
        else:
            print(" 대출 내역이 없는 도서입니다.")

    # 5. 전체 도서 목록 출력
    elif menu == "5":
        if books:
            print("# 현재 도서 목록 #")
            print("┌----------------------------┐")
            for book in books:
                available = book["quantity"] - book["borrowed"]
                
                print(f" 제목: {book['title']}")
                print(f" 저자: {book['author']}")
                print(f" 남은 수량: {available}")
                print(" ---------------------------- ")
            print("└----------------------------┘")
        else:
            print(" 도서관에 책이 없습니다.")

    # 6. 종료
    elif menu == "6":
        print(" 도서관 시스템을 종료합니다.")
        break

    # 7. 잘못된 명령어 처리
    else:
        print(" 올바른 명령어를 입력하세요. (추가, 검색, 대출, 반납, 목록, 종료)")
