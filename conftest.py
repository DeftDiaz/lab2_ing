import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            screenshot = driver.get_screenshot_as_base64()
            html = (
                "<div><img src=\"data:image/png;base64,"
                f"{screenshot}\" alt=\"screenshot\" "
                "style=\"width:304px;height:228px;\" "
                "onclick=\"window.open(this.src)\" align=\"right\"/></div>"
            )
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                extras.append(pytest_html.extras.html(html))
            report.extra = extras


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI", "").lower() == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
