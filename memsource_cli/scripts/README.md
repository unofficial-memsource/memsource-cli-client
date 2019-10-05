# Getting started

### Prepare
```
source ~/git/memsource-cli-client/.memsource/bin/activate
pip install -r ~/git/memsource-cli-client/memsource_cli/scripts/requirements.txt
```

### Required Kerberos authentication
```
kinit <user>@<DOMAIN>
klist
```

### Create JIRA ticket
```
$ python3 jira.py --jira-url <JIRA URL> \
--auth-url <JIRA AUTH URL for Kerberos> \
--project <JIRA Project "PROJECT13> \
--summary <Summary> \
--description <Description> \
--labels <Labels "label1" "label2"> \
--components <Components "component1" "component2"> \
--issue-type <Issue type Task, Bug...>
--affects-version <Affects version ie "1.1.0" "1.0.0"> \
--fix-versions <Fix version/s ie "1.2.0" "1.2.1"> \
--epic <Epic ie PROJECT-12> \
--sprint <Sprint ID ie 7731>
```

#### How to get Sprint ID
Find another JIRA issue in the same Sprint you want to use

Visit  `https://<jira-url>/rest/api/2/issue/<jira-issue>`  
Search for `com.atlassian.greenhopper.service.sprint.Sprint@166e2f31[id=7731,rapidViewId=...` and use id=`7731`
