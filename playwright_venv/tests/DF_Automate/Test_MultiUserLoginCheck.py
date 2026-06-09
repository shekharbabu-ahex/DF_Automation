def test_navigation(page):
    
    # URL Opening
    URL="http://localhost:8080"
    page.goto(URL)
    print("")
    print("Page URL Is: ", page.url)
    print("Page Title Is:", page.title())

    # Navigating to Sign in Page
    page.get_by_role("button", name="Sign In").click()


    user_list_emails=["admin@acm.com", "pm@acm.com", "dev@acm.com", "tester@acm.com", "tl@acm.com"]
    user_list_passwords=["Password@123", "Password@123", "Password@123", "password123", "password123"]
    print("")

    for i in range(0,5):
         # Filling Credentials
        page.get_by_label("Email").fill(user_list_emails[i])
        page.get_by_label("Password").fill(user_list_passwords[i])

        # Clicking Sign in Button
        page.get_by_role("button", name="Sign in").click()

        error_msg = page.get_by_text("Username or Password is incorrect.")
        dashboard = page.get_by_role("heading", name="Dashboard")  # change if needed

        if error_msg.is_visible():
            print("Login failed:", error_msg.inner_text())
            continue
            # Waiting for Dashboard Page
        
        page.wait_for_url(f"{URL}/dashboard")

        # Asserting Login Successful Popup Message
        assert page.get_by_role("region", name="Notifications alt+T").get_by_role("listitem").is_visible()
    
        # Printing Success login popup message
        print(page.get_by_role("region", name="Notifications alt+T").get_by_role("listitem").inner_text())
    
        # Clicking on Profil Icon
        page.get_by_role("button", name="AC", exact=True).click()

        print("User Name: ",page.locator(".text-sm.font-medium.leading-none.text-foreground").inner_text())
        # page.get_by_text("Acme Corporation Administrator").click()

        #Clicking on logout button
        page.get_by_role("menuitem", name="Log out").click()
        print("")

    print("All Users Login Tested")