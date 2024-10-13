# Wiiflow Extra Plugins Pack (Installation Below)
This is a plugin pack that installs the following:

Emulators:
NEC PC-9800 Emulators (Neko Project II - Supports PC9801 and PC9821 games)
DS Emulators (DeSmuME Wii)

Media:
Internet Browser (Opera Browser)
Wiiflow Media Pack (MPlayer CE)

Each mod has also been made to work with Tetsuo Shima's Rhapsodii Shima Mod.

# Why this mod exists
It's a pretty good question. There are a lot of mods that are often left behind, or aren't as popular as the rest (or just down right horrendous like DeSmuME Wii). However, some people like myself find value in such... shit. In 2012, Abz created the Wiiflow 4 Masterpiece Pack containing plugins for... pretty much everything under the sun. Some of these plugins are still the only way to boot these types of files in Wiiflow. Unfortunately, the Wiiflow Plugins Pack by Tetsuo does not contain or support some of these emulators, or support was stopped, like the DS, where older versions of the pack still contain it, however it isn't supported in the latest version anymore. My goal was to bring back these forgotten plugins, which can be supported with the latest versions of these mods.
(ok ngl i just wanted to play touhou on my wii)

# Installation
## Emulators:

### Note: You will need the plugins pack by Tetsuo Shima or Abz already installed

1. Copy the contents of Step 1 to the root of your SD or USB

2. We now need to modify the .ini file in wiiflow/source_menu. The file you need to modify will depend on if you are using Rhapsodii Shima or not:

### Rhapsodii Users:

You need to modify the file named: computers.ini

### Non Rhapsodii Users:

Depending on how many .ini files you have, steps may vary. If you only have 1 .ini file, modify source_menu.ini the exact same way as above. If you have multiple, choose the best source menu you think a PC-98 will fall under (probably the menu to do with computers?)


First, open the file. We need to see how many buttons there are. You can see how many there are by looking.
[ BUTTON_1 ] is button 1 and means there's only 1 button, [ BUTTON_2 ] is button 2, and there's 2 buttons, etc.
Copy the contents of Step 2.ini into this, but change [ BUTTON_NUMBER TO MODIFY ] to the highest amount of buttons you have.
Eg: If I have 16 buttons, I'll change [ BUTTON_NUMBER TO MODIFY ] to [ BUTTON_17 ].
After that, save the file and close it.

3. Repeat Step 2 with the contents of Step 3, however,

### Rhapsodii Users:

You need to modify the file named: handhelds.ini

### Non Rhapsodii Users:

Either source_menu.ini if you have one file, or the source menu to do with handhelds (whatever you think a DS is best for)


Great, you're all done installing the Emulator plugins for the DS and PC98.

### Closing Notes

You may need to fiddle with linking the source buttons with the buttons in the source menu in Wiiflow if they don't automatically configure.
DS boxart can be downloaded from the Cover Project, the dimensions are pretty spot on already.
Turns out, NES boxart size fits really well for PC98 boxart, I left a copy of Balloon Fight in there so you can see the dimensions of the front, back, and spine.

## Opera Browser:

Coming Soon

## Media Pack:

Coming Soon

# Auto Installer:

The auto installer can be used to install this automatically.

## Changelog:

### v1.0 Beta:
- Auto installer is released
- Only supports Rhapsodii Shima and Rhapsodii install option

# Credits:

- Tetsuo - Rhapsodii Shima, Wiiflow Plugins Pack
- Abz - Wiiflow 4 Masterpiece Pack
- Wiimpathy - PC-Neko Project II Wiiflow Plugin
- Yui - Neko Project II
- MPlayer CE Team - MPlayer CE
- MagoDX - SFX
- Myself, あ3J - Custom Graphics