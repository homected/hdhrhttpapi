HDHRHTTPAPI
-----------

This is a small library to get information from HD HomeRun devices through the HTTP API for Python 3.

Background
----------

The HDHomeRun products from SiliconDust are basically network TV tuners that broadcast the TV from 
your cable or antenna to your network. These devices has one or more built-in TV tunners so allow to
stream the TV channels to the SiliconDust and third-parties applications.

There are several libraries for different lenguages to communicate to HDHomeRun devices but the aim 
of this library is only to allow homeassistant software to be able to know the state of the tunners.

As homeassistant is developed in Python and has some restrictions to access directly to the I/O hardware
I develop this small utility to allow a custom component 

The goals of this project were as follows:

- Be able to discover the device(s) on the local network.
- Be able to poll for status.
- For a tuner to be able to get the current channel.

All goals have all been completed.


Requirements
------------

- The HDHomeRun library. If your distro has a packaged version that is 
  too old, you might have to download these from the website: 
  
    http://www.silicondust.com/support/hdhomerun/downloads/linux

  If you have the build-tools installed, all you have to do is "make" from the 
  directory that you extracted the files to. Then, just make sure the library 
  "libhdhomerun.so" is either in the directory of this project, or in the 
  library search-path.

Development Resources
---------------------

In addition to the libhdhomerun source, the [HDHomeRun development guide](https://www.silicondust.com/hdhomerun/hdhomerun_development.pdf) is also useful.
