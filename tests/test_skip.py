from selene import browser, have
import pytest
import allure


def is_desktop(height):
    return height > 1000


@pytest.fixture(
    scope='function',
    autouse=True,
    params=[(375, 667), (393, 851), (1920, 1080), (1280, 1024)]
)
def browser_settings(request):
    with allure.step("Configuration browser"):
        browser.config.window_width, browser.config.window_height = request.param
        yield
    with allure.step("Close browser"):
        browser.quit()


def test_github_desktop():
    with allure.step("Check condition if height for desktop"):
        if not is_desktop(browser.config.window_height):
            pytest.skip('Этот тест только для десктопа')
    with allure.step("Open main page github"):
        browser.open('https://github.com/')
    with allure.step("Click on 'Sign in'"):
        browser.element('[href="/login"]').click()
    with allure.step("Check sign in text on header"):
        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile():
    with allure.step("Check condition if height for mobile"):
        if is_desktop(browser.config.window_height):
            pytest.skip('Этот тест только для мобильных устройств')
    with allure.step("Open main page github"):
        browser.open('https://github.com/')
    with allure.step("Open 'hamburger'"):
        browser.element('.flex-1 button').click()
    with allure.step("Click on 'Sign in'"):
        browser.element('[href="/login"]').click()
    with allure.step("Check sign in text on header"):
        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
