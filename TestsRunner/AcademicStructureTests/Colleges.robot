*** Settings ***
Documentation       MedadCMP Academic Structure

Resource            ../../PageObjects/commons/common.robot
Resource            ../../PageObjects/AcademicStructureKeywords/CollegesPage.robot

Test Teardown       closing Browser


*** Test Cases ***
Create a College
    Login To The ControlPanel
    Navigate to Add College
    Fill out Colleges Details
    Submit College Form
    Successfully Messages Appears After Submitting

Delete a College
    Delete Doctype By Name    College    col1

Create new
    Create College By Name    doctype=College
