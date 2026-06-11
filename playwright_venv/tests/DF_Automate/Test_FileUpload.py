import re
from playwright.sync_api import expect
from Tests.DF_Automate.config.config import Config
from Tests.DF_Automate.Test_UserLogin import login

def test_Attachments(page):

    login(page, email=Config.AdminEmail, password=Config.AdminPassword)

    # Navigating to View All Projects Page
    page.get_by_role("button", name="Projects").click()
    page.get_by_role("link", name="View All Projects").click()

    # Using Search Functionality to directly navigate to the project
    page.get_by_role("textbox", name="Search by project name, code or client...").clear()
    page.get_by_role("textbox", name="Search by project name, code or client...").fill(Config.ProjectCode)
    expect(page.get_by_role("heading", name=Config.ProjectName, exact=True)).to_be_visible()

    # Opeing the project details page by clicking on the project name in the search results
    page.get_by_role("heading", name=Config.ProjectName).click()

    # Navigating to Tasks Tab in Project Details Page    
    page.get_by_role("tab", name="Tasks").click()

    page.get_by_role("tab", name="Tasks").click()

    # page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    page.get_by_role("cell", name="huewihfjen").click()
    page.get_by_role("tab", name="Attachments").click()
    page.get_by_role("button", name="Upload")
    page.locator('input[type="file"]').set_input_files("C:/Users/shekh/OneDrive/Desktop/DeskFactor/TestDocs/1 MB/2 MB File.txt")
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(2000)
    expect(page.get_by_text("1 file(s) uploaded successfully")).to_be_visible()