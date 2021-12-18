from jira import JIRA

jira = JIRA('https://hatool.home', basic_auth=('llm234','85167787887SS#'))
# options={"headers":{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}})



# print(jira.projects())