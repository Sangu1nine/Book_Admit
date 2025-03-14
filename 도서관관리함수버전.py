# 도서관 = {'분야':[[식별코드, 도서명, 저자, 대출여부],[],[]]}
# 디스플레이_대출
# 디스플레이_반납
# 디스플레이_검색

import book_func as bf
filename = 'library.json'
display = '''
┌==================================================┐
   1. 추가 2. 검색 3. 대출 4. 반납 5. 목록, 6.종료
└==================================================┘
메뉴 번호를 선택해주세요 >>> '''

# 빈 리스트 선언 (도서 목록)
books = bf.book_load(filename)

while True:
    menu = input(display).strip()


    # 1. 도서 추가
    if menu == '1':
        books = bf.book_add(books)

    # 2. 도서 검색
    elif menu == '2':
        books = bf.book_search(books)

    # 3. 도서 대출
    elif menu == '3':
        books = bf.book_checkout(books)

    # 4. 도서 반납
    elif menu == "4":
        books = bf.book_return(books)

    # 5. 전체 도서 목록 출력
    elif menu == "5":
        books = bf.book_list(books)

    # 6. 종료
    elif menu == "6":
        print(" 도서관 시스템을 종료합니다.")
        bf.book_save(books,filename)
        break

    # 7. 잘못된 명령어 처리
    else:
        print(" 메뉴를 1~6사이의 숫자로 입력해주세요. ")