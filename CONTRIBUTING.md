## How to file a bug report

- Open issues/feature requests, etc at <https://github.com/unofficial-memsource/memsource-cli-client/issues>

## Pull Requests
- [Fork a repository](https://help.github.com/en/articles/fork-a-repo)
- [Configure upstream repository for your fork](https://help.github.com/en/articles/configuring-a-remote-for-a-fork)
- [Sync your fork with upstream repository](https://help.github.com/en/articles/syncing-a-fork)
- Create new branch `git checkout -b "new-topic"`
- Modify the code ie `modified_file.py` then `git add modified_file.py`
- Prepare commit message `git commit`
- Submit the code `git push` and create pull request

### Commit message
- Please always state the next version in the commit name:

For example if the current release version is `0.2.8`, can be found from [here](https://pypi.org/project/memsource-cli/), the commit name must contain `[0.2.9]` in the name like this:
```
[0.2.9] Fix xyz
```
- When you are submitting merge requests, that fixes an issue, please add at the end of your commit message on single line:
```
Closes: #N
```
- Make sure that commit message lines are wrapped at maximum of 72 characters

Your pull requests will be reviewed.
