import itertools
import random


def create_scenarios():
    # DEMAND
    demand_uniform_range = [
        (i, j)
        for i in range(10, 14)  # 10 to 13
        for j in range(i, 14)  # i to 13
        if i <= j
    ]
    demand_uniform = [
        {"Dist_Type": "UNIFORM", "min": min_val, "max": max_val}
        for min_val, max_val in demand_uniform_range
    ]
    demand_gaussian = [
        {"Dist_Type": "GAUSSIAN", "mean": mean, "std": std}
        for mean in range(9, 14)  # 9 to 13
        for std in range(1, 5)    # 1 to 4
    ]

    # LEADTIME
    leadtime_uniform_range = [
        (i, j)
        for i in range(1, 4)  # 1 to 3
        for j in range(i, 4)  # i to 3
        if i <= j
    ]
    leadtime_uniform = [
        {"Dist_Type": "UNIFORM", "min": min_val, "max": max_val}
        for min_val, max_val in leadtime_uniform_range
    ]
    leadtime_gaussian = [
        {"Dist_Type": "GAUSSIAN", "mean": mean, "std": std}
        for mean in range(1, 4)   # 1부터 3까지
        for std in range(1, 4)    # 1부터 3까지
    ]

    # 모든 조합 생성
    scenarios = list(itertools.product(demand_uniform +
                     demand_gaussian, leadtime_uniform + leadtime_gaussian))
    scenarios = [{"DEMAND": demand, "LEADTIME": leadtime}
                 for demand, leadtime in scenarios]

    return scenarios


def split_scenarios(scenarios, train_ratio=0.8):
    # 시나리오 리스트를 무작위로 섞습니다.
    random.shuffle(scenarios)

    # 훈련 세트의 크기를 계산합니다.
    train_size = int(len(scenarios) * train_ratio)

    # 리스트를 8:2 비율로 나눕니다.
    train_scenarios = scenarios[:train_size]
    test_scenarios = scenarios[train_size:]

    return train_scenarios, test_scenarios
