Command Monitor
---------------

This is a command line utility for reporting the status of a long-running job.
This project started because the author got tired of building ``c++`` code and
having to choose between staring at a screen while waiting for the job to end
or starting another task only to come back much after a job had ended. With
this utility, instead of typing::

    $ make

you can instead type:: 

    $ cmd_monitor.py "make"

When the make job ends, a status notification will show up on your desktop
along with a sound indicating whether the job was successful or not.

Installation
------------

    $ pip install cmd_monitor

Additionally, the default sounds are provided on Ubuntu with the
``ubuntu-sounds`` package. Pulseaudio is used to play the sounds (from the package ``pulseaudio-utils``).
If you are on another distribution, you can override
the default sounds with the following flags::

    $ cmd_monitor --success_sound /my/success/sound --fail_sound /my/fail/sound

Or to have no sound at all::
    
    $ cmd_monitor --success_sound "" --fail_sound ""

Library 
--------

Users can also call this as a library

    
LICENSE
-------

MIT License.
