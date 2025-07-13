import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.regression
def empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')

    new_page_toolbar = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(new_page_toolbar).to_have_text('Courses')

    new_page_courses_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(new_page_courses_title).to_have_text('There is no results')

    new_page_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(new_page_description).to_have_text('Results from the load test pipeline will be displayed here')
