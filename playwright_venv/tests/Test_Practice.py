# from playwright.sync_api import page
from Pages.login_page import LoginPage
from Tests.DF_Automate.config.config import Config

def test_login(page):
    fn_page = LoginPage(page)

    page.goto("http://localhost:8080/login")
    page.evaluate("""document.body.style.zoom='75%'""")
    # login_page.login(Config.AdminEmail, Config.AdminPassword)
    fn_page.forgot_password_button.click()
    page.reload()

