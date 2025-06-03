from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_title(self):
        expect(self.page_title).to_have_text('Dashboard')

    def check_dashboard_url(self):
        expect(self.page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
