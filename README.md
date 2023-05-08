# USD Project Browser
<img width="744" alt="usdPB_default" src="https://user-images.githubusercontent.com/85879687/236754664-5a7025f6-4abe-4907-9126-84013e4a7e82.png">

This **Houdini Tool** is a Pane Interface that acts as a File Directory Browser that allows users to navigate selected directories to view and import **USD** related files.

## Installation

1. Clone this repository into the folder of your choosing - *then continue with one of the following methods:*

### Package Install - Method 1

2. Place the .json file in the appropriate directory for Houdini Packages:
    - Windows: `C:\Users\[username]\Documents\houdini[version]\packages`
    - macOS: `/Users/[username]/Library/Preferences/houdini/[version]/packages`
    - Linux: `~/houdini[version]/packages`
    
3. Restart Houdini to load the new tool located in Houdini's "Pane Tab" section

### Manual Install - Method 2

2. Place the `usdbrowser.pypanel` file into the appropriate directory for Houdini Python Panels:
    - Windows: `C:\Users\[username]\Documents\houdini[version]\python_panels`
    - macOS: `/Users/[username]/Library/Preferences/houdini/[version]/python_panels`
    - Linux: `~/houdini[version]/python_panels`
    
3. Add the USD Project Browser interface to the Toolbar Menu:
    1. In Houdini, navigate to the Python Panel Pane.
    2. Click on 'Edit Interface'.
    3. In the Pane Tab Menu, locate the `USD Project Browser` interface.
    4. Drag and drop the `USD Project Browser` interface to the 'Toolbar Menu Entries' section.
    5. Click 'Apply' and then 'Accept' to save the changes.
    
4. Load the new tool located in Houdini's "Pane Tab" section
    
or

2. Manually create the Pane Interface
    1. In Houdini, navigate to the Python Panel Pane.
    2. Click on 'Edit Interface'.
    3. In the `Interfaces` tab fill out the parameters and code found in __init__.py.
    4. In the Pane Tab Menu, locate the `USD Project Browser` interface.
    5. Drag and drop the `USD Project Browser` interface to the 'Toolbar Menu Entries' section.
    6. Click 'Apply' and then 'Accept' to save the changes.

3. Load the new tool located in Houdini's "Pane Tab" section

## Features

- Browser Toolbar Navigation Buttons with history
- Search Bar
- USD Labels & values
- Directory Labels for the `$JOB` path and it's subdirectories
- Import button creates a `USD Import` Node
