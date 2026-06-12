import random

PRJCODE=random.randint(1, 1000)
SPRINTCODE=random.randint(1, 100)

class Config:

    DevURL = "http://localhost:8080"
    AdminEmail ="shekharbabu.ahex@gmail.com"
    AdminPassword ="Password@123"
    UserEmail ="test_dev2@yopmail.com"
    UserPassword ="Password@456"
    ProjectName = "RBAC check" #f"Auto Project Test {PRJCODE}"    # "Tester Work Project" 
    ProjectCode = "PRJ4129" #f"PRJ{PRJCODE}"    # "PRJ3837" 
    ProjectType ="Client"   # Internal, Client, Research, Maintenance
    ProjectManager ="PM 01 (TEC002)"
    ProjectStartDate ="2025-08-01"
    ProjectStatus = "On Hold"     # On Hold, Cancelled, Completed, Active, Draft
    BillingModel = "Fixed Price"    # Fixed Price, Time & Material, Hourly, Milestone, N/A
    BudgetEstimate = "100000"
    ProjectDocumentPath = r'C:\Users\shekh\OneDrive\Desktop\DeskFactor\TestDocs\1 Excel Template.xls'

    MembersList = [
                    # {"user": "A_Admin_01", "role": "Administrator", "start_date": "2026-08-01", "end_date": "2028-08-01"},
                    # {"user": "A_PM_02 (PM-002)","role": "Developer", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test Dev 09 (dev-009)","role": "Dev", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test_Dev 10 (EMP010)","role": "Developer", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "user long email (@#$%)","role": "PM", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test User 03 Z (EMP009)","role": "PM", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test User 04 (EMP007)","role": "QA", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test User 05 (ACM001)","role": "Developer", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test User 6","role": "Client", "start_date": "2026-08-01", "end_date": "2026-08-01"},
                    {"user": "Test User 09 (EMP006)","role": "Developer", "start_date": "2026-08-01", "end_date": "2026-08-01"},

                    # {"user": "PM 01 (PM001)","role": "PM"},
                    # {"user": "Tester 01 (TEC005)","role": "Tester", "start_date": "2027-08-01", "end_date": "2027-01-01"}
                    ]

    SprintTitle = f"Auto Sprint {SPRINTCODE}"
    SprintStartDate="2027-05-11"
    SprintEndDate="2027-06-11"
    SprintStatus="Planning"         #Planning, Completed, Cancelled
    SprintPlannedCapacity="100"
    SprintGoal="This is an automated sprint created by Playwright Python script"
    SprintAdditionalNotes="These are additional notes for the sprint, added by Playwright Python script"


    TaskTitle = "This is a task created by Playwright Python Script"
    TaskDescription = "This is a description for the task created by Playwright Python Script"
    TaskAcceptanceCriteria = "These are acceptance criteria for the task created by Playwright Python Script"
    TaskType = "Change Request"          # Task, change request, Enhancement, Story, Spike
    TaskPriority = "High"                # Low, Medium, High, Critical
    TaskAssignee = "PM 01"
    # TaskReviewer = "Test_Tester2"
    TaskBulkUploadFilePath = r'C:\Users\shekh\OneDrive\Desktop\DeskFactor\TestDocs\Tasks Bulk Upload\Task Bulk Upload 100 Test  CSV.csv'
