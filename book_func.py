def book_add(books) :
    title = input(" 책 제목: ").strip(" ,.:").lower()
    author = input(" 저자: ").strip(" ,.:").lower()
    
    while True :
        quantity_input = input(" 수량을 숫자로 입력해주세요: ").strip()
        if quantity_input.isnumeric():  # 숫자인지 확인
            quantity = int(quantity_input)  # 숫자로 변환
            break
        else :
            print("숫자만 입력해주세요!")  # 숫자가 아니면 다시 입력 요청
    found = False  # 우선적으로 책 검색
    for book in books: # 도서관에 이미 있던 도서명과 일치하면 found = True로 바꾸기
        if book["title"] == title:
            book["quantity"] += quantity
            print(f" '{title}'의 수량이 {quantity}권 추가되었습니다. (총 {book['quantity']}권)")
            found = True
            break
    if not found: # 전부 비교를 했는데 겹치는 것이 없으므로 found = False인 상태이므로 돌아가는 코드
        books.append({"title": title, "author": author, "quantity": quantity, "borrowed": 0})
        print(f" 새로운 도서 '{title}'이(가) 추가되었습니다. ({quantity}권)")
    return books

def book_search(books) :
    keyword = input(" 검색어 (제목 또는 저자): ").strip().replace(" ","").replace(",","") # 띄어쓰기와 ","를 안쳐도 검색이 되도록
    results = [book for book in books if keyword in book["title"].replace(" ","").replace(",","") or keyword in book["author"].replace(" ","").replace(",","")]

    if results:
        print(" 검색 결과 :")
        for book in results:
            available = book["quantity"] - book["borrowed"]
            print("┌--------------------------------┐")
            print(f" 제목: {book['title']}")
            print(f" 저자: {book['author']}")
            print(f" 남은 수량: {available}")
            print("└--------------------------------┘")
    else:
        print(" 검색 결과가 없습니다.")
    return books

def book_checkout(books) :
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
        if book["title"].replace(" ","").replace(",","") == title.replace(" ","").replace(",",""):
            available = book["quantity"] - book["borrowed"]
            if available > 0:
                book["borrowed"] += 1
                print(f" '{title}'을(를) 대출했습니다. 남은 수량: {available - 1}")
            else:
                print(f" '{title}'은(는) 현재 모두 대출 중입니다.")
            break
    else:
        print(" 해당 도서는 도서관에 없습니다.")
    return books

def book_return(books) :
    title = input(" 반납할 책 제목 : ").strip()
    for book in books:
        if book["title"].replace(" ","").replace(",","") == title.replace(" ","").replace(",","") and book["borrowed"] > 0:
            book["borrowed"] -= 1
            print(f" '{title}'을(를) 반납했습니다. 현재 남은 대출 가능 수량: {book['quantity'] - book['borrowed']}")
            break
    else:
        print(" 대출 내역이 없는 도서입니다.")
    return books

def book_list(books) :
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
    return books
