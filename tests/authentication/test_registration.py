import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_success_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com', password='password', username='username')
        registration_page.registration_form.check_visible(
            email='user.name@gmail.com', password='password', username='username')
        registration_page.click_registration_button()
        dashboard_page.check_dashboard_url()
        dashboard_page.dashboard_toolbar_view.check_visible()

    def test_navigate_from_registration_to_authorization(self,
                                                         registration_page: RegistrationPage,
                                                         login_page: LoginPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.click_login_link()

        login_page.login_form.check_visible(email='', password='')
