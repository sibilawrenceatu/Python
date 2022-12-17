@echo off
cls
echo "**********************************************"
echo This batch file will create a project directory
echo This is for demonstration purposes only.
echo "**********************************************"
echo *** press [ctrl][c] to exit or any key to continue ***
pause
set /p NAME=Enter the name of the project, then press [return]
echo Creating %NAME%
mkdir %NAME%
cd %NAME%
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source
cls
dir
echo "**********************************************"
echo Finished creating project %NAME%
echo "**********************************************"
cd ..




@echo off
cls
git status
echo "**************************************************"
echo Performing an add for all files in this directory
git add .
git status
echo "**************************************************"
echo "Enter the commit message:"
set /p id=Enter ID: 
echo %id%
read CommitMessage
git commit -m "$CommitMessage"
git status
echo '**************************************************'
echo 'Pushing to GITHUB repository'
git push -u origin master
echo '**************************************************'
echo 'Done!'









set /p choice= "Please Select one of the above options :" 
echo '%choice%'
