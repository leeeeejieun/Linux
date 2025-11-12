#!/usr/bin/python3

# 도시 이름 중 가장 긴 길이와 짧은 길이를 반환 하는 함수
def cal_length(cities):
    cities_length = [len(city) for city in cities]   # 도시 길이만 추출하여 리스트로 저장
    return max(cities_length), min(cities_length)    # 가장 긴 길이와 짧은 길이 반환

# 가장 긴 이름의 도시와 짧은 이름의 도시를 찾는 함수
def find_short_long_city(longest_length, shortest_length, cities):
    longest_list = []   # 긴 이름의 도시 이름을 저장할 리스트
    shortest_list = []  # 짧은 이름의 도시 이름을 저장할 리스트

    for city in cities:
        if len(city) == longest_length:
            longest_list.append(city)
        elif len(city) == shortest_length:
            shortest_list.append(city)

    return longest_list, shortest_list  # 결과 반환

# 형식을 알맞게 변환하여 결과 출력
def print_short_long_city(longest_list, shortest_list):
    print(f"Long Name City: {''.join(longest_list)}")
    print(f"Short Name City: {', '.join(shortest_list)}")

# 메인 함수 정의
def main():
    # 도시 리스트
    cities = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'busan']

    # 함수 호출
    longest_length, shortest_length = cal_length(cities)
    longest_list, shortest_list = find_short_long_city(longest_length, shortest_length,cities)
    print_short_long_city(longest_list, shortest_list)

# 메인 함수 호출
if __name__ == "__main__":
    main()






