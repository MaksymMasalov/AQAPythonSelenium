import base64
import os
import time
import random

import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(FormPageLocators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(FormPageLocators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(FormPageLocators.EMAIL).send_keys(person.email)
        self.element_is_visible(FormPageLocators.GENDER).click()
        self.element_is_visible(FormPageLocators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(FormPageLocators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(FormPageLocators.HOBBIES).click()
        self.element_is_visible(FormPageLocators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(FormPageLocators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(FormPageLocators.SELECT_STATE).click()
        self.element_is_visible(FormPageLocators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(FormPageLocators.SELECT_CITY).click()
        self.element_is_visible(FormPageLocators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(FormPageLocators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(FormPageLocators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        # for i in result_list:
        #     result_text.append(i.text)

        return result_text
