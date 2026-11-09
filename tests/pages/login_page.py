from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.config import BASE_URL
from selenium.webdriver import Keys

class LoginPage:
    EMAIL = (By.CSS_SELECTOR, "input[type=email]")
    PASSWORD = (By.CSS_SELECTOR, "input[type=password]")
    SUBMIT = (By.CSS_SELECTOR, "form .btn-primary")
    ERREUR = (By.CSS_SELECTOR, ".notice-err")
    DECONNEXION = (By.XPATH, "//button[normalize-space()='Deconnexion']")

    # Constructeur, executé à la création d'une instance de 'LoginPage'
    def __init__(self, driver: "webdriver.Chrome"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def ouvrir(self):
        self.driver.get(BASE_URL + "/login")
        self.wait.until(EC.visibility_of_element_located(self.EMAIL))
        return self

    def saisir(self, locator: tuple[str, str], text: str):
        champ = self.wait.until(EC.visibility_of_element_located(locator))
        champ.clear()
        champ.send_keys(Keys.CONTROL, "a")
        champ.send_keys(Keys.DELETE)
        champ.send_keys(text)
        return self

    def cliquer(self, locator: tuple[str, str]):
        # attend qu'un élément soit cliquable et clique
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def trouver(self, locator: tuple[str, str]):
        # attend qu'un élément soit visible et le renvoie
        return self.wait.until(EC.visibility_of_element_located(locator))

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
