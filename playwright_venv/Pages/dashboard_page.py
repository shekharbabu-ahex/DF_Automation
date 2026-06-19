class DashboardPage:
    def __init__(self, page):
        self.dashboard = page.get_by_role("link", name ="Dashboard")
        self.my_work_view = page.get_by_role("link", name ="My Work View")
        self.projects = page.get_by_role("button", name ="Projects")
        self.view_all_projects = page.get_by_role("link", name ="View All Projects")
        self.rbac = page.get_by_role("link", name ="RBAC")
