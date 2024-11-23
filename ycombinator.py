from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

driver = webdriver.Chrome()
driver.maximize_window()


# driver.get("https://www.ycombinator.com/companies?batch=F24&batch=S23&batch=W23&batch=W24&batch=S24&batch=W25&regions=United%20States%20of%20America")
# # Wait for the page to load completely
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "body"))
# )

# store_main_urls = []

# # Infinite scroll logic
# while True:
#     # Get the current scroll height
#     scroll_height = driver.execute_script("return document.body.scrollHeight")
#     # Scroll down to the bottom of the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Wait for 10 seconds to allow new content to load
#     time.sleep(10)

#     # Checking if we reached the bottom by comparing the new height
#     new_scroll_height = driver.execute_script("return document.body.scrollHeight")
#     if new_scroll_height == scroll_height:
#         print("No more content to load.")
#         break
    
#     #Collecting urls
#     all_main_urls = driver.find_elements(By.XPATH, "//div[@class='_section_86jzd_146 _results_86jzd_326']/a")
    
#     for url in all_main_urls:
#         single_url = url.get_attribute("href")
#         #duplicate remove
#         if single_url not in store_main_urls:
#             store_main_urls.append(single_url)
            

# df = pd.DataFrame(store_main_urls, columns=["Links"])
# df.to_excel("Y_combinator.xlsx", index= False)

all_profile_data = []

company_url_directory = "y_combinator.xlsx"
df = pd.read_excel(company_url_directory)

for unique_url in df["Links"]:
    driver.get(unique_url)
    time.sleep(5)
    
    try:
        company_name = driver.find_element(By.XPATH, "//h1").text
    except:
        company_name = ""
        
    try:
        company_slogan = driver.find_element(By.XPATH, "//div[@class='text-xl']").text
    except:
        company_slogan = ""
    
    #Tag issues
    multiple_keywords =[]  
    try:
        company_keywords = driver.find_elements(By.XPATH, "//div[@class='yc-tw-Pill rounded-sm bg-[#E6E4DC] uppercase tracking-widest px-3 py-[3px] text-[12px] font-thin']")
        for all_keywords in company_keywords:
            keywords_name = all_keywords.text.strip()
            multiple_keywords.append(keywords_name)
            
        string_keywords = ", ".join(multiple_keywords)
    
    except:
        string_keywords = ""
 
    try:
        company_description = driver.find_element(By.XPATH, "//p[@class='whitespace-pre-line']").text
    except:
        company_description = ""
        
    try:
        website = driver.find_element(By.XPATH, "//div[@class='group flex flex-row items-center px-3 leading-none text-linkColor ']/a")
        website = website.get_attribute("href")
    except:
        website = ""
        
    try:
        founded = driver.find_element(By.XPATH, "((//div[@class='flex flex-row justify-between'])[1]//span)[2]").text
    except:
        founded = ""

    try:
        team_size = driver.find_element(By.XPATH, "((//div[@class='flex flex-row justify-between'])[2]//span)[2]").text
    except:
        team_size = ""
        
    try:
        Location = driver.find_element(By.XPATH, "((//div[@class='flex flex-row justify-between'])[3]//span)[2]").text
    except:
        Location = ""
        
    try:
        group_partner = driver.find_element(By.XPATH, "(//div[@class='flex flex-row justify-between'])[4]/a").text
    except:
        group_partner = "" 

    try:
        company_linkedin = driver.find_element(By.XPATH, "(//div[@class='space-x-2']/a)[1]").get_attribute("href")
    except:
        company_linkedin = ""

    try:
        company_x = driver.find_element(By.XPATH, "(//div[@class='space-x-2']/a)[2]").get_attribute("href")
    except:
        company_x = ""
        
    try:
        p1_name = driver.find_element(By.XPATH, "(//div[@class='font-bold'])[1]").text
    except:
        p1_name = ""
        
    try:
        p1_designation = driver.find_element(By.XPATH, "(//div[@class='flex-grow']//h3)[2]").text
        p1_designation = p1_designation.split(",")[1].strip()
    except:
        p1_designation = ""
    
    #used contains function
    try:
        p1_x = driver.find_element(
            By.XPATH, "(//a[contains(@href, 'x.com') or contains(@href, 'twitter.com')])[2]"
            ).get_attribute("href")
    except:
        p1_x = "" 

    try:
        p1_linkedin = driver.find_element(
            By.XPATH, "(//a[contains(@href, 'linkedin.com')])[2]"
            ).get_attribute("href")
    except:
        p1_linkedin = ""
        
    try:
        p2_name = driver.find_element(By.XPATH, "(//div[@class='font-bold'])[2]").text
    except:
        p2_name = ""
        
    try:
        p2_designation = driver.find_element(By.XPATH, "(//div[@class='flex-grow']//h3)[3]").text
        p2_designation = p2_designation.split(",")[1].strip()
    except:
        p2_designation = ""
        
    try:
        p2_x = driver.find_element(
            By.XPATH, "(//a[contains(@href, 'x.com') or contains(@href, 'twitter.com')])[3]"
            ).get_attribute("href")
    except:
        p1_x = "" 

    try:
        p2_linkedin = driver.find_element(
            By.XPATH, "(//a[contains(@href, 'linkedin.com')])[3]"
            ).get_attribute("href")
    except:
        p2_linkedin = ""
        
    profile_links = {
        "Company_name":company_name,
        "Company_slogan": company_slogan,
        "Company_tag": string_keywords,
        "Company_description": company_description,
        "website": website,
        "Founded": founded,
        "Team Size": team_size,
        "Location": Location,
        "Group_partner": group_partner,
        "Company_Linkedin": company_linkedin,
        "Company_X": company_x,
        "P1_name": p1_name,
        "P1_Designation":p1_designation,
        "P1_twitter":p1_x,
        "P1_Linkedin":p1_linkedin,
        "P2_name":p2_name,
        "P2_Designation":p2_designation,
        "P2_twitter":p2_x,
        "P2_Linkedin":p2_linkedin,
        
    }
    
    all_profile_data.append(profile_links)
    print(f"Scrape done{len(all_profile_data)}")
    # if (len(all_profile_data) == 10): break
    
df = pd.DataFrame(all_profile_data)
df.to_excel("yc_finaldata.xlsx", index= False)


driver.quit()

