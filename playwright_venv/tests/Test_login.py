import pytest
from playwright.sync_api import Page, expect

URL = "http://localhost:8081"

valid_users = [
    ("admin@acm.com", "Password@123"),
    ("pm@acm.com", "Password@123"),
]

@pytest.mark.parametrize("email,password", valid_users)
def test_valid_login(page: Page, email: str, password: str):
    page.goto(URL)
    page.get_by_role("button", name="Sign In").click()

    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()

    expect(page).to_have_url(f"{URL}/dashboard")
    # expect(page.get_by_role("heading", name="Admin Dashboard")).to_be_visible()

    # Asserting Login Successful Popup Message
    assert page.get_by_role("region", name="Notifications alt+T").get_by_role("listitem").is_visible()
    
def test_invalid_login_wrong_password(page: Page):
    page.goto(URL)
    page.get_by_role("button", name="Sign In").click()

    page.get_by_label("Email").fill("admin@acm.com")
    page.get_by_label("Password").fill("WrongPassword")
    page.get_by_role("button", name="Sign in").click()

    expect(page.get_by_text("Username or Password is incorrect.")).to_be_visible()