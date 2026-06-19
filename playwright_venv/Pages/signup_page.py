from playwright.sync_api import expect

class SignUp:
    def __init__(self, page):
        
        self.sign_up_button = page.get_by_role("button", name="Sign up")
        self.pricing_page_button = page.get_by_role("link", name="Back to Pricing")

        self.company_name = page.get_by_role("textbox", name="Company Name")
        self.admin_name = page.get_by_role("textbox", name="Admin Name")
        self.work_email = page.get_by_role("textbox", name="Work Email")
        self.password = page.get_by_role("textbox", name="Password Confirm Password")
        self.see_password = page.get_by_role("button").nth(1)
        self.confirm_password = page.get_by_role("textbox", name="Create a strong password")
        self.see_confirm_password = page.get_by_role("button").nth(2)
        self.mobile_number = page.get_by_role("textbox", name="Mobile Number (Optional)")
        self.plan_switch_toggle = page.locator(".block")
        self.check_TandC = page.get_by_role("checkbox", name="I agree to the Terms of")
        self.create_workspace_button = page.get_by_role("button", name="Create Workspace")
        
        expect(page.get_by_role("heading", name="Create Your Workspace")).to_be_visible
