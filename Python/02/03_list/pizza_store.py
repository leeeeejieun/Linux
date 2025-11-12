movies = {'파묘': [23.6, 5.5, 11914798],
          '범죄도시4': [20.6, 8.8, 11502779],
          '인사이드 아웃2': [15.6, 8.8, 7525302],
          '베테랑2': [10.8, 5.3, 5000000]}

print(movies['파묘'][2])

# for m in movies:
#     if movies[m][1] == 8.8:
#        print(m)

# 평점이 8.8인 영화 제목 출력
print('*' * 50)
print('평점이 8.8인 영화 제목 출력')
print('*' * 50)
for k,m in movies.items():
    if m[1] == 8.8:
        print(k)

# 관객 수가 100만명 이상인 영화 제목
print('*' * 50)
print('관객 수가 1000만명 이상인 영화 제목')
print('*' * 50)
for k,m in movies.items():
    if m[2] >= 10000000:
        print(k)