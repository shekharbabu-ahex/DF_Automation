from playwright.sync_api import expect, sync_playwright
from Tests.DF_Automate.config.config import Config 
from Tests.DF_Automate.UserLogin import login           # Login function from UserLogin test file
from datetime import datetime

User="A_Dev_01 (Dev-002)"
Role="Administrator"
StartDate="2026-08-01"
EndDate="2026-08-15"

  
#----------------------------
# Assigning Users to Project
#----------------------------
def assign_users_to_project(admin_page):

    print("Assigning users to project in Admin Context")

    # Navigating to the created project details page and verifying the details by asserting the values in respective fields with the Actual filled Values
    admin_page.get_by_role("button", name="Projects").click()
    admin_page.get_by_role("link", name="View All Projects").click()


    # Using Search Functionality to directly navigate to the project
    admin_page.get_by_role("textbox", name="Search by project name, code or client...").clear()
    admin_page.get_by_role("textbox", name="Search by project name, code or client...").fill(Config.ProjectCode)
    expect(admin_page.get_by_role("heading", name=Config.ProjectName, exact=True)).to_be_visible()

    #Opeing the project details page by clicking on the project name in the search results
    admin_page.get_by_role("heading", name=Config.ProjectName).click()

    # Navigating to Team Tab in Project Details Page    
    admin_page.get_by_role("button", name="Project Details").click()
    admin_page.get_by_role("tab", name="Team").click()

    admin_page.get_by_role("combobox").click()
    admin_page.get_by_text("Project", exact=True).click()

    admin_page.get_by_role("button", name="Add Team Member").click()

    admin_page.get_by_role("combobox", name="Select User *").click()
    admin_page.get_by_role("option", name=User).click()

    admin_page.get_by_role("textbox", name="Role *").fill(Role)

    admin_page.get_by_role("button", name="Start Date *").click()

    user_start_date_obj = datetime.strptime(StartDate, "%Y-%m-%d")

    user_start_month_year = user_start_date_obj.strftime("%B %Y")
    user_start_day = str(user_start_date_obj.day)
    
    today = datetime.today()

    # Decide navigation direction
    nav_button = (
        "Go to previous month"
        if user_start_date_obj.date() < today.date()
        else "Go to next month"
    )
    while True:
        current_month = admin_page.locator('[role="presentation"]').first.text_content()

        if current_month == user_start_month_year:
            break

        admin_page.get_by_role("button", name=nav_button).click()     #previous

    admin_page.get_by_role("gridcell", name=user_start_day, exact=True).first.click()


    # End Date Selection
    # admin_page.get_by_role("button", name="End Date *").click()

    # user_end_date_obj = datetime.strptime(EndDate, "%Y-%m-%d")

    # user_end_month_year = user_end_date_obj.strftime("%B %Y")
    # user_end_day = str(user_end_date_obj.day)

    # today = datetime.today()

    # # Decide navigation direction
    # nav_button = (
    #     "Go to previous month"
    #     if user_end_date_obj.date() < today.date()
    #     else "Go to next month")
    
    # while True:
    #     current_month = admin_page.locator('[role="presentation"]').first.text_content()

    #     if current_month == user_end_month_year:
    #         break

    #     admin_page.get_by_role("button", name=nav_button).click()     #previous

    # admin_page.get_by_role("gridcell", name=user_end_day, exact=True).first.click()


    admin_page.get_by_role("combobox", name="Engagement Type *").click()
    admin_page.get_by_role("option", name="Full Time").click()


    admin_page.get_by_role("button", name="Assign Member").click()

    # Asserting Team Member Added Successful Popup Message
    expect(admin_page.get_by_text("Member Assigned Successfully")).to_be_visible()

    print(f"{User} assigned successfully as {Role}")

    # print(member["user"].split("(")[0].strip())

    expect(admin_page.get_by_role("paragraph").filter(has_text=User.split("(")[0].strip())).to_be_visible()

# def user_context_verification(user_page):

#     expect(user_page.get_by_text("New notification: New Project Assignment")).to_be_visible(timeout=5000)

#     user_page.get_by_role("button", name="Notifications").click()
#     expect(user_page.get_by_role("button").filter(has_text=f"You have been assigned to project: {Config.ProjectName}").first).to_be_visible()


def test_browser_context_page():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False) #, slow_mo=1000)
        admin_context = browser.new_context()
        user_context = browser.new_context()

        admin_context.tracing.start(screenshots=True, snapshots=True, sources=True)
        user_context.tracing.start(screenshots=True, snapshots=True, sources=True)

        admin_page = admin_context.new_page()
        user_page = user_context.new_page()
       
        try:
            login(admin_page, email=Config.AdminEmail, password=Config.AdminPassword)
            login(user_page, email=Config.UserEmail, password=Config.UserPassword)
            assign_users_to_project(admin_page)
            # user_context_verification(user_page)
        finally:
            admin_context.tracing.stop(path="C:/Users/shekh/OneDrive/Desktop/Playwright/playwright_venv/Traces/admin_trace.zip")
            # user_context.tracing.stop(path="C:/Users/shekh/OneDrive/Desktop/Playwright/playwright_venv/Traces/user_trace.zip")

            admin_context.close()
            user_context.close()
            browser.close()

