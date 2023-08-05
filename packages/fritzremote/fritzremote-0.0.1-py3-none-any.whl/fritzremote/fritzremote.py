import time
from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from fritzremote.model import FritzInput, FritzButton, FritzPages, FritzWifiProfileSelect, FritzPath


class FritzRemote(object):
    """
    Navigates on the fritz.box user interface and changes settings.
    https://en.avm.de/service/fritzbox/fritzbox-7430/knowledge-base/publication/show/1_Opening-the-FRITZ-Box-user-interface/

    This class expects an selenium web driver object to work.
    See https://selenium-python.readthedocs.io/index.html for more.
    """
    _browser: WebDriver
    _host: str

    def __init__(self, browser: WebDriver) -> None:
        self._browser = browser

    def start(self) -> None:
        assert self.host
        self.browser.get(self.host)

    def login(self, username: str, password: str) -> None:
        input_username = FritzInput('uiViewUser', username)
        input_password = FritzInput('uiPass', password)
        button = FritzButton('submitLoginBtn', By.ID)

        self.__fill_input([input_username, input_password])
        self.__click_button(button)

    def got_to_wifi_profiles(self) -> None:
        page = FritzPages()
        self.__navigate(page.child_lock)

    def change_wifi_profiles(self, settings: Dict[str, str]):

        for setting in settings:
            select = FritzWifiProfileSelect(device_name=setting, profile=settings[setting])
            self.__select_option(select)

        self.__click_button(FritzButton('#btn_form_foot button:first-Child', By.CSS_SELECTOR))

    def close(self) -> None:
        self.browser.close()

    def quit(self) -> None:
        self.browser.quit()

    def __navigate(self, path: FritzPath) -> None:
        path_fragments = path.fragments

        for segment in path_fragments:
            element: WebElement = WebDriverWait(self.browser, 60).until(
                EC.element_to_be_clickable((By.ID, segment))
            )
            time.sleep(1)
            element.click()

    def __fill_input(self, input_fields: List[FritzInput]) -> None:

        for input_field in input_fields:
            input_element: WebElement = self.browser.find_element_by_id(input_field.id)
            input_element.send_keys(input_field.value)

    def __select_option(self, select_field: FritzWifiProfileSelect) -> None:
        input_select = WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, f"//td[@title='{select_field.device_name}']/..//select"))
        )
        select = Select(input_select)
        select.select_by_value(select_field.profile)

    def __click_button(self, btn: FritzButton) -> None:
        btn_element: WebElement = WebDriverWait(self.browser, 60).until(
            EC.element_to_be_clickable((btn.by_type, btn.selector))
        )
        btn_element.click()

    @property
    def browser(self) -> WebDriver:
        return self._browser

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self, host: str)-> None:
        self._host = host
