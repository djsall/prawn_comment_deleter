# PRAWN Comment Deleter
This project was inspired by older versions of the same thing, which sadly didn't work, so I had to rewrite it to work with the new version of [prawn](https://praw.readthedocs.io/en/latest/).

## Requirements
- Python 3.6+ 

- 'prawn' package from pip (pip install prawn)

- [Reddit API access token](https://www.reddit.com/prefs/apps/)

-  a configuration file, we will use the [password flow](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth) authentication method.

### Configuration file
The configuration file has to be placed into the same directory, as your reddit_client.py file.

This is how your creds.py should look like:
```python
credentials = {
  "client_id": "",
  "client_secret": "",
  "password": "",
  "user_agent": "comment deleter by djsall",
  "username": ""
}
```