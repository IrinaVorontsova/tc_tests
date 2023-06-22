import allure

from constants.read_env import ReadEnv
from models.tabs_model import TabsModel
from pages.main_page import StartPage


class TestsTC:
    def test_tc_ui(self, setup_browser):
        # with allure.step("Authorization data"):
        #     user = Authorization(
        #         login=ReadEnv.LOGIN,
        #         password=ReadEnv.PASSWORD)

        with allure.step("Initialize form page"):
            start_page = StartPage(setup_browser)

        with allure.step("Open test urls"):
            start_page.open_browser(ReadEnv.URL)
            start_page.check_tabs(main_page=ReadEnv.MAIN_PAGE, city=ReadEnv.SPB, menu_title=ReadEnv.MENU_TITLE, delivery_title=ReadEnv.DELIVERY_TITLE,
                                    promos_title=ReadEnv.PROMOS_TITLE, news_title=ReadEnv.NEWS_TITLE, addresses_title=ReadEnv.ADDRESSES_TITLE, cooking=ReadEnv.COOKING,
                                    banquet=ReadEnv.BANQUET)


        # with allure.step("Passed data for authorization"):
        #     registration.authorization(vk_header=ReadEnv.VK_HEADER, authorization=user, check_password=ReadEnv.CHECK_PASSWORD)
        #
