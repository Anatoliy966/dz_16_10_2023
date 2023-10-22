# dz 16.10.2023

import pytest

link = "https://solmar.com.ua/ua/"

class TestPage1:
    @pytest.mark.smoke
    def test_math_1(self, browser):
        browser.get(link)
        result = 3 ** 2  # Возводим 5 в квадрат
        expected_result = 9
        assert result == expected_result
        print("Выполнен test_math_1")

    @pytest.mark.smoke
    def test_math_2(self, browser):
        browser.get(link)
        result = 10 ** 2  # Возводим 5 в квадрат
        expected_result = 100
        assert result == expected_result
        print("Выполнен test_math_2")

    @pytest.mark.regression
    def test_math_3(self, browser):
        browser.get(link)
        num1 = 10
        num2 = 5
        result = num1 + num2
        expected_result = 15
        assert result == expected_result
        print("Выполнен test_math_3")

    @pytest.mark.regression
    def test_math_4(self, browser):
        browser.get(link)
        result = 50 / 2  # Возводим 5 в квадрат
        expected_result = 25
        assert result == expected_result
        print("Выполнен test_math_4")

    @pytest.mark.regression
    def test_math_5(self, browser):
        browser.get(link)
        result = 32 - 2  # Возводим 5 в квадрат
        expected_result = 30
        assert result == expected_result
        print("Выполнен test_math_5")

    @pytest.mark.funct
    def test_math_6(self, browser):
        browser.get(link)
        result = 100 ** 2  # Возводим 5 в квадрат
        expected_result = 10000
        assert result == expected_result
        print("Выполнен test_math_6")
