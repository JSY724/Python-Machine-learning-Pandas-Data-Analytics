# -*- coding: utf-8 -*-
#6-16. 그룹 연산 데이터 변환 : group.transform(매핑함수)
# 그룹 연산의 결과를 원본 df와 같은 형태(각 원소의 본래 행, 열 기준)로 변형하여 정리
# 즉 반환되는 객체는 그룹별로 나누지 않고, 원래 행 인덱스 순서로 정렬
# (agg: 그룹별 연산 결과를 그룹별로 집계 반환)


# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 

# 그룹별 age 열의 평균 집계 연산
age_mean = grouped.age.mean()
print(age_mean)
print('\n')

# 그룹별 age 열의 표준편차 집계 연산
age_std = grouped.age.std()
print(age_std)
print('\n') 

# 그룹 객체의 age 열을 iteration으로 z-score를 계산하여 출력
#z-score: z= (x-mean)/std
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
        # 한 그룹의 각 value- 해당 열 평균/해당 열 표준편차  
        # 위 연산을 해당 그룹의 모든 원소에 대해 수행, 모든 그룹에 대해 수행
    print('* origin :', key)
    print(group_zscore.head(3))  # 각 그룹의 첫 3개의 행을 출력
    print('\n')
    # 행 인덱스는 원본과 그대로 유지



# z-score를 계산하는 사용자 함수 정의
def z_score(x): 
    return (x - x.mean()) / x.std()
   
# transform() 메소드를 이용하여 age 열의 데이터를 z-score로 변환
age_zscore = grouped.age.transform(z_score)  
#반환되는 객체는 그룹별로 나누지 않고 원래 행 인덱스 순서로 정렬
print(age_zscore.loc[[1, 9, 0]])     # 1, 2, 3 그룹의 첫 데이터 확인 (변환 결과)
print('\n')
print(len(age_zscore))              # transform 메소드 반환 값의 길이
print('\n')
print(age_zscore.loc[0:9])          # transform 메소드 반환 값 출력 (첫 10개)
print('\n')
print(type(age_zscore))             # transform 메소드 반환 객체의 자료형: series
