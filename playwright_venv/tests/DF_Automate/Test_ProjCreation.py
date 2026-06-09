import re
from playwright.sync_api import expect
from datetime import datetime

from Tests.DF_Automate.config.config import Config      # Constant values for the test
from Tests.DF_Automate.UserLogin import login
from Tests.DF_Automate.conftest import page           # Login function from UserLogin test file

# ----------------------------
# Open Project Drawer
# ----------------------------
def open_new_project_drawer(page):

    # Navigating to Projects Tab And Checking if user has permission to create project by asserting the presence of "Add New Project" button
    page.get_by_role("button", name="Projects").click()
    page.get_by_role("link", name="View All Projects").click()
    expect(page.get_by_role("button", name="Add New Project")).to_be_visible()
    print("Assertion Successful, User has a Permission To Create New Project")

    # Clicking on "Add New Project" button and asserting the presence of "Create New Project" text to confirm that project creation drawer is opened
    page.get_by_role("button", name="Add New Project").click()
    expect(page.get_by_text("Create New Project")).to_be_visible()
    print("Assertion successful, Project Drawer Opened")


# ----------------------------
# Fill Project Details
# ----------------------------

def fill_project_details(page):

    # Filling the project details in the project creation drawer using the constant values from config file
    page.get_by_role("textbox", name="Project Name *").fill(Config.ProjectName)
    page.get_by_role("textbox", name="Project Code").fill(Config.ProjectCode)
    page.get_by_role("combobox", name="Project Manager *").click()
    page.get_by_text(Config.ProjectManager, exact=True).click()
    page.get_by_role("button", name="Start Date *").click()

    date_obj = datetime.strptime(Config.ProjectStartDate, "%Y-%m-%d")

    target_proj_month_year = date_obj.strftime("%B %Y")
    target_Proj_day = str(date_obj.day)

    today = datetime.today()

    # Decide navigation direction
    nav_button = (
        "Go to previous month"
        if date_obj.date() < today.date()
        else "Go to next month"
    )

    while True:
        current_month = page.locator('[role="presentation"]').first.text_content()

        if current_month == target_proj_month_year:
            break

        page.get_by_role("button", name=nav_button).click()

    page.get_by_role("gridcell", name=target_Proj_day, exact=True).first.click()

    page.get_by_role("combobox", name="Project Type *").click()
    page.get_by_role("option", name=Config.ProjectType).click()

    page.get_by_role("combobox", name="Project Status *").click()
    page.get_by_role("option", name=Config.ProjectStatus).click()


    page.get_by_role("combobox", name="Billing Model").click()
    page.get_by_role("option", name=Config.BillingModel).click()

    page.get_by_placeholder("e.g., 50,000").fill(Config.BudgetEstimate)

    print("Project details filled successfully")


# ----------------------------
# Submit Project
# ----------------------------
def submit_project(page):

    # Clicking on "Create Project" button and asserting the presence of success message to confirm that project is created successfully
    page.get_by_role("button", name="Create Project").click()

    # Asserting Project Creation Successful Toast Message
    expect(page.get_by_text("Your project has been successfully created.")).to_be_visible()
    print("Assertion successful, Project Created successfully")


# ----------------------------
# Verify Project Creation
# ----------------------------
def verify_project_creation(page):
    
    # Confirming Project Creation by Asserting the presence of Project Name in Top Of Projects List
    page.get_by_role("button", name="Projects").click()
    expect(page.get_by_text(Config.ProjectName, exact=True)).to_be_visible()
    print("Assertion successful, Project is visible in Top Of The Projects List")


