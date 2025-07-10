import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page, create_course_page):
    create_course_page.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.create_course_toolbar.check_visible()

    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

    create_course_page.fill_create_course_form.check_visible_create_course_form(
        title='', estimated_time='', description='', max_score='0', min_score='0')

    create_course_page.create_exercise_toolbar.check_visible()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.image_upload_widget.upload_preview_image(
        r'C:\Users\Rita\PycharmProjects\autotests-ui\testdata\files\image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    create_course_page.fill_create_course_form.fill(
        title="Playwright", estimated_time="2 weeks", description='Playwright', max_score="100", min_score="10")

    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
    create_course_page.create_course_toolbar.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()

    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", estimated_time="2 weeks", max_score="100", min_score="10")
