HDHRHTTPAPI
-----------

This is a small library to retrieve information from HD HomeRun devices through the HTTP API and Python 3.

Background
----------

The [HDHomeRun products](https://www.silicondust.com/hdhomerun/) from SiliconDust are basically network TV tuners that broadcast the TV from 
your cable or antenna to your network. These devices has one or more built-in TV tunners so it allows to
stream the TV channels to the [SiliconDust](http://www.silicondust.com) and third-party applications.

There are several libraries for different lenguages to communicate to HDHomeRun devices but I develop this
library to use with homeassistant, a home automation software, to allow it to know the state of the tunners.

As homeassistant is developed in Python and has some restrictions to access directly to the I/O hardware, so 
this library has only some functions needed for my custom component for home assistant.

The goals of this project were as follows:

- Be able to discover the device(s) on the local network.
- Be able to poll for status.
- For a tuner to be able to get the current channel.

All goals have been completed.


Requirements
------------

- There is not other additional requirements than Python 3.8. Other versions not tested.
  
Development Resources
---------------------

- [Nat Burns](https://github.com/burnnat/ha-hdhomerun) custom component for home assistant
- [SiliconDust HD HomeRun development guide](https://www.silicondust.com/hdhomerun/hdhomerun_development.pdf)
- [HDHomeRun HTTP Development Guide](https://info.hdhomerun.com/info/http_api)
