HomeKit Display Switch
======================


HomeKit accessory that allows you to sleep/wake your Mac's display.

Installation:

    $ pipx install HomeKit-DisplaySwitch

(You don't need to use `pipx`, but that keeps this application isolated from the rest of your system).

    $ homekit-display-switch

This starts the server, and shows you the QRCode that you may use to add your Mac to HomeKit.

After pairing, you will want to stop the server (Ctrl-C), and then:

    $ load-homekit-display-switch

This will create the entry in `~/Library/LaunchAgents` to ensure that this program starts whenever you log in.