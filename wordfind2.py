def word_search(file_path, search_word):
    # 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    # 각 줄을 나누어 리스트로 변환
    grid = data.split("\n")

    # 검색 결과 저장 (위치, 방향 포함)
    results = []

    # 검색할 단어 길이
    word_len = len(search_word)

    # 검색 방향 정의
    directions = {
        "오른쪽 가로": (0, 1),
        "왼쪽 가로": (0, -1),
        "아래로 세로": (1, 0),
        "위로 세로": (-1, 0),
        "오른쪽 아래 대각선": (1, 1),
        "왼쪽 위 대각선": (-1, -1),
        "오른쪽 위 대각선": (-1, 1),
        "왼쪽 아래 대각선": (1, -1),
    }

    # 2차원 배열에서 단어 찾기
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # 각 방향으로 검색
            for direction, (dy, dx) in directions.items():
                found = True
                for i in range(word_len):
                    ny, nx = y + i * dy, x + i * dx
                    # 경계 조건 확인
                    if (
                        ny < 0 or ny >= len(grid) or
                        nx < 0 or nx >= len(grid[ny]) or
                        grid[ny][nx] != search_word[i]
                    ):
                        found = False
                        break
                if found:
                    # (x, y 좌표는 1부터 시작하도록 조정)
                    results.append((y + 1, x + 1, direction))

    return results


# 실행 코드
if __name__ == "__main__":
    print("단어 찾기 프로그램입니다")

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
            line, column, direction = match
            print(f"  - 줄: {line}, 칸: {column}, 방향: {direction}")
    else:
        print(f"'{search_word}' 단어는 파일에서 발견되지 않았습니다.")

