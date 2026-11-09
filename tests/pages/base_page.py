from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Barre de navigation et titre, présents sur toutes les pages du back-office
    LIEN_BACK_OFFICE = (By.PARTIAL_LINK_TEXT, "Back-office")
    DECONNEXION = (By.XPATH, "//button[normalize-space()='Deconnexion']")
    TITRE = (By.CSS_SELECTOR, "h1.page-title")

    def __init__(self, driver: "webdriver.Chrome"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- actions élémentaires ---------------------------------------------
    def attendre(self, condition):
        """Attend que la condition soit vraie et renvoie son résultat."""
        return self.wait.until(condition)

    def trouver(self, locator):
        """Attend qu'un élément soit visible et le renvoie."""
        return self.attendre(EC.visibility_of_element_located(locator))

    def cliquer(self, locator):
        """Attend qu'un élément soit cliquable, puis clique dessus."""
        self.attendre(EC.element_to_be_clickable(locator)).click()

    def saisir(self, locator: tuple[str, str], text: str):
        champ = self.wait.until(EC.visibility_of_element_located(locator))
        champ.clear()
        champ.send_keys(Keys.CONTROL, "a")
        champ.send_keys(Keys.DELETE)
        champ.send_keys(text)
        return self

    def texte(self, locator):
        """Renvoie le texte d'un élément visible."""
        return self.trouver(locator).text

    def champ(self, libelle):
        """Renvoie le locator du champ placé juste après un label."""
        return (By.XPATH, f"//label[normalize-space()='{libelle}']/following-sibling::input")

    # --- barre de navigation ------------------------------------------------
    def aller_au_back_office(self):
        """Clique sur le lien Back-office et attend le titre de la page."""
        self.cliquer(self.LIEN_BACK_OFFICE)
        self.attendre(EC.url_contains("/admin"))
        self.trouver(self.TITRE)
        return self

    def a_le_lien_back_office(self):
        """Indique si le lien Back-office est affiché (sans attendre)."""
        return self.driver.find_elements(*self.LIEN_BACK_OFFICE) != []


    def titre(self):
        """Renvoie le titre de la page."""
        return self.texte(self.TITRE)
