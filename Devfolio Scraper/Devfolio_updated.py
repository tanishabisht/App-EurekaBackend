from selenium import webdriver
from time import sleep
import io
import json


driver = webdriver.Chrome(executable_path="E:\\Setups\\chromedriver.exe")
driver.get("https://devfolio.co/hackathons?hackathon_type%3Din_person%2Conline%26time_frame%3Dpast")
sleep(5)

# Get list of all submission btns
viewSubmissionBtnList = driver.find_elements_by_class_name("csLBIo")


# for viewSubmissionBtn in viewSubmissionBtnList[:3]:
for viewSubmissionBtn in viewSubmissionBtnList:
    print()
    print("start")
    viewSubmissionBtn.click()

    idx = viewSubmissionBtnList.index(viewSubmissionBtn)
    
    # change the driver value to the new window
    window_after = driver.window_handles[idx + 1]
    driver.switch_to.window(window_after)

    print("after clicking view submit button: ", driver.current_url)



    # find devfolio project links: devfolioProjectSiteLinkList
    sleep(10)
    projectCards = driver.find_elements_by_class_name("ctjdaT")
    devfolioProjectSiteLinkList = []
    for projectCard in projectCards:
        devfolioProjectSiteLinkList += [projectCard.get_attribute("href")]
    print("project in devfolio link : \t\t", devfolioProjectSiteLinkList)


    
    # find gitHub links
    gitHubList = []
    nameList = []
    descList = []
    specialMentionList = []
    stacksList = []
    longDescList = []
    if devfolioProjectSiteLinkList:
        for projectSiteLink in devfolioProjectSiteLinkList:
        # for projectSiteLink in devfolioProjectSiteLinkList:
            driver.get(projectSiteLink)
            sleep(5)
            nameList += [driver.find_elements_by_class_name("kLvVpV")[0].text]
            descList += [driver.find_elements_by_class_name("ibjmgQ")[0].text]
            if driver.find_elements_by_class_name("fnBGpd"):
                specialMentionList += [driver.find_elements_by_class_name("fnBGpd")[0].text]
            else:
                specialMentionList += " "
            longDescList += [driver.find_elements_by_class_name("dWQqhO")[0].text]
            githubProjectList = []
            for gitHubLink in driver.find_elements_by_class_name("CcGlC"):
                githubProjectList += [gitHubLink.get_attribute("href")]
            gitHubList.append(githubProjectList)
            stackList = []
            for stack in driver.find_elements_by_class_name("hhaqiy"):
                stackList += [stack.text]
            stacksList.append(stackList)
        print("nameList\t", len(nameList))
        print("descList\t", len(descList))
        print("devfolioProjectSiteLinkList\t", len(devfolioProjectSiteLinkList))
        print("gitHubList\t", len(gitHubList))
        print("specialMentionList\t", len(specialMentionList))
        print("stacksList\t", len(stacksList))
        print("longDescList\t", len(longDescList))

        # for i in range(len(projectCards)):
        finalDic = []
        for i in range(len(specialMentionList)):
            dic = {
                "idNo":i, 
                "name":nameList[i], 
                "desc":descList[i], 
                "devfolioLink":devfolioProjectSiteLinkList[i], 
                "githubLinks":gitHubList[i], 
                "special_mention":specialMentionList[i],
                "stacksUsed": stacksList[i],
                "longDesc":longDescList[i]
            }
            finalDic.append(dic)

    # finalJSON = {
    #     "allData": finalDic
    # }

    # with io.open("./Database/finalDic"+ str(idx) + ".js", "w", encoding="utf-8") as f:
    #     f.write(str(json.loads(finalJSON)))
    #     f.close()

    with open("C:\\Users\\TANISHA\\Desktop\\Hackathons\\Hackofiesta\\Devfolio Scraper Updated\\Datbase\\finalDic"+ str(idx) + ".json", 'w') as f:
        json.dump(finalDic, f)


    allTabs = driver.window_handles
    print("all tabs currently open: ", allTabs)
    print("before switching tab: ", driver.current_url)
    driver.switch_to.window(allTabs[0])
    print("after switching tab: ", driver.current_url)