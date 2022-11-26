# ig-analyzer
This python module analyzes IG statistics for your profile. Running this app generates the file `Instagram-Stats-Analysis.md` with the analysis results.

Current features include:
- List of followers you aren't following
- List of users not following back

### Setup
1. Login to Instagram and go to https://www.instagram.com/accounts/privacy_and_security/ or `More > Settings > Privacy and security`
1. Click `Request Download` under `Data Download` 
1. Enter email address and select `JSON`
1. Once you receive the data in your email (typically a few min), download and unzip the file
1. In the unzipped folder, go to `followers_and_following` and copy files `followers.json` and `following.json` to path in `ig-analyzer`: `/iganalyzer/input/`

### Running the app
```
python3 -m iganalyzer
```

### Run unit tests
```
python3 -m unittest discover
```