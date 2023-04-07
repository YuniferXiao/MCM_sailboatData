from urllib.request import urlopen
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url="https://sailboatdata.com/sailboat"
info_df = pd.DataFrame()
final_df =pd.DataFrame()
name_df,hull_type,rigging_type,loa,lwl,beam,sa,draft,displacement,ballast,sa2,bal,disp,construction,ballast_type,\
first_built,comfort_ratio,formula,S,I,J,P,E,SPL,ISP,sa3,sa4,sa5,sa6,est\
=([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
for name in namelist:
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--proxy-server=https://127.0.0.1:7890")

    s = Service(r"./chromedriver.exe")
    driver = webdriver.Chrome(service = s, options=options)
    driver.get(url)

    textarea = driver.find_element(By.NAME,"filter[name]")
    submit_checkbox = driver.find_element(By.ID,"search-submit")

    textarea.send_keys(name)
    driver.execute_script("arguments[0].click();", submit_checkbox)

    href = driver.find_element(By.XPATH,"/html/body/main/div[3]/div/div[3]/div[1]/div/table/tbody/tr/td[1]/a")
    driver.execute_script("arguments[0].click();", href)

    html1 = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/article/section[2]/div[4]").get_attribute("textContent")
    html2 = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/article/section[2]/div[5]").get_attribute("textContent")
    html3 = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/article/section[2]/div[6]").get_attribute("textContent")
    html4 = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/article/section[2]/div[7]").get_attribute("textContent")
    html5 = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/article/section[2]/div[8]").get_attribute("textContent")
    html6 = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/article/section[2]/div[9]").get_attribute("textContent")
    html = html1 + html2 + html3 + html4 + html5 + html6

    sleep(2) #所需时间较久
    driver.quit()
    temp = html.split("\n")
    name_df.append(name)
    for i in range(len(temp)):
        if "Hull Type" in temp[i]:
            hull_type.append(temp[i+3])
        elif "Rigging Type" in temp[i]:
            rigging_type.append(temp[i+3])
        elif "LOA" in temp[i]:
            loa.append(temp[i+3])
        elif "LWL" in temp[i]:
            lwl.append(temp[i+3])
        elif "Beam" in temp[i]:
            beam.append(temp[i+3])
        elif "S.A. (reported)" in temp[i]:
            sa.append(temp[i+3])
        elif "Draft (max)" in temp[i]:
            draft.append(temp[i+3])
        elif "Displacement" in temp[i]:
            displacement.append(temp[i+3])
        elif "Ballast:" in temp[i]:
            ballast.append(temp[i+3])
        elif "S.A./Disp." in temp[i]:
            sa2.append(temp[i+3])
        elif "Bal./Disp." in temp[i]:
            bal.append(temp[i+3])
        elif "Disp./Len." in temp[i]:
            disp.append(temp[i+3])
        elif "Construction" in temp[i]:
            construction.append(temp[i+3])
        elif "Ballast Type" in temp[i]:
            ballast_type.append(temp[i+3])
        elif "First Built" in temp[i]:
            first_built.append(temp[i+3])
        elif "Comfort Ratio" in temp[i]:
            comfort_ratio.append(temp[i+3])
        elif "Capsize Screening Formula" in temp[i]:
            formula.append(temp[i+3])
        elif "S#" in temp[i]:
            S.append(temp[i+3])
        elif "I:" in temp[i]:
            I.append(temp[i+3])
        elif "J:" in temp[i]:
            J.append(temp[i+3])
        elif "P:" in temp[i]:
            P.append(temp[i+3])
        elif "E:" in temp[i]:
            E.append(temp[i+3])
        elif "SPL/TPS:" in temp[i]:
            SPL.append(temp[i+3])
        elif "ISP" in temp[i]:
           ISP.append(temp[i+3])
        elif "S.A. Fore" in temp[i]:
            sa3.append(temp[i+3])
        elif "S.A. Main" in temp[i]:
            sa4.append(temp[i+3])
        elif "S.A. Total (100% Fore + Main Triangles)" in temp[i]:
            sa5.append(temp[i+3])
        elif "S.A./Disp. (calc.)" in temp[i]:
            sa6.append(temp[i+3])
        elif "Est. Forestay Len." in temp[i]:
            est.append(temp[i+3])
    info_df = pd.DataFrame(zip(name_df,hull_type,rigging_type,loa,lwl,beam,sa,draft,displacement,ballast,sa2,bal,disp,construction,ballast_type,\
        first_built,comfort_ratio,formula,S,I,J,P,E,SPL,ISP,sa3,sa4,sa5,sa6,est),columns=["name_df","hull_type","rigging_type","loa","lwl","beam","sa","draft","displacement","ballast","sa2","bal","disp","construction","ballast_type","\
        first_built","comfort_ratio","formula","S","I","J","P","E","SPL","ISP","sa3","sa4","sa5","sa6","est"])
   info_df.to_csv("info.csv")
