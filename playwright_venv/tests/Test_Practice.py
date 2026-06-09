from playwright.sync_api import expect

from Tests.DF_Automate.Test_ProjCreation import verify_project_details  
from Tests.DF_Automate.UserLogin import login           # Login function from UserLogin test file

def test_practice (page):
    login (page)
    verify_project_details(page)
