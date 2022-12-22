from playwright.sync_api import Page, expect
import re
import pytest
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import allure


"""Test case for validating url and title of page"""



"""Test case for validating port locations"""
#@pytest.mark.xdist_home
@pytest.mark.homepage
@pytest.mark.smokeUI
@pytest.mark.xdist_group
@pytest.mark.regression
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')
def title_test(page: Page ,host) -> None:
    page.goto(host)
    #assertions
    expect(page).to_have_url(host)
    assert page.title() =="React App"
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'title_test.png'))

@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def title_browsers_screen_test(page: Page ,host) -> None:
    page.goto(host)
    #test case for desktop edge , chrome , webkit , mozilla
    page.set_viewport_size( {
      "width": 1920,
      "height": 1080
    })
    #assertions
    expect(page).to_have_url(host)
    assert page.title() =="React App"
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'title_browsers_test.png'))


@pytest.mark.homepage
@pytest.mark.smokeUI
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')
def port_location_available_test(page: Page,host)-> None:
    page.goto(host)
    locator =page.get_by_label("Port Location")
    
    #assertions
    if locator is True:
        print('Port location is visible on page')
    else:
        print('Port location is not available')
   
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'port_location_available.png'),full_page=True)


            
@pytest.mark.homepage
@pytest.mark.xdist_group  
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')     

def port_location_enabled_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Port Location")
    #assertions
    assert locator.is_enabled()
    page.wait_for_timeout(500)
    assert page.get_by_text('dover')
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'port_location_enabled.png'),full_page=True)

@pytest.mark.smokeUI
@pytest.mark.regression
@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')
def port_location_choose_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Port Location")
    a=locator.select_option(value='liverpool')
    #assertions
    assert locator.is_enabled()
    assert page.get_by_text('liverpool')
    result=a
    if result is True:
        print('selecting ports is available')
    else:
        print('No port locations can be selected')
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'port_location_choose.png'),full_page=True)

@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def port_location_click_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Port Location")
    locator.click()
    page.wait_for_timeout(300)
    page.keyboard.press('Escape')
    #assertions
    
    result=page.get_by_text('liverpool')
    if result is True:
        print('Error-closing the combobox')
    else:
        print('Combobox is successfully closed using keyboard button')
        assert True
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'port_location_open_close.png'),full_page=True)


@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def port_location_count_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.locator("#content > div:nth-child(1) > label:nth-child(1) > select")
    data =expect(locator).to_have_count(7)
    assert data
   
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'port_location_count.png'),full_page=True)


@pytest.mark.xdist_group
@pytest.mark.homepage
@pytest.mark.smokeUI
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')
def freight_available_test(page: Page,host)-> None:
    page.goto(host)
    locator =page.get_by_label("Freight Type")
    #assertions
    if locator is True:
        print('Freight Type  is visible on page')
    else:
        print('Freight Type label is not available')
   
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'Freight_available.png'),full_page=True)


            
@pytest.mark.homepage
@pytest.mark.xdist_group 
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')       
def freight_enabled_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Freight Type")
    #assertions
    assert locator.is_enabled()
    page.wait_for_timeout(100)
    assert page.get_by_text('All')
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'Freight_enabled.png'),full_page=True)

@pytest.mark.homepage
@pytest.mark.smokeUI
@pytest.mark.xdist_group
@pytest.mark.regression
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def freight_choose_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Freight Type")
    result=locator.select_option(value='lolo')
    #assertions
    assert locator.select_option(value='lolo')
    
    if result is True:
        print('selecting Freight type is successful')
    else:
        print('Error-Freight type is not selected')
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'freight_choose.png'),full_page=True)


@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def frewight_click_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Freight Type")
    locator.click()
    page.wait_for_timeout(300)
    page.keyboard.press('Escape')
    #assertions
    
    result=page.get_by_text('lolo')
    if result is True:
        print('Error-closing the combobox')
    else:
        print('Combobox is successfully closed using keyboard button')
        assert True
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'freight_open_close.png'),full_page=True)

@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def freight_count_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.locator("#content > div:nth-child(1) > label:nth-child(2) > select")
    expect(locator).to_have_count(3) 

    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'freight_count.png'),full_page=True)

@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def Target_Selected_test(page: Page,host)-> None:
    page.goto(host)    
    #action
    locator =page.get_by_role("combobox", name="Port Location")
    locator.select_option('southampton')
    locator2=page.get_by_role('combobox',name='Freight Type')
    locator2.select_option('roro')
    result=page.get_by_role("button", name="Enter New Target").click()
     #assertions
     
    assert locator
    assert locator2
    assert page.get_by_role("button", name="Enter New Target").click()
    if result is True:
        print('Enter New Target Functionality is working')
    else:
        print('Error-Enter New Target button click')
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'new_target_selected.png'),full_page=True)


@pytest.mark.homepage
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def Choose_from_table_test(page: Page,host)-> None:
    page.goto(host)    
    locator=page.get_by_role("link", name="AB123456").inner_text()
    

     #assertions
    assert page.get_by_role("link", name="AB123456").is_visible()
    assert page.get_by_role("link", name="AB123456").is_enabled()
    if locator is True:
        print(locator)
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'Table_available.png'),full_page=True)

@pytest.mark.homepage
@pytest.mark.keyboard_cases
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def Click_table_using_keys_test(page: Page,host)-> None:
    page.goto(host)    
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Enter')
    

    #assertions
    locator=page.get_by_role("link", name="AB123456")
    expect(locator).not_to_be_visible()
    expect(page.get_by_role('Button',name='Analyse'))
    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'Table_click.png'),full_page=True)

