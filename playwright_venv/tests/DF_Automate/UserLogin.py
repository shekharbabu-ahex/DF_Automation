from tests.DF_Automate.config.config import Config      # Constant values for the test
from playwright.sync_api import expect

# ----------------------------
# User Login Function
# ----------------------------
def login (page):
        
    page.goto(Config.DevURL)
    print("Application Opened")
    page.evaluate("""document.body.style.zoom='75%'""")

    print("Page URL:", page.url)
    print("Page Title:", page.title())

    page.get_by_role("button", name="Sign in").click()
    print("Page URL:", page.url)

    expect(page).to_have_url(Config.DevURL + "/login")
    print("Assertion Successful, Navigated to Login Page")

    page.get_by_label("Email").fill(Config.UserEmail)
    page.get_by_label("Password").fill(Config.UserPassword)

    page.get_by_role("button", name="Sign in").click()
    
    # Asserting successful login
    expect(page.get_by_text("Login successful")).to_be_visible()    
    page.wait_for_url(Config.DevURL + "/dashboard")
    print("Assertion Successful, Login Successful")