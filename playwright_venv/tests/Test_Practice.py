from playwright.sync_api import expect
from tests.DF_Automate.config.config import Config     # Constant values for the test
from tests.DF_Automate.UserLogin import login       # Login function from UserLogin test file

def test_practice (page):

    login (page)
    verify_project_details(page)
    # URL="https://the-internet.herokuapp.com/upload"
    # "https://the-internet.herokuapp.com/javascript_alerts"
    # URL="http://localhost:8081"
    # UserEmail="dev@acm.com"
    # UserPassword="Password@123"
    # ProjectName ="test project 2"
    
    # page.goto(URL)
    # print("")

    # # page.evaluate("""document.body.style.zoom='75%'""")

    # print(page.title())
    # print(page.url)


# ----------------------------
# Verify Project Details
# ----------------------------
def verify_project_details(page):

    # Navigating to the created project details page and verifying the details by asserting the values in respective fields with the constant values from config file
    page.get_by_role("button", name="Projects").click()
    page.get_by_role("link", name="View All Projects").click()

    # Using Search Functionality to directly navigate to the project details page
    page.get_by_role("textbox", name="Search by project name, code or client...").fill(Config.ProjectCode)
    expect(page.get_by_text(Config.ProjectCode)).to_be_visible()
    print("Project Search Successful")

    page.get_by_role("heading", name=Config.ProjectName).click()

    page.get_by_role("button", name="Project Details").click()
    page.get_by_role("tab", name="Documents").click()

    page.get_by_role("button", name="Upload Document").set_input_files(Config.ProjectDocumentPath)
    print("Document Uploaded Successfully")

    # Hovering on the project row to make the action buttons visible and clicking on "Edit Project" button to navigate to the project details page
    # project_row = page.locator("tr").filter(has_text=Config.ProjectCode)

    
    # page.on("dialog", lambda dialog: (print("Message:",dialog.type), dialog.accept()))

        
    # page.get_by_role("button", name="Click for JS Confirm").click()

    # page.get_by_role("button", name="Sign in").click()

    # page.get_by_label("Email").fill(UserEmail)
    # page.get_by_label("Password").fill(UserPassword)
    # page.on("dialog", lambda dialog: (print(dialog.message), dialog.accept()))

    # page.get_by_role("button", name="Sign in").click()
    # page.on("dialog", lambda dialog: print(dialog.message))


    # page.get_by_role("button", name="Projects").click()
    # page.get_by_role("link", name=ProjectName, exact=True).click()
    # page.get_by_role("tab", name="Tasks").click()

    # page.get_by_role("button", name="Bulk Upload").click()
    # # page.get_by_text("CSV").click()
    # page.get_by_role("dialog", name="Bulk Upload Tasks").click()
    # # page.get_by_role("dialog", name="Bulk Upload Tasks").set_input_files("C:\Users\shekh\OneDrive\Desktop\DeskFactor\TestDocs\Tasks Bulk Upload\Task Bulk Upload Test CSV.csv")

    # file_path = r'C:\Users\shekh\OneDrive\Desktop\DeskFactor\TestDocs\Tasks Bulk Upload\Task Bulk Upload Test CSV.csv'
    # page.locator('input[type="file"]').set_input_files(file_path)
    # print("File Uploaded Successfully")

    # page.get_by_role("button", name="Upload & Parse").click()
    # print("Parsed")

    # page.get_by_role("button", name="Confirm import").click()
    # print("Confirm Uplaod")

    # page.get_by_role("button", name="View tasks").click()
    # print("Uplaod Successful")




    # page.wait_for_url("***/dashboard***")
    # # Asserting Login Successful Popup Message
    # expect (page).to_have_url("http://localhost:8081/dashboard")
    # print("Assertion Done")
    
    # page.get_by_role("button", name="Projects").click()

    # page.get_by_role("link", name="Project 2", exact=True).click()

    # print(page.title())

    # page.get_by_role("link", name="Project 2", exact=True).click()

    # expect (page.get_by_role("heading", name = "Project 2 (PRJ3239)")).to_be_visible()

    # expect (page.get_by_role("main")).to_contain_text("Project 2 (PRJ3239)") #, "Wrong project"

    # assert page.title() == ("AI Research Project (AI006)"), "Wrong Project Name"
    
    # expect(page.get_by_role("main")).to_contain_text("AI Research Project (AI006)")

    # assert "Project 2 (AI006)" in page.get_by_role("main").inner_text(), "Wrong project"

    # expect(page.get_by_role("main")).to_contain_text("AI Research Project (AI006)")