# Help Update

The manual update process is explained [here](updates.md).

The Help Update is an automated version.

The DEMO version can not be updated. You can however install the full version into the DEMO folder.

In order to do a successful update you need the following :

\- license validated in the register (https://register.mcselec.com)

\- working internet connection.

\- firewall and anti virus software must allow BASCOM to connect to the internet

When you click Help, Update, the following window will be shown:

![help_update](help_update.png)

You can select if you want to update BasCom or the Add-On's. 

By default BasCom is selected.

BasCom Update

You need to click the START button to start the actual update process.

When there are unsaved files, you will get an error message :

![update_error](update_error.png)

Your work/project must be saved since as soon the update download is finished, the setup will be executed and BASCOM is closed.

When there are no unsaved files, the current version will be checked.

Checking for update...

Current version : 2.0.8.0

Latest version : 2.0.7.8

No newer version found

In this case, there is no newer file and nothing happens. You need to click the CLOSE button to close the Update window. The IDE will not be closed in this case.

If however a newer version exists, it will be downloaded and unzipped in your windows TEMP folder.

After that setup.exe will be executed with admin rights. So you might get a windows security message that setup requires admin rights. 

BASCOM will close automatically so the new version can be installed in the same folder. We recommend however to install each version into a different folder.

There is no need to uninstall an older version first. 

This setup is the same as you used when you installed the software. But of course the latest version.

You can install into the same folder, but you may also install into a new folder. 

When installing into a new folder you must manual install/copy the license file bscavrl.dll into the new folder yourself.

The bscavrl.dll file you get when you purchase bascom. It is either on CD-ROM or in the bascom-avr application folder.

Please notice that this license file is offered during purchase. We do not offer it again in the event you lost it. 

Add On Update

When you chose to update Add On, you can also specify that libraries will be copied after the update. You do this by checking the 'Copy Libs After Update' check box.

The Add on update will check if you have an add on installed. It will then check if there is an update available. Notice that not all add ons you purchased are supported yet. So those you have to manual download/install.

The supported Add Ons :

\- AVRDOS. 

\- I2CSLAVE

\- XTINY

The add on is always ZIPPED and this ZIP file is downloaded to a new SUB folder named ADDONS.

This ADDONS subfolder is created in the BasCom-AVR application folder.

Each Add On is installed into its own sub folder. So for AVRDOS it is installed into ADDONS\AVRDOS

Older versions that might exist are overwritten.

When an Add-On contains a LIB or LBX file, the option 'Copy Libs after update' will be copied to the BasCom-AVR Library folder. The original file will be renamed so you always have a backup. 

You do need write access in the BasCom-AVR application folder and sub folder.