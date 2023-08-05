# Platinum - Very Important Update
[![License](https://img.shields.io/badge/license-Apache_2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![PyPI version](https://img.shields.io/pypi/v/platinum.svg)](https://pypi.org/project/platinum/) [![Wheel](https://img.shields.io/pypi/wheel/platinum.svg)](https://pypi.org/project/platinum/)


> Chromium - Frequently used google chrome commands mappings.

There are lots of command lines which can be used with the Google Chrome browser.
Some change behavior of features, others are for debugging or experimenting.
This page lists the available switches including their conditions and descriptions.
Last update occurred on **2018-06-08** from `https://peter.sh/experiments/chromium-command-line-switches/`.


## Usage Example

```python
from platinum import Chromium
from selenium import webdriver

options = webdriver.ChromeOptions()
# Run in headless mode, i.e., without a UI or display server dependencies.
# options.add_argument(Chromium.HEADLESS)

# Prevent infobars from appearing.
options.add_argument(Chromium.DISABLE_INFOBARS)

# Starts the browser maximized, regardless of any previous settings.
options.add_argument(Chromium.START_MAXIMIZED)

chrome = webdriver.Chrome(options=options)
```

---


>  generate_user_agent - A User-Agent generator.

This module is for generating random, valid web navigator's User-Agent HTTP headers.

Functions:
* generate_user_agent: generates User-Agent HTTP header

Support:
* os: win, linux, mac, android, ios
* device: desktop, smartphone
* navigator: chrome, firefox, ie, edge


## Usage Example
```python
>>> from platinum import generate_user_agent
>>> generate_user_agent()
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3504.86 Safari/537.36'
>>> generate_user_agent(os=('mac', 'linux'))
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3384.62 Safari/537.36'
>>> generate_user_agent(navigator='edge')
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
>>> generate_user_agent(device_type='smartphone')
'Mozilla/5.0 (Linux; Android 8.0; OPPO R11 Plus Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3191.41 Mobile Safari/537.36'
```


## Command Line Usage
```shell
$ gua
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/15.14986

$ gua -n chrome
Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3489.10 Safari/537.36
```


## Installation

```shell
pip install -U platinum
```