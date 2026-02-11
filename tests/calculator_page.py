def test_decimal_numbers(self, driver):
    file_path = os.path.abspath("../src/index.html")
    driver.get(f"file://{file_path}")

    driver.find_element(By.ID, "num1").send_keys("5.5")
    driver.find_element(By.ID, "num2").send_keys("2.3")

    select = Select(driver.find_element(By.ID, "operation"))
    select.select_by_value("add")

    driver.find_element(By.ID, "calculate").click()

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )

    assert "7.8" in result.text
