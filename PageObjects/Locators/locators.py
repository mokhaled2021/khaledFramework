# Login Locators
Username_Locator = "//input[@id='login_email']"
password_Locator = "//input[@id='login_password']"
Login_Button = "//button[@type='submit']"
Success_Login = "//input[@id='navbar-search']"
Institution_title = "//h3[@title='New Institution']"

### Academic Structure pages Locators ###

#  Links Locators
Academic_Structure = "//a[@href='/app/academic-structure']"
Admission_Link = "//a[@href='/app/admission']"
admission_Calender_Link ="//*[@id='page-Workspaces']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div[3]/div[2]/div[6]/div[2]/a[1]"
Institution_Link = "//a[@href='/app/institution']"
Campuses_Link = "//a[@href='/app/campus']"
College_Link =  "//a[@href='/app/college']"
Academic_Program_Link = "//a[@href='/app/academic-program']"

# Institutions Locators 
Add_Inistitutions = "//div[@id='page-List/Institution/List']//button[@class='btn btn-primary btn-sm primary-action']"
Institution_Code_Locator = "//input[@data-fieldname='institution_code']"
Institution_Name_Locator = "//input[@data-fieldname='institution_name']"
Institutional_Type_Locator ="//input[@data-fieldname='institutional_type']"
Institutional_Type_Selected = "//ul[@id='awesomplete_list_4']/li[1]"
Website_Locator = "//input[@data-fieldname='website']"
Email_Locator = "//input[@data-fieldname='email']"
Ownership_Locator = "//input[@data-fieldname='ownership']"
Ownership_Selected = "//ul[@id='awesomplete_list_5']/li[1]"
Location_Locator = "//input[@data-fieldname='location'][@data-doctype='Institution']"
MOE_Number_Locator = "//input[@data-fieldname='moe_number']"
Time_Zone_Locator = "//select[@data-fieldname='time_zone']"
Time_Zone_Selected = "//select[@data-fieldname='time_zone']/option[1]"
Date_of_establishment_Locator = "//input[@data-fieldname='establishment_date']"
Date_of_establishment_date = "//div[@id='datepickers-container']/div/div[1]/div/div[2]/div[3]"
Submit_Institution = "//button[@data-label='Save']"
Successfully_Saved = "//*[@id='alert-container']"

# Campuses Locators 
Add_Campuses = "//span[@data-label='Add%20Campus']"
Campus_name_Locator = "/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/div/form/div[1]/div/div[2]/div[1]/input"
campus_code_Locator = "/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div/div[2]/div[1]/input"
campus_location_Locator = "/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/div/form/div[3]/div/div[2]/div[1]/input"
Submit_Campus = "/html/body/div[8]/div/div/div[3]/div[2]/button[2]"

# Colleges Locators 
Add_College = "//span[@data-label='Add%20College']"
College_Name_Locator = "//input[@data-fieldname='college_name'][@data-doctype='College']"
College_Code_Locator = "//input[@data-fieldname='college_code'][@data-doctype='College']"
Establishment_date_Locator = "//input[@data-fieldname='establishment_date']"
Establishment_date = "//*[@id='datepickers-container']/div/div[1]/div/div[2]/div[4]"
Open_campus_collapse = "//DIV[@class='section-head collapsed']"
Add_capmus_row = "//button[@class='btn btn-xs btn-secondary grid-add-row']"
click_in_campus_row = "//*[@id='page-College']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/form/div/div[2]/div[2]/div[1]/div/div/div[2]"
Select_campus = "//*[@id='awesomplete_list_23']/li[1]"
Submit_college = "//*[@id='page-College']/div[1]/div/div/div[2]/div[3]/button[2]/span"

