import time

from pages.forms_page import FormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open_url()
            person = form_page.fill_form_fields()
            result = form_page.form_result()
            assert f"{person.firstname} {person.lastname}" == result[0], "the form has not been filled"
            assert person.email == result[1], "the form has not been filled"
