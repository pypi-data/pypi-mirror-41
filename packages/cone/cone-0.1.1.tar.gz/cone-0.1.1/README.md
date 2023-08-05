# __CONE__
---
__cone__ is a tool to simplify your workflow when you are working on Roblox. It comes it two parts:
 - A python package named `cone`
 - A Roblox plugin also named [`cone-plugin`](https://gitlab.com/rbx-cone/cone-plugin)

__cone__ is similar to any syncing tool for Roblox (like [Rojo](https://github.com/LPGhatguy/rojo)). What makes __cone__
allows you to work outside of Roblox Studio, run your tests with [TestEZ](https://github.com/Roblox/testez) from your command line.
## Installation
---
### Package
If you don't have python installed on your computer, you can [get it here](https://www.python.org/downloads/). Then, you can install the package by running `pip install cone` in your command line.
### Plugin
Easiest way to download it is from the [Roblox page](www.google.ca)

## How to use `cone`
---
### Configuration file
In your working directory, there must be a file named `cone.json` where you can tell __cone__ how to sync your project.
```
[
    {
        "path" : "src/ClientScripts",
        "parent" : "ReplicatedFirst"
    },
    ...
    {
        "path" : "src/ServerScripts",
        "parent" : "ServerScriptService"
    }
]
```
The `path` key needs to point to a folder or a file in your project. The `parent` value needs to point to an instance in the Roblox place where you will parent the file or folder pointed by `path`. You can place as many as you need.
### Commands
Each of these commands can be run in the working directory where you `cone.json` file is located.
#### `cone test`
Runs your tests and prints the results in the console.
#### `cone deploy [-t]`
Takes you project and use the `cone.json` configuration file to apply your scripts in the opened Roblox place.
#### `cone revert`
Reverts the last executed `cone deploy`.
