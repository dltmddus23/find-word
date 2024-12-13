# 단어 찾기 프로그램
def word_search(file_path, word_to_find):
    # 결과를 저장할 리스트
    lines_with_word = []

    # 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            # 단어가 해당 줄에 있는지 확인 (대소문자 무시)
            if word_to_find.lower() in line.lower():
                lines_with_word.append(line_number)
    
    # 결과 출력
    if lines_with_word:
        print(f"'{word_to_find}' 단어는 다음 줄에서 발견되었습니다: {lines_with_word}")
    else:
        print(f"'{word_to_find}' 단어는 파일에서 발견되지 않았습니다.")

# 실행 코드
if __name__ == "__main__":
    print("Avicii SOS 단어 찾기 프로그램입니다.")
    word_to_find = input("찾고 싶은 단어를 입력하세요: ")
    word_search("example.txt", word_to_find)
