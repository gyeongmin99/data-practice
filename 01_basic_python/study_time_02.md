# STEP 9 – CSV-based Analysis

Data was loaded from an external CSV file using pandas.
Separating data from code allows the same analysis logic
to be reused across different datasets.


#CSV 파일을 읽고 간단한 요약 및 분포 통계 구하기


## df란? 
df: 데이터 프레임을 정의하는 함수

(예제)
- usage_minutes: 이용 시간
- df["usage_minutes"]: CSV 속 'usage_minutes' 한 열의 값을 통째로 꺼낸 것
- df["usage_minutes"] == 0 : 열 전체에 대한 비교 --> 각 행마다 '0'인지를 확인 (★pandas 규칙)
    ==> 각 행이 0이면 True, 0이 아니면 False
    ==> [False, True, False ...] (불리언 마스크, Boolean mask)
    - 각 행이 조건을 만족하는지 True/False로 표시해 두는 것
- .sum(): 모두 합하는 것
    - True ->1, False -> 0으로 표시 (★pandas 규칙)
    ==> [False, True, False ... ] -> [0, 1, 0, ...]
    ==> (df["usage_minutes"]==0).sum() : 1의 합산 = N : '0'인 달(이용 시간이 0시간인 달) N개

💡활용
total_usage = df["usage_minutes"].sum()
average_usage = df["usage_minutes"].mean()
min_usage = df["usage_minutes"].min()
max_usage = df["usage_minutes"].max()
zero_months = (df["usage_minutes"] == 0).sum()

👾정리
df[""]: 열 선택
df[""] == 0 : 조건 검사
(df[""]==0).sum() : True의 개수 


### 특정 조건에서는?
**이용 시간이 0분인 달 말고, 5분 미만인 달.. 인 경우에도 확인 가능한가?
- df["usage_minutes"] < 5
- low_usage = df["usage_minutes"] < 5
    --> 'low_usage' (낮은 사용량)를 5분 미만으로 정의함
- print(low_usage)
- (df["usage_minutes"]<5).sum(): 사용 시간이 5분 미만인 달의 개수

- 범위 조건 (AND): (df["usage_minutes"] >=10) & (df["usage_minutes"]<60)
- 여러 조건 중 하나라도 만족(OR): (df["usage_minutes"] == 0) | (df["usage_minutes"] > 80)
