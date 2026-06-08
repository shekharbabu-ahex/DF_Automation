from ast import Assert
import re

from playwright.sync_api import expect
from tests.DF_Automate.config.config import Config          # Constant values for the test
from tests.DF_Automate.UserLogin import login     # Login function from UserLogin test file

#----------------------------
# Navigation through Project
#----------------------------
def project_navigation(page):
    page.get_by_role("button", name="Projects").click()
    page.get_by_role("link", name="View All Projects").click()

    # Using Search Functionality to directly navigate to the project details page
    page.get_by_role("textbox", name="Search by project name, code or client...").fill(Config.ProjectCode)
    expect(page.get_by_role("heading", name=Config.ProjectName)).to_be_visible()
    print("Project Search Successful")

    # Opeing the project details page by clicking on the project name in the search results
    page.get_by_role("heading", name=Config.ProjectName).click()

    # Navigating to Tasks Tab in Project Details Page
    page.get_by_role("tab", name="Tasks").click()
    print("Navigated to Tasks Tab in Project Details Page")


#----------------------------
# Manual Task Creation
#----------------------------
def manual_task_creation(page):

    Assert (page.get_by_role("button", name="New Task").is_visible(), "New Task button is not visible")
    page.get_by_role("button", name="New Task").click()

    page.get_by_role("heading", name="Add New Task").wait_for(state="visible")

    page.get_by_role("textbox", name="Title *").fill(Config.TaskTitle)
    page.get_by_role("paragraph").first.click()
    page.locator(".tiptap").first.fill(Config.TaskDescription)

    page.get_by_role("paragraph").filter(has_text=re.compile(r"^$")).click()
    page.locator(".tiptap.ProseMirror.focus\\:outline-none.min-h-\\[70px\\].px-3.py-2.ProseMirror-focused").fill(Config.TaskAcceptanceCriteria)
	
    page.get_by_role("combobox", name="Type *").click()
    page.get_by_role("option", name=Config.TaskType).click()

    page.get_by_role("combobox", name="Priority").click()
    page.get_by_role("option", name=Config.TaskPriority).click()

    page.get_by_role("combobox", name="Assigned To").click()
    page.get_by_role("option", name=Config.TaskAssignee).click()

    # page.get_by_role("combobox", name="Reviewer").click()
    # page.get_by_role("option", name=Config.TaskReviewer).click()

    page.get_by_role("button", name="Create Task").click()
    expect(page.get_by_text("Task created successfully")).to_be_visible()
    print("Manual Task Creation Successful")

    
#----------------------------
# Bulk Uploading Tasks
#----------------------------
def bulk_upload(page):
    page.get_by_role("button", name="Bulk Upload").click()

    # page.get_by_role("dialog", name="Bulk Upload Tasks").set_input_files(Config.TaskBulkUploadFilePath)
    page.locator('input[type="file"]').set_input_files(Config.TaskBulkUploadFilePath)
    print("File Uploaded Successfully")

    page.get_by_role("button", name="Upload & Parse").click()
    print("Parsed")

    page.get_by_role("button", name="Confirm import").click()
    print("Confirm Upload")

#----------------------------
# Upload Verification
#----------------------------
def bulk_upload_verification(page):
    expect(page.get_by_text("Task import started. Track progress in the Notifications panel.")).to_be_visible(timeout=120000)
    print("Task Import Start Message Verified")
    expect(page.get_by_text("Task import completed.")).to_be_visible(timeout=120000)
    print("Task Import Completed Message Verified")

    # page.get_by_text("Task import started. Track progress in the Notifications panel.").wait_for(state="visible", timeout=240000)

    # page.get_by_text("Task import completed.").wait_for(state="visible", timeout=240000)


    page.get_by_role("button", name="Notifications").click()
    page.get_by_role("tab", name="Imports").click()

    expect(page.get_by_role("button", name="Task Import Completed Task")).to_be_visible()
    page.get_by_role("button", name="Task Import Completed Task").click()
    page.get_by_role("heading", name="All test cases imported").click()
    page.get_by_role("button", name="Close").first.click()
    
    # page.wait_for_timeout
    # page.get_by_role("button", name="View tasks").wait_for(state="visible", timeout=240000)
    # page.get_by_role("button", name="View tasks").click()
    print("Upload Successful")

#----------------------------
# Test Execution
#----------------------------

def test_task_bulk_upload(page):
    login (page)
    project_navigation(page)
    # manual_task_creation(page)
    bulk_upload(page)
    bulk_upload_verification(page)