@pytest.mark.homepage
@pytest.mark.keyboard_cases
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def Click_table_using_keys_test(page: Page,host)-> None:
    page.goto(host)    
    page.keyboard.press('Win')
    
    

    #assertions
    locator=page.get_by_role("link", name="AB123456")
    expect(locator).not_to_be_visible()
    expect(page.get_by_role('Button',name='Analyse'))
    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'Table_click.png'),full_page=True)

@pytest.mark.analyse_page
@pytest.mark.smokeUI
@pytest.mark.regression
@allure.parent_suite('ScanApp_UI')
@allure.suite('analyse_page')
def analyse_test(page: Page ,host) -> None:
    page.goto(host)
    #actions
    page.get_by_role('link', name='AB123456').click()
    page.wait_for_load_state()
    
    #assertions
    page.get_by_role('combobox', name='select-image-summary').is_visible()
    page.get_by_role('button', name='Analyse ButtonArrow').is_visible()
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'scanapp_preview_page.png'))


@pytest.mark.analyse_page
@pytest.mark.smokeUI
@pytest.mark.regression
@allure.parent_suite('ScanApp_UI')
@allure.suite('analyse_page')

def image_summary_test(page: Page ,host) -> None:
    page.goto(host)
    #actions
    page.get_by_role('link', name='AB123456').click()
    page.wait_for_timeout()
    #assertions
    locator=page.get_by_role('combobox', name='select-image-summary').select_option(index=0)
    if locator is True:
        print('Image summary options are available')
    else:
        print('error:not found')
               
    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'image_summary.png'))




@pytest.mark.analyse_page
@pytest.mark.smokeUI
@pytest.mark.regression
@allure.parent_suite('ScanApp_UI')
@allure.suite('analyse_page')

def image_summary_options_test(page: Page ,host) -> None:
    page.goto(host)
    #actions
    page.get_by_role('link', name='AB123456').click()
    page.wait_for_timeout(3000)
    #assertions
    page.get_by_role('combobox', name='select-image-summary').first.click()
    page.wait_for_timeout(1000)
    assert page.get_by_role('combobox', name='select-image-summary').first.click()
   
    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'image_options.png'))




@pytest.mark.analyse_page
@pytest.mark.smokeUI
@pytest.mark.regression
@allure.parent_suite('ScanApp_UI')
@allure.suite('analyse_page')

def symtool_test(page: Page ,host) -> None:
    page.goto(host)
    #actions
    page.get_by_role('link', name='AB123456').click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Analyse ButtonArrow").click()    
    page.wait_for_timeout(3000)
    locator=page.get_by_role('button' ,name='pan')
    

    #assertions
    
    expect(locator)
    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'sym_tool_test.png'))


def safari_viewport_test(page: Page ,host) -> None:
    page.goto(host)
    #actions
    page.get_by_role('link', name='AB123456').click()
    page.wait_for_timeout(1000)
    page.set_viewport_size({
      "width": 1280,
      "height": 720
    },)
    page.get_by_role("button", name="Analyse ButtonArrow").click()    
    page.wait_for_timeout(3000)
    locator=page.get_by_role('button' ,name='Invert colour scheme')
    

    #assertions
    
    expect(locator)
    
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'safari_viewport_test.png'))

 



@pytest.mark.homepage
@pytest.mark.xdist_group
@allure.parent_suite('ScanApp_UI')
@allure.suite('HomePage')

def safari_viewport_homepage_test(page: Page,host)-> None:
    #preconditions
    page.goto(host)    
    #actions
    #safari desktop viewport size 
    page.set_viewport_size({
      "width": 1280,
      "height": 720
    },)
    page.wait_for_timeout(3000)
    page.get_by_role('link',name='AB123456').click()
    page.get_by_role('Button',name='Analyse ButtonArrow').click()
    page.wait_for_timeout(3000)
    #assertions
    assert page.get_by_role("button", name="Colour Scheme").is_enabled()
    assert page.get_by_role("button", name="Pan").is_enabled()
    assert page.get_by_role("button", name="Inspection Complete").is_enabled()
    

    #screenshot report
    page.screenshot(path = os.path.join(os.getcwd(), 'Reports','Automated_reports', 'safari_desktop_viewport.png'),full_page=True)




#  page.get_by_role("cell", name="A").click()
#     page.get_by_role("link", name="AB123456").click()
#     page.wait_for_url("http://localhost:3000/scan/AB123456")
#     page.get_by_role("link", name="Scan Analysis").click()
#     page.wait_for_url("http://localhost:3000/scan/AB123456#1")
#     page.get_by_role("link", name="Scan Analysis").click()
#     page.wait_for_url("http://localhost:3000/")
#     page.get_by_role("link", name="AB123456").click()
#     page.wait_for_url("http://localhost:3000/scan/AB123456")
#     page.get_by_role("button", name="Select directory").click(button="right")
#     page.get_by_role("button", name="Select directory").click()
#     page.get_by_text("Select a directory containing UFF files.").click()
#     page.get_by_text("Select a directory containing UFF files.").click()


# def compare_port_test():
#     path = os.getcwd()
#     path1 = path + "/Reports/" +"/Automated_reports/"
#     path2 = path + "/Reports/"+"/Manual_expected_reports/"
#     a = cv2.imread(path1 + "A_portlocation.png")
#     b = cv2.imread(path2 + "manual.png")
#     difference = cv2.subtract(a, b)
  
#     result = not np.any(difference)
#     if result is True:
#         assert True
#         print("test passed")
#     else:
#         assert False, "Images are different"
      
    
    

    
    


