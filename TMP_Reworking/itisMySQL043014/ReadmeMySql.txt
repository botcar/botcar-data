Instructions for ITIS Database MySQL Download 

1. A MySQL database is required to use this data file. If you want
   the database installed on your local system, download and install
   the MySQL database from http://www.mysql.com. 

Note: Downloads and installation instructions are provided on 
      the MySql site. The ITIS staff doesn't provide installation
      or usage support for MySql.

2. Download the latest ITIS MySQL tar.gz file (itisMySQLTables.tar.gz)
   from http://www.itis.gov/downloads. This file is normally updated
    monthly on the last day of the month. 

3. Use an archive tool to ungzip, then untar the ITIS
   data file. This will create a folder containing
   the data installation files.


Installation Instructions for Windows.

Caution: When you install this new ITIS data in MySQL,
   any existing database named "ITIS" will be dropped
   (permanently removed) before the new database is 
   created and the new data loaded. If this is not what you
   want, you should investigate backup and/or data 
   preservation options prior to loading the new data.

Note: The following instructions are for loading the data
   using the Windows GUI via Windows Explorer. You can also
   load the data by entering the appropriate MySql commmand
   directly from a Windows command prompt. See your MySql
   documentation for details.
  
1. Use Windows Explorer to go to the folder you created by
   unzipping the ITIS download.

2. If necessary, edit (using notepad or another plain text
   editor) the installdb.bat file and replace root (-uroot)
   with your MySQL user name.

   If you are updating a remote server, you will need to
   add a -h<servername> to the command in installdb.bat
   as well.

3. Double-click the installdb.bat entry in the ITIS data
   folder to start the load. You will be prompted for the
   MySql password corresponding to the user name in the
   file (root, or your user name if you changed it). Once
   you enter the password, the load process will start.

Note: Depending on the speed and resources of the system
   where you are loading the data, the load process 
   could take several minutes.
  

Installation Instructions for Unix/Linux and OS X
  
1. Open a terminal and navigate to the folder where you
   unzipped the ITIS download file.

2. Enter the following:

      mysql -uroot -p --enable-local-infile < dropcreateloaditis.sql
  
   If your MySql user is not root, substitute your user
   name for root. Also, if you are updating a remote 
   server, you will need to  add a -h<servername> to 
   the command

3. When prompted for your MySql user's password, enter
   it and the load process will start.

Note: Depending on the speed and resources of the system
   where you are loading the data, the load process 
   could take several minutes.

