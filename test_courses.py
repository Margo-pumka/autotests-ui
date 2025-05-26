import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Открывем страницу регистрации
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()
        context.storage_state(path="usename_state.json")

        # Открываем страницу с курсами
        new_browser = playwright.chromium.launch(headless=False)
        new_context = new_browser.new_context(storage_state="usename_state.json")
        new_page = new_context.new_page()

        new_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        new_page.get_by_test_id('courses-list-empty-view-icon')

        new_page_toolbar = new_page.get_by_test_id('courses-list-toolbar-title-text')
        expect(new_page_toolbar).to_have_text('Courses')

        new_page_courses_title = new_page.get_by_test_id('courses-list-empty-view-title-text')
        expect(new_page_courses_title).to_have_text('There is no results')

        new_page_description = new_page.get_by_test_id('courses-list-empty-view-description-text')
        expect(new_page_description).to_have_text('Results from the load test pipeline will be displayed here')
