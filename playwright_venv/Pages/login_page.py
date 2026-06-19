import re

class LoginPage:

    def __init__(self, page):
        # self.page = page
        self.user_email = page.get_by_label("Email")
        self.user_password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Sign in")
        self.remember_me_checkbox = page.get_by_role("checkbox", name="Remember me")
        self.forgot_password_button = page.get_by_role("link", name="Forgot password?")
        self.signup_button = page.get_by_role("button", name="Sign up")
        self.see_password = page.get_by_role("button").filter(has_text=re.compile(r"^$"))

    def login(self, email, password):
        self.user_email.fill(email)
        self.user_password.fill(password)
        self.see_password.click()
        self.login_button.click()
        # self.remember_me_checkbox.click()
        # self.forgot_password_button.click()
        # self.signup_button.click()

