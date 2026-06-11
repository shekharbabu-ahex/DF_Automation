import random

PRJCODE=random.randint(1, 1000)
SPRINTCODE=random.randint(1, 100)

class Config:

    DevURL = "http://localhost:8080"
    AdminEmail ="shekharbabu.ahex@gmail.com"
    AdminPassword ="Password@123"
    UserEmail ="test_dev2@yopmail.com"
    UserPassword ="Password@456"
    ProjectName = "Status Test Project" #f"Auto Project Test {PRJCODE}"    # "Tester Work Project" 
    ProjectCode = "PRJ1884" #f"PRJ{PRJCODE}"    # "PRJ3837" 
    ProjectType ="Client"   # Internal, Client, Research, Maintenance
    ProjectManager ="PM 01 (TEC002)"
    ProjectStartDate ="2025-08-01"
    ProjectStatus = "On Hold"     # On Hold, Cancelled, Completed, Active, Draft
    BillingModel = "Fixed Price"    # Fixed Price, Time & Material, Hourly, Milestone, N/A
    BudgetEstimate = "100000"
    ProjectDocumentPath = r'C:\Users\shekh\OneDrive\Desktop\DeskFactor\TestDocs\1 Excel Template.xls'

    MembersList = [
                    {"user": "Admin 01 (TEC001)", "role": "Administrator", "start_date": "2027-08-01", "end_date": "2028-08-01"},
                    {"user": "Dev 01 (TEC004)","role": "Developer", "start_date": "2026-08-01", "end_date": "2027-08-01"},
                    # {"user": "PM 01 (PM001)","role": "PM"},
                    {"user": "Tester 01 (TEC005)","role": "Tester", "start_date": "2020-08-01", "end_date": "2021-08-01"}
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
