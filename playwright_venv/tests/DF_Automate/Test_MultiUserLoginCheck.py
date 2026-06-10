from Tests.DF_Automate.config.config import Config

def test_users_login_check(page):

    # Application URL and Login
    page.goto(Config.DevURL)
    page.evaluate("""document.body.style.zoom='75%'""")
    print("")
    print("Page URL Is: ", page.url)
    print("Page Title Is:", page.title())

    # Navigating to Sign in Page
    page.get_by_role("button", name="Sign In").click()

    # Users Credentials List
    user_list_emails=["admin@acm.com", "pm@acm.com", "dev@acm.com", "tester@acm.com"] #, "tl@acm.com"]
    user_list_passwords=["Password@4567", "Password@456", "Password@1234", "Password@456"] #, "password123"]
    UserCount = len(user_list_emails)
    print("")

    for i in range(0, UserCount):
        page.wait_for_timeout(2000)
        page.evaluate("""document.body.style.zoom='75%'""")

         # Filling Credentials
        page.get_by_label("Email").fill(user_list_emails[i])
        page.get_by_label("Password").fill(user_list_passwords[i])

        # Clicking Sign in Button
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_timeout(2000)

        Message = page.get_by_role("region", name="Notifications alt+T").get_by_role("listitem").inner_text()

        if Message == "Login successful":
            print(f"Login Successful For User: {user_list_emails[i]} With Message: {Message} ")
        
        elif Message == "Username/Password is incorrect!":
            print(f"Login Failed For User: {user_list_emails[i]} With Message: {Message} ")
            page.get_by_label("Email").clear()
            page.get_by_label("Password").clear()
            continue

        # Clicking on Profil Icon
        page.get_by_role("button", name="AC", exact=True).click()

        # Clicking on logout button
        page.get_by_role("menuitem", name="Log out").click()

    print(f"Login Tested For {UserCount} Users Successfully")