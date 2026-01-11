#Review for study_time_01

# 주제: 월별 앱 사용 시간 분석
    한 모바일 앱의 월별 평균 사용 시간(분)을 기록했다. 이 데이터를 통해 사용 패턴을 파악하고자 한다.

import matplotlib.pyplot as plt

# 8개월 간 월별 앱 사용 평균 시간(분), 0은 거의 사용 하지 않은 달

usage_minute = [45, 0, 30, 60, 90, 40, 0, 75]
    # 이 데이터는 이용자 행동 데이터인가, 0은 단순한 숫자인가 의미있는 신호인가?

# 기본 요약 통계
total_minutes = sum(usage_minute)
number_of_months = len(usage_minute)
average_minutes = total_minutes / number_of_months

print("Total usage minutes: ", total_minutes)
print("Number of months: ", number_of_months)
print("Average minutes per month: ", average_minutes)

    # 평균 사용 시간이 높으면 "앱 사용성이 좋다" 라고 할 수 있는가?

# 분포 확인용 통계
min_minute = min(usage_minute)
max_minute = max(usage_minute)
zero_months = usage_minute.count(0)

print("Minimum usage minutes: ", min_minute)
print("Maximum usage minute: ", max_minute)
print("Month with zero usage: ", zero_months)

# 막대그래프 작성★

months = list(range(1, len(usage_minute)+1))
    # 이 줄은 축에 쓸 값들을 자동으로 만들어주는 코드
        # (내가 가진 데이터) usage_minutes는 y축의 값
        # len 함수는 usage_minute 안에 값이 몇 개 있는지 세어 줌
    # range()는 숫자를 순서대로 만들어주는 도구로,
        # 예로, range(1,9)하고 한다면, 1, 2, 3, 4, 5, 6, 7, 8로 출력됨 (*끝 숫자는 포함되지 않음)
            # 이런 이유로, 끝에 +1을 해 주어야 함 => 데이터의 개수와 정확히 맞추기 위해서
    # list()는 그래프에 사용할 실제 값의 묶음을 만들어 줌
        # range(1,9)와 같은 형태는 python 내부의 범위 객체일 뿐, 그래프에 사용할 수 있는 실제 값은 아님
        # 따라서, list(range(1,9))라고 한다면 [1, 2, 3, 4, 5, 6, 7, 8]로 그래프에 사용할 수 있는 x축이 만들어짐
    # [결론]
        # 1. x축 설정: months = list()
        # 2. x축 값 부여: list () = [1, 2, 3, 4, 5, 6, 7, 8]
            # <= range(1,9)
            # <= range(1, len(usage_minute)+1)

    ## x축은 "순서/범주" / y축은 "크기/강도"


plt.bar(months, usage_minute)
plt.xlabel("Month")
plt.ylabel("Average Usage (minutes)")
plt.title("Monthly App Usage")

plt.show()

    ## 그래프에서 0인 달이 즉시 보이는가
    ## 사용량이 특정 달에 몰려 있는가
    ## 평균 시간이 "전형적 사용자"를 잘 설명하는가

## 평균 사용 시간은 약 42분이지만, 사용이 거의 없는 달도 존재함
## 사용 시간의 편차가 크기 때문에 평균만으로는 사용자 경험을 대표하기 어려움
## 막대그래프는 사용 중단과 집중 사용 시점을 한 눈에 보여줌

