# 단어 찾기 프로그램 (example.txt용)
def word_search(word_to_find):
    # example.txt 파일 열기
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        
    # 단어 개수 세기
    word_count = content.lower().split().count(word_to_find.lower())
    print(f"'{word_to_find}' 단어는 총 {word_count}번 발견되었습니다.")

# 실행 코드
if __name__ == "__main__":
    print("단어 찾기 프로그램에 오신 것을 환영합니다!")
    word_to_find = input("찾고 싶은 단어를 입력하세요: ")
    word_search(word_to_find)
