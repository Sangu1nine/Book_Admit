# 도서관 = {'분야':[[식별코드, 도서명, 저자, 대출여부],[],[]]}
# 디스플레이_대출
# 디스플레이_반납
# 디스플레이_검색

import book_func as bf

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
        break

    # 7. 잘못된 명령어 처리
    else:
        print(" 메뉴를 1~6사이의 숫자로 입력해주세요. ")