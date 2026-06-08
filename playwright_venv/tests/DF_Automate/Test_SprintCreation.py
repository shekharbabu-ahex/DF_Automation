from logging import config

from playwright.sync_api import expect
from datetime import datetime
from tests.DF_Automate.config.config import Config      # Constant values for the test

ProjectName ="Tester Work Project"

#----------------------------
# LOGIN FUNCTION
#----------------------------
def login (page):
   
    page.goto(Config.URL)
    print("")
    page.evaluate("""document.body.style.zoom='75%'""")

    print("Title:", page.title())
    print("URL:", page.url)

    page.get_by_role("button", name="Sign in").click()

    page.get_by_label("Email").fill(Config.UserEmail)
    page.get_by_label("Password").fill(Config.UserPassword)

    page.get_by_role("button", name="Sign in").click()

    expect(page.get_by_text("Login successful")).to_be_visible()
    print("Login Successful")

    page.wait_for_url(Config.URL + "/dashboard")


#----------------------------
# SPRINT DRAWER OPENNNG
#----------------------------
def sprint_creation(page):
    page.get_by_role("button", name="Projects").click()
    page.get_by_role("link", name=ProjectName).first.click()

    page.get_by_role("tab", name="Sprints").click()

    page.get_by_role("button", name="Add Sprint").first.click()


#----------------------------
# FILL SPRINT DETAILS
#----------------------------
def fill_sprint_details(page):
    page.get_by_role("textbox", name="Sprint Title *").fill(Config.SprintTitle)

    page.get_by_role("combobox").click()
    page.get_by_role("option", name=Config.SprintStatus).click()

    # Start Date Selection
    page.get_by_role("button", name="Select date").first.click()

    start_date_obj = datetime.strptime(Config.SprintStartDate, "%Y-%m-%d")
    end_date_obj = datetime.strptime(Config.SprintEndDate, "%Y-%m-%d")

    start_month_year = start_date_obj.strftime("%B %Y")
    start_day = str(start_date_obj.day)
    
    end_month_year = end_date_obj.strftime("%B %Y")
    end_day = str(end_date_obj.day)

    today = datetime.today()

    # Decide navigation direction
    nav_button = (
        "Go to previous month"
        if start_date_obj.date() < today.date()
        else "Go to next month"
    )

    while True:
            current_month = page.locator('[role="presentation"]').first.text_content()

            if current_month == start_month_year:
                break

            page.get_by_role("button", name=nav_button).click()

    page.get_by_role("gridcell", name=start_day, exact=True).first.click()

    # End Date Selection
    page.get_by_text("End Date *Select date").click()

    while True:
            current_month = page.locator('[role="presentation"]').first.text_content()

            if current_month == end_month_year:
                break

            page.get_by_role("button", name=nav_button).click()

    page.get_by_role("gridcell", name=end_day, exact=True).first.click()


    page.get_by_role("spinbutton", name="Planned Capacity").fill(Config.SprintPlannedCapacity)

    page.get_by_role("textbox", name="Sprint Goal").fill(Config.SprintGoal)

    page.get_by_role("textbox", name="Additional Notes").fill(Config.SprintAdditionalNotes)


#----------------------------
# CREATE SPRINT AND ASSERT SUCCESS
#----------------------------
def create_sprint(page):
    page.get_by_role("button", name="Create Sprint").click()
    expect(page.get_by_text("Sprint created successfully")).to_be_visible()
    print("Sprint Created successfully")


#----------------------------
# VERIFY SPRINT CREATION
#----------------------------
def verify_sprint_creation(page):
    page.reload()
    page.evaluate("""document.body.style.zoom='75%'""")

    # expect(page.get_by_role("heading", name=Config.SprintTitle)).to_be_visible()
    # page.get_by_role("button", name="Upcoming").click()
    expect(page.get_by_text(Config.SprintTitle)).to_be_visible()
    print("Assertion successful, Sprint Created successfully")


#----------------------------
# MAIN TEST FUNCTION
#----------------------------
def test_sprint_creation(page):
    login(page)
    sprint_creation(page)
    fill_sprint_details(page)
    create_sprint(page)
    verify_sprint_creation(page)
