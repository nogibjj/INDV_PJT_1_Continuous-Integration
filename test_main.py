import matplotlib.pyplot as plt  # matplotlib을 import해야 합니다.
from main import ppl, age_mean, age_median, age_std


def test_age_statistics():
    """
    Test that age statistics (mean, median, std) match the expected values.
    """
    expected_mean = ppl["Age"].mean()  # 예상 평균
    expected_median = ppl["Age"].median()  # 예상 중앙값
    expected_std = ppl["Age"].std()  # 예상 표준편차

    assert round(age_mean, 1) == round(
        expected_mean, 1
    ), f"Expected mean: {expected_mean}, but got: {age_mean}"
    assert (
        age_median == expected_median
    ), f"Expected median: {expected_median}, but got: {age_median}"
    assert age_std == expected_std, f"Expected std: {expected_std}, but got: {age_std}"

    print("Test_passed: Age statistics are correct.")


def test_age_histogram():
    """
    Test that the age histogram is displayed without errors.
    """
    try:
        plt.figure(figsize=(8, 6))
        ppl["Age"].plot(kind="hist", bins=10, edgecolor="black")
        plt.title("Age Distribution Histogram")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
        plt.show()
        print("Check histogram: Successfully displayed.")
    except Exception as e:
        print(f"Test_failure: {e}")


if __name__ == "__main__":
    test_age_statistics()  # Descriptive statistics test
    test_age_histogram()  # Visualization test