# Academic Program Locators
Add_Academic_Program = "//*[@id='page-List/Academic Program/List']/div[1]/div/div/div[2]/div[2]/button[2]"
Program_Name_Locator = "//*[@id='page-Academic Program']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div/div[1]/form/div[2]/div/div[2]/div[1]/input"
Program_Code_Locator  = "//*[@id='page-Academic Program']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div/div[2]/form/div/div/div[2]/div[1]/input" 
Status_Locator  = "//Select[@data-fieldname='status']" 
Status_Option_Locator  = "//Select[@data-fieldname='status']/option[1]"
Major_Locator  = "//div[@data-fieldname='major']//div[@class='form-group']//input[@role='combobox']" 
Major_Option_Locator = "//strong[normalize-space()='Accounting']"
Education_level_Locator  = "//div[@data-fieldname='education_level']//div[@class='form-group']//input[@role='combobox']" 
Education_level_Option_Locator = "//p[@title='Diploma']"
Degree_Locator  = "//div[@data-fieldname='degree']//div[@class='form-group']//input[@role='combobox']"
Degree_Option_Locator = "//strong[normalize-space()='Associate Diploma']"
Scientific_Certificate_Locator  = "//div[@data-fieldname='scientific_certificate']//input[@role='combobox']"
Scientific_Certificate_Option_Locator = "//strong[normalize-space()='ScientificCertificate1']"
Add_Ownership_Button = "//div[@data-fieldname='offerings']//button[@class='btn btn-xs btn-secondary grid-add-row']"
Ownership_Campus_Locator = "//div[@class='col grid-static-col col-xs-4 error bold']"
Ownership_Campus__Option_Locator = "//li[@aria-selected='true']//p[@title='Arar']"
Ownership_College_Locator = "//input[@placeholder='College']"
Ownership_College_Option_Locator = "//strong[normalize-space()='College of Applied Medical Sciences']"
Ownership_Department_Locator = "//input[@placeholder='Department']"
Ownership_Department_Option_Locator = "//li[@aria-selected='true']//p[@title='Clinical Nutrition']"
Student_Gender_Locator = "//select[@data-fieldname='student_gender']"
Student_Gender_Male = "//select[@data-fieldname='student_gender']/option[1]"
Student_Gender_Female = "//select[@data-fieldname='student_gender']/option[2]"
Qualification_Level_Locator = ""
Period_Type_Locator = ""
Program_Type_Locator = ""
Mode_of_Instruction_Locator = ""
Periods_to_complete_the_program_Locator = ""
Program_Language_Locator = ""
Maximum_Terms_to_complete_the_program_Locator = ""
Program_Discipline_Domain_Locator = ""
Study_Start_Date_Locator = ""
Total_Credit_Hours_Locator = "//input[@data-fieldname='total_credit_hours']"
Current_capacity_Locator = "//input[@data-fieldname='current_capacity']"
Web_View_Section_Name_Locator = ""
Add_Section_Name_Button = ""
Web_View_Section_MyField_Locator = "//div[@data-fieldname='myfield']//input[@type='text']"
Web_View_Section_Camp_Locator = "//div[@data-fieldname='camp']//input[@role='combobox']"
Web_View_Section_Camp = "//*[@id='awesomplete_list_19']/li[2]"
# Admission Calender  Locators
Add_AdmissionCalender = "//*[@id='page-List/Admission Calendar/List']/div[1]/div/div/div[2]/div[2]/button[2]/span"
Academic_Term_Locator = "//*[@id='page-Admission Calendar']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div/div/form/div[2]/div/div[2]/div[1]/div/div/input"
Academic_Term = "//span[normalize-space()='Second Semester 2021-2022']"
AdmissionCalender_status = "//*[@id='page-Admission Calendar']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div/div/form/div[3]/div/label/span[1]/input"
Preference_Start_Date_Locator = "//input[@data-fieldname='capacity_start_date']"
Preference_Start_Date = "//div[@id='datepickers-container']/div[2]/div[1]/div[1]/div[2]/div[21]"
Preference_End_Date_Locator = "//input[@data-fieldname='capacity_end_date']"
Preference_End_Date = "//*[@id='datepickers-container']/div[3]/div[1]/div/div[2]/div[32]"
Submit_AdmissionCalender = "//*[@id='page-Admission Calendar']/div[1]/div/div/div[2]/div[3]/button[2]"
SelectAllRecords = "//*[@id='page-List/Admission Calendar/List']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div[1]/header/div[1]/div[1]/input"
ActionsButton = "//*[@id='page-List/Admission Calendar/List']/div[1]/div/div/div[2]/div[2]/div[2]/button"
DeleteAction = "//*[@id='page-List/Admission Calendar/List']/div[1]/div/div/div[2]/div[2]/div[2]/ul/li[6]"
DeleteActionYes= "//div[contains(@class,'modal fade show')]//button[contains(@type,'button')][normalize-space()='Yes']"