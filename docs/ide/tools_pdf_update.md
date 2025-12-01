# Tools PDF Update

Use this option to update all Atmel PDF files.

The Atmel data sheets are stored in the \PDF subdirectory.

The following window will be shown :

![pdf_update](pdf_update.png)

There is only one option available : Check. When you click the Check-button, the MCS server will be checked for newer versions of the PDF documents.

You need to make sure that BASCOM is allowed to contact the internet. 

You also need to have port 211 open. This port is used in FTP mode to contact the MCS server.

The MCS server is synchronizing all PDF files each day with the ATMEL server. This means that the copy on the MCS server can be maximum 24 hours old.

The check will read all available DAT files and check if there is a reference to the PDF.

When an item is disabled(grayed) then it means there is no link to the PDF in the DAT file.

During the check the window will look like this :

![pdf_update_check](pdf_update_check.png)

All PDF's that are newer will have a check mark. These need an update.

You can manual unselect or select the PDF's.

In the log window at the bottom of the window you can view which files will be downloaded.

When you want to download the selected files, press the Download-button.

This will close all PDF documents in the PDF viewer. A backup of each PDF file downloaded will be made before it is downloaded. You need to restore it when something goes wrong during the download(server drops the connection for example).

When a document is downloaded, the check mark will be removed.

After all documents are downloaded, they documents are opened again in the PDF viewer.

As of version 2077 the PDF documents are downloaded from the MCS Electronics server.

Previously they were downloaded from Atmels webserver. When Atmel change the file name the link is broken and you can not update the file.

To solve this all files are stored on the MCS server and each day all files are synchronized with atmel so all files are maximum 1 day old.

As of version 2079 the PDF files are downloaded using FTP. This results in a better performance. Just make sure port 411 is open in your firewall for outgoing connections.