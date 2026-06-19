from playwright.sync_api import Page
from Pages.login_page import LoginPage
from Tests.DF_Automate.config import Config

def test_login(page:Page):
    login_page = LoginPage(page)

    page.goto("http://localhost:8080/login")
    login_page.user_email(Config.AdminEmail)
    login_page.user_password(Config.AdminPassword)
    login_page.login_button()
