# ❗This is a few years old and no longer maintained

# Python Banner
Python Banner is an open source project to display strings in a big banner like way using non-unicode characters.
This module is fully customizeable and can be used with one import and one function call.

## Setup
First up, download the module, on Windows you can do this by right clicking "Code" and clicking "Download ZIP" and extracting "py-banner.py" to your project directory or use the provided command line commands. If you're on Linux I'll assume you already know how to download a GitHub Repo

In your project file, add the following code:
`from pybanner import createBanner`

And then to call it run:
`createBanner("Hello World", " ", "@")`
(`createBanner(Message, Blank Symbol, Filled Symbol)`)

## Notes
  ###### As of right now, if the window size is too small, the message will appear weird. It may also look strange in Web IDEs but with Visual Studio Code I encountered no issues



