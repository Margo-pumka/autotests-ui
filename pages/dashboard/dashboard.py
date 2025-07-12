from playwright.sync_api import expect

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

    def check_dashboard_url(self):
        expect(self.page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
