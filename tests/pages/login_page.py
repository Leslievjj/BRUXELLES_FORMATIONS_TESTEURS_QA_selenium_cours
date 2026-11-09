from selenium import webdriver
from tests.config import BASE_URL
from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "input[type=email]")
    PASSWORD = (By.CSS_SELECTOR, "input[type=password]")
    SUBMIT = (By.CSS_SELECTOR, "form .btn-primary")
    ERREUR = (By.CSS_SELECTOR, ".notice-err")

    def ouvrir(self):
        self.driver.get(BASE_URL + "/login")
        self.wait.until(EC.visibility_of_element_located(self.EMAIL))
        return self

    def soumettre(self, email: str, password: str):
        self.saisir(self.EMAIL, email)
        self.saisir(self.PASSWORD, password)
        self.cliquer(self.SUBMIT)
        return self

    def se_connecter(self, email: str, password: str):
        self.soumettre(email, password)
        self.trouver(self.DECONNEXION)
        return self

    def message_erreur(self):
        # attend le message et renvoie son texte
        return self.trouver(self.ERREUR).text
        

# Ne lance pas les focntions si on import seulement login page
if __name__ == "__main__":
    my_driver = webdriver.chrome()

    page = LoginPage(my_driver)
    page.ouvrir().saisir(page.EMAIL, 'orga@eventflow.com')
    page.saisir(page.EMAIL, 'orga@eventflow.com')
