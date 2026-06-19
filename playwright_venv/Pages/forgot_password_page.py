class ForgetPassword:
    def __init__(self, page):
        self.email = page.get_by_role("textbox", "Email")
        self.send_reset_link_button = page.get_by_role("button", "Send Reset Link")
        self.back_to_signin_button = page.get_by_role("button", "Back to Sign in")
        