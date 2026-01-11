# STEP 9 – CSV-based Analysis

Data was loaded from an external CSV file using pandas.
Separating data from code allows the same analysis logic
to be reused across different datasets.


#CSV 파일을 읽고 간단한 요약 및 분포 통계 구하기


## df란? 
df: 데이터 프레임을 정의하는 함수 <br>

(예제)
- usage_minutes: 이용 시간
- df["usage_minutes"]: CSV 속 'usage_minutes' 한 열의 값을 통째로 꺼낸 것<br>
- df["usage_minutes"] == 0 : 열 전체에 대한 비교 --> 각 행마다 '0'인지를 확인 (★pandas 규칙)<br>
    ==> 각 행이 0이면 True, 0이 아니면 False<br>
    ==> [False, True, False ...] (불리언 마스크, Boolean mask)<br>
    - 각 행이 조건을 만족하는지 True/False로 표시해 두는 것<br>
- .sum(): 모두 합하는 것<br>
    - True ->1, False -> 0으로 표시 (★pandas 규칙)<br>
    ==> [False, True, False ... ] -> [0, 1, 0, ...]<br>
    ==> (df["usage_minutes"]==0).sum() : 1의 합산 = N : '0'인 달(이용 시간이 0시간인 달) N개<br>

💡활용<br>
total_usage = df["usage_minutes"].sum()<br>
average_usage = df["usage_minutes"].mean()<br>
min_usage = df["usage_minutes"].min()<br>
max_usage = df["usage_minutes"].max()<br>
zero_months = (df["usage_minutes"] == 0).sum()<br>

👾정리<br>
df[""]: 열 선택<br>
df[""] == 0 : 조건 검사<br>
(df[""]==0).sum() : True의 개수 <br>


### 특정 조건에서는?
**이용 시간이 0분인 달 말고, 5분 미만인 달.. 인 경우에도 확인 가능한가?<br>
- df["usage_minutes"] < 5<br>
- low_usage = df["usage_minutes"] < 5<br>
    --> 'low_usage' (낮은 사용량)를 5분 미만으로 정의함<br>
- print(low_usage)<br>
- (df["usage_minutes"]<5).sum(): 사용 시간이 5분 미만인 달의 개수<br>

- 범위 조건 (AND): (df["usage_minutes"] >=10) & (df["usage_minutes"]<60)<br>
- 여러 조건 중 하나라도 만족(OR): (df["usage_minutes"] == 0) | (df["usage_minutes"] > 80)<br>
