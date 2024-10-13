@echo off
setlocal enabledelayedexpansion

:main_loop
set /p check_plugin="Enter the drive letter (e.g., C, D): "
set check_plugin=!check_plugin:~0,1!

rem Validate the drive letter
if not "!check_plugin!"=="" (
    set check_path_1="%check_plugin%:\wiiflow\plugins_data\platform.ini"
    set check_path_2="%check_plugin%:\wiiflow\source_menu\source_menu.ini"

    rem Check if the first path exists
    if exist !check_path_1! (
        echo Plugins found

        rem Check if the second path exists
        if exist !check_path_2! (
            echo Source Menu found
            call :get_plugin_type
            if defined plugin_type (
                if !plugin_type! == 1 (
                    set /p source_folder="Enter the path of the folder you want to copy: "
                    call :copy_files !source_folder! !check_plugin!
                    call :clean_handhelds_file !check_plugin!

                    set handhelds_path="%check_plugin%:\wiiflow\source_menu\handhelds.ini"
                    call :get_highest_button_number !handhelds_path!
                    set /a new_button_handhelds=!highest_buttons! + 1
                    call :add_button_to_handhelds_file !check_plugin! !new_button_handhelds!
                    set /a new_button_computers=!highest_buttons! + 1
                    call :add_button_to_computers_file !check_plugin! !new_button_computers!
                    goto end
                ) else (
                    echo No files will be copied for this selection.
                    goto end
                )
            ) else (
                echo Error: Could not find the necessary files. Please try again.
                goto main_loop
            )
        ) else (
            echo Source Menu not found.
            goto main_loop
        )
    ) else (
        echo Plugins not found. Please install plugins pack.
        goto main_loop
    )
) else (
    echo Invalid drive letter. Please enter a single letter (e.g., C, D).
    goto main_loop
)

:end
echo Done.
pause
exit /b

:get_plugin_type
echo What source menu are you using?
echo 1. Rhapsodii Shima/Rhapsodii
echo 2. Wiiflow 4 Masterpiece Mod
echo 3. Other
set /p plugin_type="Enter the number corresponding to your choice: "
exit /b

:copy_files
set source_folder=%1
set destination_drive=%2
set destination_path=%destination_drive%:\

if exist "%source_folder%" (
    echo Copying files from %source_folder% to %destination_path%...
    xcopy "%source_folder%\*" "%destination_path%" /E /I /Y
    echo Files copied successfully!
) else (
    echo The specified source folder does not exist.
)
exit /b

:clean_handhelds_file
set handhelds_path=%1:\wiiflow\source_menu\handhelds.ini

if exist %handhelds_path% (
    echo Opening %handhelds_path% to clean out the 'magic' section...
    set skip=0
    for /F "usebackq delims=" %%i in (%handhelds_path%) do (
        set line=%%i
        if "!line!"=="magic=4445534D" (
            set skip=1
        ) else if !skip! == 1 (
            if "!line:~0,1!"=="[" (
                set skip=0
                echo !line! >> "%handhelds_path%.tmp"
            )
        ) else (
            echo !line! >> "%handhelds_path%.tmp"
        )
    )
    move /Y "%handhelds_path%.tmp" %handhelds_path% >nul
    echo Removed the magic section and its associated lines from the file.
) else (
    echo handhelds.ini file not found.
)
exit /b

:get_highest_button_number
set handhelds_path=%1
set buttons=0

if exist %handhelds_path% (
    echo Opening %handhelds_path% to check button instances...
    for /F "tokens=*" %%i in (%handhelds_path%) do (
        echo %%i | findstr /R "\[BUTTON_[0-9][0-9]*\]" >nul
        if !errorlevel! == 0 (
            for /F "tokens=2 delims=_" %%j in ("%%i") do (
                if %%j gtr !buttons! set buttons=%%j
            )
        )
    )
    echo The highest button number found is: !buttons!
) else (
    echo handhelds.ini file not found.
)
set highest_buttons=!buttons!
exit /b

:add_button_to_handhelds_file
set check_plugin=%1
set new_button=%2
set handhelds_path=%check_plugin%:\wiiflow\source_menu\handhelds.ini

(
    echo.
    echo [BUTTON_%new_button%]
    echo autoboot=
    echo cat_page=1
    echo category=0
    echo hidden=no
    echo image=nintendo_ds.png
    echo image_s=nintendo_ds.png
    echo magic=4445534D
    echo source=plugin
    echo title=Nintendo DS
) >> %handhelds_path%

echo DS Emulator Installed in handhelds.ini.
exit /b

:add_button_to_computers_file
set check_plugin=%1
set new_button=%2
set computers_path=%check_plugin%:\wiiflow\source_menu\computers.ini

(
    echo.
    echo [BUTTON_%new_button%]
    echo autoboot=
    echo cat_page=1
    echo category=0
    echo hidden=no
    echo pc98neko.png
    echo image_s=pc98neko.png
    echo magic=6E656B6F,6E656B7F
    echo source=plugin
    echo title=PC-9800
) >> %computers_path%

echo PC98 Emulator was installed to computers.ini.
exit /b
