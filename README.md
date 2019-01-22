# iMessage-Visualizer
Visualize your iMessage texts and data with graphs and statistics. Allows you to visualize your texting habits with your contacts. Uses your iPhone backup from iTunes to export iMessage Data.
Requires **Python 3.6**.
Requires **iTunes**.

## __Step 1__
Download and install iTunes if you do not already have it.
https://www.apple.com/itunes/download/

## __Step 2__
Plug your iPhone into your computer and open up iTunes. After it has opened click on the phone icon in the upper right corner.
![iPhone Icon Location](https://www.isumsoft.com/images/apple/how-to-backup-my-contacts-from-iphone-to-my-computer/iphone-icon.png)
After Selecting your iPhone on iTunes, click on the button that says "Back Up Now".
![iPhone BackUpNow Location](https://drfone.wondershare.com/images/article/2017/09/15053246246506.jpg)
Wait for the Backup to finish before proceeding to the next step.

## __Step 3__
Download and install iBackup Viewer in order to export the data for visualization.
http://www.imactools.com/iphonebackupviewer/

## __Step 4__
**If you are running the Windows Store version of iTunes, click on *Preferences*, then change the *Default Backup Location* to *C:\Users\[USERNAME]\Apple\MobileSync\Backup\** Where *[USERNAME]* is your Username. Then press okay and continue.**
After letting the installer finish, launch iBackup Viewer. Once it has launched you should see your iPhone Backup, if not then repeat **Step 2**. Click on your iPhone backup and proceed to the next step.

## __Step 5__
Click on the iMessage icon, then select the conversation you would like to export.
![iBackupViewer iMessage icon](https://www.imactools.com/uploads/choose-imessage.png)
After doing so, click on the export button in the top right, and select ***Current Thread to CSV File...***
![iBackupViewer Export Location](https://i.imgur.com/kRTBbR3.png)
Proceed to the next step.

## __Step 6__
Naviagate to the directory where you extracted this project, and save the file as ***texts.csv***.
![Export CSV File](https://i.imgur.com/wxvEZio.png)
Proceed to the next step.

## __Step 7__
Once iBackup Viewer finishes extracting the CSV file, navigate to the Directory containing this project, and start the BAT file called ***GenerateVisualizations.bat***.
After the Command prompt window closes, the generated files will be inside of the ***Data*** folder.

### __ Extra __
If you would like you could run every python file individualy after initially running the ***GenerateVisualizations.bat*** file. The file ***data.csv*** contains all of your text data and extra info.
