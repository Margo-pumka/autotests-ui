from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

from dataclasses import dataclass


@dataclass
class CheckVisibleCourseCardParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str


class CoursesListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Навбар и сайдбар
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Заголовок и кнопка создания курса
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Карточка курса
        self.course_view = CourseViewComponent(page)

        # Пустой блок при отсутствии курсов
        self.empty_view = EmptyViewComponent(page, 'courses-list')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
