def test_success_registration(registration_page, dashboard_page):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form.fill(email='user.name@gmail.com', password='password', username='username')
    registration_page.fill_registration_form.check_visible(
        email='user.name@gmail.com', password='password', username='username')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_url()
    dashboard_page.dashboard_title.check_visible()


def test_go_to_login_page(registration_page, login_page):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.click_login_link()
    login_page.check_login_url()
