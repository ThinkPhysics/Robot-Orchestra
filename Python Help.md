# Python (especially on Windows)

There are a zillion ways of doing this. Here's one:

## Running Python scripts

- Open the `Robot Orchestra Huzzah` directory in a file browser.
- Launch Windows PowerShell. The easiest way to do this is to hit the Windows key (on Think Physics' tablets, this usually says 'Command') and type `PowerShell`, then press Enter.
- Type `cd`, then drag the `Robot Orchestra Huzzah` folder into the PowerShell window. Then his enter. Your command-line shell is now in the right folder.
- Type `C:\Python27\python.exe robot_orchestra.py` to run the main script.

```
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")

pip install paho-mqtt
```

## Editing Python scripts

We like `NotePad++`. Right-click on a Python file and 'Edit with NotePad++' will be an option.

The main file is `robot_orchestra.py`. It's worth reading the comments. Also note that it imports `mod_orchestra.py`, which contains all the networking code and the functions we've written to make scripting the robots as straightforward as possible.
