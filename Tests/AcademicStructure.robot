*** Settings ***
Documentation  MedadCMP LoginPage
Resource  ../PageObjects/KeywordDefinationFiles/common.robot
Test Teardown   closing Browser


*** Test Cases ***
TC1 : Add new Inistitutions
    Add new Inistitutions
TC2 : Add new College
    Add new College
TC3 : Add new Campuses
    Add new Campuses

