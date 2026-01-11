#study_time_02 (260112)
    ## CSV 기반 데이터 분석 (pandas 기초)


# CSV 파일 읽기
import pandas as pd
    #pandas: csv를 표처럼 다루는 도구
import matplotlib.pyplot as plt

df = pd.read_csv("app_usage.csv")
    # pd.read_csv("읽을 파일의 이름"): CSV 파일을 읽어라
    # df = : 읽은 결과를 df라는 변수에 저장하라
        # df: DataFrame의 약자처럼 사용하는 관습적 이름
        
print(df)
    # CSV가 제대로 읽혔는지 확인하는 작업


# 기본 요약 통계 (리스트 -> 열(column))
total_usage = df["usage_minutes"].sum()
average_usage = df["usage_minutes"].mean()
min_usage = df["usage_minutes"].min()
max_usage = df["usage_minutes"].max()
zero_months = (df["usage_minutes"] == 0).sum()

    # 요약 통계 명령들: 모두 pandas로 계산
    # df["usage_miutes"]: 열 선택 => usage_minutes 열만 꺼낸 것
        ## df는 표 전체
            ## --> df["~"] = [45, 0, 30 ....]

    # .sum(): 그 열의 모든 값을 더함(총합)
    # .mean(): 평균 (총합/개수)
    # .min()/.max(): 최소값 / 최대값
        # pandas에서는 열.기능() 형태로 사용함
    # df["usage.minutes"] == 0
        ## usage_minutes 열에서 값이 0인가?를 행마다 검사하고, 결과는 T/F로 이루어진 목록이 됨
        ## --> [F, T, F, F ...]
        ## True는 1로, False는 0으로 계산됨. 즉, .sum()하면 True의 개수, 즉 0인 달의 수가 됨


print("Total usage minutes:", total_usage)
print("Average usage minutes:", average_usage)
print("Minimum usage minutes:", min_usage)
print("Maximum usage minutes:", max_usage)
print("Months with zero usage:", zero_months)

    # df["usage_minutes"] = 하나의 데이터 열
    # 연산은 열 전체에 대해 수행

# CSV 기반 시각화
plt.bar(df["month"], df["usage_minutes"])
plt.xlabel("Month")
plt.ylabel("Usage Minutes")
plt.title("Monthly App Usage (CSV-based)")
plt.show()



