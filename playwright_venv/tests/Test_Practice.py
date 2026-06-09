from playwright.sync_api import expect
from tests.DF_Automate.config.config import Config     # Constant values for the test
from tests.DF_Automate.UserLogin import login       # Login function from UserLogin test file

def test_practice (page):

    login (page)