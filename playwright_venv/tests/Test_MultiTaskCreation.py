def test_task_creation (page):
    page.goto("https://deskfactor.app/")
    page.get_by_role("button", name="Sign In").click()

    page.get_by_role("textbox", name="Email").fill("shekharbabu.ahex@gmail.com")
    page.get_by_role("textbox", name="Password").fill("Password@123")
    page.get_by_role("button", name="Sign in").click()

    page.get_by_role("button", name="Projects").click()
    page.get_by_role("link", name="Test Full Project").click()

    page.get_by_role("tab", name="Tasks").click()

    # page.get_by_role("button", name="Status").click()
    # page.get_by_role("checkbox").first.click()

    page.get_by_role("button", name="Priority").click()
    page.get_by_role("checkbox").first.click()

    # for i in range(0,10): 
    #     task= f"Test Task {i}"
    #     page.get_by_role("tab", name="Tasks").click()
    #     page.get_by_role("button", name="New Task").click()

    #     page.get_by_role("textbox", name="Title *").wait_for(state="visible")
    #     page.get_by_role("textbox", name="Title *").fill(task)
    #     page.get_by_role("button", name="Create Task *").click()
