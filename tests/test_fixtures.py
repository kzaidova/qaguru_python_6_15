from selene import browser, have
import pytest
import allure



@pytest.fixture(scope='function', autouse=False, params=[(1920, 1080)])
def github_desktop(request):
    with allure.step("Configuration browser"):
        browser.config.window_width, browser.config.window_height = request.param
        yield
    with allure.step("Close browser"):
        browser.quit()


@pytest.fixture(scope='function', autouse=False, params=[(375, 667)])
def github_mobile(request):
    with allure.step("Configuration browser"):
        browser.config.window_width, browser.config.window_height = request.param
    with allure.step("Pause browser"):
        yield
    with allure.step("Close browser"):
        browser.quit()



def test_github_desktop(github_desktop):
    with allure.step("Open main page github"):
        browser.open('https://github.com/')
    with allure.step("Click on 'Sign in'"):
        browser.element('[href="/login"]').click()
    with allure.step("Check sign in text on header"):
        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(github_mobile):
    with allure.step("Open main page github"):
        browser.open('https://github.com/')
    with allure.step("Open 'hamburger'"):
        browser.element('.flex-1 button').click()
    with allure.step("Click on 'Sign in'"):
        browser.element('[href="/login"]').click()
    with allure.step("Check sign in text on header"):
        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
