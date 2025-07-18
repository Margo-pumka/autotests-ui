import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_success_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email, password=settings.test_user.password, username=settings.test_user.username)
        registration_page.registration_form.check_visible(
            email=settings.test_user.email, password=settings.test_user.password, username=settings.test_user.username)
        registration_page.click_registration_button()
        dashboard_page.check_dashboard_url()
        dashboard_page.dashboard_toolbar_view.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from registration page to login page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_registration_to_authorization(self,
                                                         registration_page: RegistrationPage,
                                                         login_page: LoginPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.click_login_link()

        login_page.login_form.check_visible(email='', password='')
