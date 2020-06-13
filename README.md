# Privakey


## How to set-up
To set the machine up download "setup" to your OpenWRT machine and run it.
Make sure internet connection is available while setup is running, so it can download the required packages.
After setup is done running, restart the machine and the service will start at boot.

## Usage
After you set up the machine, you need to edit the files change_config and check_dok to your needs.
Once everything is running with the correct IDs, all you need to do is connect your USB to the router.
If you want to stop the program from within the machine, use the command `/etc/init.d/project_service stop`.
Lastly, you can disconnect your USB at any time for the changes to revert.

## Tested Versions
The only tested version of OpenWRT is 19.07.2-x86-64-combined-ext4.
