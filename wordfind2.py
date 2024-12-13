# 파일 읽기 및 단어 검색 프로그램
def word_search(file_path, search_word):
    # 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()  # 파일 내용을 줄 단위로 읽기

    # 검색 결과 저장
    results = []

    # 각 줄에서 단어 찾기
    for line_number, line in enumerate(lines, start=1):
        # 줄에서 단어를 찾을 때 모든 시작 위치를 기록
        start_index = 0
        while (index := line.find(search_word, start_index)) != -1:
            # 위치 저장 (칸 번호는 1부터 시작하도록 조정)
            results.append((line_number, index + 1))
            start_index = index + 1  # 다음 검색 시작 위치를 업데이트

    return results


# 실행 코드
if __name__ == "__main__":
    print("단어 찾기 프로그램 입니다.")

    # 파일 이름 고정: test.txt
    file_path = "test.txt"

    # 사용자로부터 검색할 단어 입력
    search_word = input("찾고 싶은 단어를 입력하세요: ")

    # 단어 찾기 실행
    matches = word_search(file_path, search_word)

    # 결과 출력
    if matches:
        print(f"'{search_word}' 단어는 다음 위치에서 발견되었습니다:")
        for match in matches:
            line, column = match
            print(f"  - 줄: {line}, 칸: {column}")
    else:
        print(f"'{search_word}' 단어는 파일에서 발견되지 않았습니다.")

