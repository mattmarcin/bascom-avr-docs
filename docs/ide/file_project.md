# File Project

Originally the IDE was not designed to support projects. Each file you open is a project.

Most chips were not even suited for big projects.

Some projects use a lot of include files. It is a good idea to break up your code in modular tested modules.

You can simply include the modules with [$include](include.md).

In order to make working with a project more convenient, a number of Project options have been added. The Project menu can be found under the File menu. The Project menu has 4 sub menu items and a MRU list(most recent used projects).

When in project mode, the main project file will be compiled. In normal mode, the active window is considered the project and will be compiled. The same is true for the simulator and programmer. 

A simple project explorer has been added that will list all project files. The active project will be shown in blue. The relative path is shown.

![ProjectExplorer](projectexplorer.png)

You can add a new file to the active project. By default the INC extension will be selected. It will be good practice to give included files the INC extension. The main project should have the BAS extension. When you click the ADD button, a file selection dialog will appear. You can select multiple files by using the SHIFT and/or CTRL keys.

When you add a file to a project, it will be added to the project list. When you double click the file in the list it will be selected. Or when it was not loaded before, it will be loaded from disk.

That a file is part of a project collection does not mean that the file will be used or included : you still need to [$INCLUDE](include.md) a file that you want to use in your project.

You can also remove a file from the project. This will not remove or delete the file from disk. The file will only be removed from the project collection. 

Only one file can be the main project. This is the file that will be compiled. The main file is colored in blue.

![notice](notice.jpg)When you updated from a previous version, you need to reset the docking in order to make the Project List window visible. This option you can find under [Options, Environment, IDE](options_environment.md)

Project New

This option will close all files and the current project and will query for a project file name. The file will have the PRJ extension.

Project Open

This option will close all open files and let you select an existing project file. A project file has the PRJ extension.

The PRJ file contains no code, it only contains data about the project files.

All files from the project will be loaded when they were loaded when you closed the project.

The position and size will be set exactly as when you closed. 

![FileprojectOpen](fileprojectopen.png)

Project Save

This option will save all project files. It will also save other opened non-project files.

Project Close

This option will close the active project. This will end the project mode. The project mode is started when you open a PRJ file either with OPEN or by clicking a PRJ file from the MRU menu. 

When you close bascom and you have the Option 'Auto Load All Files' checked, then like usual, all open files will be saved and when you run bascom again, they will all be opened. This might be confusing since you work in normal mode by default. It is recommended to deactivate the 'Auto Load All Files' when working with projects.

In project mode, you can also drag and drop files to the IDE. If they have the BAS or INC extension, they will be added to the project. In normal mode, the file will be opened.