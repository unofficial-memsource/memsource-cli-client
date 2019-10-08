# Getting started

### Basic Authentication requirements

You can skip `--user-name` and `--password` if you would like to, but please
make sure to `export JIRA_USERNAME` and `export JIRA_PASSWORD` in your `rc` file

For example:
```
export JIRA_USERNAME="jiraUser01"
export JIRA_PASSWORD="My secret password"
```

#### Example: Basic Authentication
```
python jira.py --jira-url <JIRA URL> \
--basic \
--user-name <JIRA username> \
--password <JIRA password> \
--project <JIRA Project "PROJECT"> \
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

### Kerberos Authentication requirements
```
source ~/git/memsource-cli-client/.memsource/bin/activate
pip install -r ~/git/memsource-cli-client/memsource_cli/scripts/requirements.txt
kinit <user>@<DOMAIN>
klist
```

#### Example: Kerberos Authentication
```
$ python jira.py --jira-url <JIRA URL> \
--auth-url <JIRA AUTH URL for Kerberos> \
--project <JIRA Project "PROJECT"> \
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

### Known issues

#### How to get Sprint ID
Find another JIRA issue in the same Sprint you want to use

Visit  `https://<jira-url>/rest/api/2/issue/<jira-issue>`  
Search for `com.atlassian.greenhopper.service.sprint.Sprint@166e2f31[id=7731,rapidViewId=...` and use id=`7731`

#### Ignore Python SSL Warnings

Add to your `rc` file:
```
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
```