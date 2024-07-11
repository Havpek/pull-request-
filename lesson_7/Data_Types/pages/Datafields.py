







def get_class_first_name(self):
    return self.browser.find_element(*self.class_first_name).get_attribute("class")
def get_class_last_name(self):
    return self.browser.find_element(*self.class_last_name).get_attribute("class")
def get_class_address(self):
    return self.browser.find_element(*self.class_address).get_attribute("class")
def get_class_email(self):
    return self.browser.find_element(*self.class_email).get_attribute("class")
def get_class_phone(self):
    return self.browser.find_element(*self.class_phone).get_attribute("class")
def get_class_zip_code(self):
    return self.browser.find_element(*self.class_zip_code).get_attribute("class")
def get_class_city(self):
    return self.browser.find_element(*self.class_city).get_attribute("class")
def get_class_country(self):
    return self.browser.find_element(*self.class_country).get_attribute("class")
def get_class_jobposition(self):
    return self.browser.find_element(*self.class_job_position).get_attribute("class")
def get_class_company(self):
    return self.browser.find_element(*self.class_company).get_attribute("class")