# ----------------------------
# Verify Project Details
# ----------------------------
def verify_project_details(page):

    # Navigating to the created project details page and verifying the details by asserting the values in respective fields with the Actual filled Values
    page.get_by_role("button", name="Projects").click()
    page.get_by_role("button", name="Projects").screenshot(path="C:/Users/shekh/OneDrive/Desktop/Playwright/playwright_venv/Screenshots/projects_list.png")
    page.get_by_role("link", name="View All Projects").click()

    # Using Search Functionality to directly navigate to the project details page
    page.get_by_role("textbox", name="Search by project name, code or client...").fill(Config.ProjectCode)
    expect(page.get_by_role("heading", name=Config.ProjectName, exact=True)).to_be_visible()
    print("Project Search Successful")

    # Hovering on the project row to make the action buttons visible and clicking on "Edit Project" button to navigate to the project details page
    project_row = page.locator("tr").filter(has_text=Config.ProjectCode)
    project_row.hover()
    project_row.locator("button").last.click()
    page.get_by_role("menuitem", name="Edit Project").click()

    page.screenshot(path="C:/Users/shekh/OneDrive/Desktop/Playwright/playwright_venv/Screenshots/test_project_details.png")
    # Asserting the values in respective fields with the constant values from config file
    expect(page.get_by_role("textbox",name="Project Name *")).to_have_value(Config.ProjectName)
    expect(page.get_by_role("textbox",name="Project Code")).to_have_value(Config.ProjectCode)
    expect(page.get_by_role("combobox",name="Project Type *")).to_contain_text(Config.ProjectType)
    expect(page.get_by_role("combobox",name="Project Status *")).to_contain_text(Config.ProjectStatus)
    expect(page.get_by_role("combobox",name="Billing Model")).to_contain_text(Config.BillingModel)

    print("All project details verified successfully")

    # Closing the project details drawer
    page.get_by_role("button", name="Close").click()

#----------------------------
# Assigning Users to Project
#----------------------------
def assign_users_to_project(page):

    # Using Search Functionality to directly navigate to the project
    page.get_by_role("textbox", name="Search by project name, code or client...").clear()
    page.get_by_role("textbox", name="Search by project name, code or client...").fill(Config.ProjectCode)
    expect(page.get_by_role("heading", name=Config.ProjectName, exact=True)).to_be_visible()

    #Opeing the project details page by clicking on the project name in the search results
    page.get_by_role("heading", name=Config.ProjectName).click()

    # Navigating to Team Tab in Project Details Page    
    page.get_by_role("button", name="Project Details").click()
    page.get_by_role("tab", name="Team").click()

    page.get_by_role("combobox").click()
    page.get_by_text("Project", exact=True).click()
    
    # Assigning users to project
    for member in Config.MembersList:

        page.get_by_role("button", name="Add Team Member").click()

        page.get_by_role("combobox", name="Select User *").click()
        page.get_by_role("option", name=member["user"]).click()

        page.get_by_role("textbox", name="Role *").fill(member["role"])
   
        page.get_by_role("button", name="Start Date *").click()

        # date_obj = datetime.strptime(member["start_date"], "%Y-%m-%d")

        # user_target_month_year = date_obj.strftime("%B %Y")
        # user_target_day = str(date_obj.day)

        user_start_date_obj = datetime.strptime(Config.member["start_date"], "%Y-%m-%d")

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
            current_month = page.locator('[role="presentation"]').first.text_content()

            if current_month == user_start_month_year:
                break

            page.get_by_role("button", name=nav_button).click()     #previous

        page.get_by_role("gridcell", name=user_start_day, exact=True).first.click()



        page.get_by_role("button", name="End Date *").click()

        # date_obj = datetime.strptime(member["end_date"], "%Y-%m-%d")

        # target_month_year = date_obj.strftime("%B %Y")
        # target_day = str(date_obj.day)

        user_end_date_obj = datetime.strptime(Config.member["end_date"], "%Y-%m-%d")

        user_end_month_year = user_end_date_obj.strftime("%B %Y")
        user_end_day = str(user_end_date_obj.day)

        today = datetime.today()


        # Decide navigation direction
        nav_button = (
            "Go to previous month"
            if user_end_date_obj.date() < today.date()
            else "Go to next month"
        )
        while True:
            current_month = page.locator('[role="presentation"]').first.text_content()

            if current_month == user_end_month_year:
                break

            page.get_by_role("button", name=nav_button).click()     #previous

        page.get_by_role("gridcell", name=user_end_day, exact=True).first.click()


        page.get_by_role("combobox", name="Engagement Type *").click()
        page.get_by_role("option", name="Full Time").click()


        page.get_by_role("button", name="Assign Member").click()

        # Asserting Team Member Added Successful Popup Message
        expect(page.get_by_text("Member Assigned Successfully")).to_be_visible()

        print(f"{member['user']} assigned successfully as {member['role']}")

        # print(member["user"].split("(")[0].strip())

        expect(page.get_by_role("paragraph").filter(has_text=member["user"].split("(")[0].strip())).to_be_visible()

# ----------------------------
# Main Test
# ----------------------------

def test_project_creation(page):
    login (page)
    # open_new_project_drawer(page)
    # fill_project_details(page)
    # submit_project(page)
    # verify_project_creation(page)
    verify_project_details(page)
    assign_users_to_project(page)