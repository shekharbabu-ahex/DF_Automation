from playwright.sync_api import expect

from tests.DF_Automate.Test_ProjCreation import verify_project_details  
from tests.DF_Automate.config.config import Config      # Constant values for the test
from tests.DF_Automate.UserLogin import login           # Login function from UserLogin test file

def test_practice (page):


    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    login (page)
    # page.screenshot(path="C:/Users/shekh/OneDrive/Desktop/Playwright/playwright_venv/Screenshots/test_practice_login.png")
    print ("Login Screenshot Successfully Saved At: Screenshots/test_practice_login.png")
    verify_project_details(page)

    # page.context.tracing.stop(
    #     path=r"C:\Users\shekh\OneDrive\Desktop\Playwright\playwright_venv\Traces\test_practice_trace.zip")

