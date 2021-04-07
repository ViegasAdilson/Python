from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.drive_path="chromedriver"
        self.opcao = webdriver.ChromeOptions()
        self.opcao.add_argument("user-data-dir=Perfil")
        self.chrome = webdriver.Chrome(
            self.drive_path,
            options=self.opcao
        )

    def acessar(self, site):
        self.chrome.get(site)

    def clica_sing(self):
        try:
            btn_sign = self.chrome.find_element_by_link_text("Sign in")
            btn_sign.click()
        except Exception as e:
            print("Erro ao clicar no Botao:", e)

    def fazerLogin(self):
        try:
            input_login= self.chrome.find_element_by_id("login_field")
            input_password= self.chrome.find_element_by_id("password")
            btn_login = self.chrome.find_element_by_name("commit")

            input_login.send_keys("adilsonviegas@hotmail.com")
            input_password.send_keys("4di150n")
            sleep(5)
            btn_login.click()
        except Exception as e:
            print("erro ao fazer Login:", e)

    def clicar_perfil(self):
        try:
            btn_perfil = self.chrome.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details")
            btn_perfil.click()
        except Exception as e:
            print("Erro ao clicar no perfil:", e)

    def clicar_out(self):
        try:
            btn_out = self.chrome.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button")
            btn_out.click()
        except Exception as e:
            print("Erro ao clicar no out:", e)

    def verificar(self, usuario):
        perfil_link = self.chrome.find_element_by_class_name("user-profile-link")
        perfil_link_html = perfil_link.get_attribute("innerHTML")
        assert usuario in perfil_link_html

    def sair(self):
        self.chrome.quit()


if __name__ == "__main__":
    chome = ChromeAuto()

    chome.acessar("https://github.com/")
    chome.clica_sing()
    chome.fazerLogin()
    chome.clicar_perfil()
    chome.verificar("ViegasAdilson")
    chome.clicar_out()
    sleep(30)
    chome.sair()