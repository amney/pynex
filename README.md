# pynex

A set of small utilities to improve the Cisco Nexus 7000 series command line implementation of Python.

[More information on Python](http://www.cisco.com/c/en/us/td/docs/switches/datacenter/sw/6_x/nx-os/fundamentals/configuration/guide/b_Cisco_Nexus_7000_Series_NX-OS_Fundamentals_Configuration_Guide_Release_6-x/b_Cisco_Nexus_7000_Series_NX-OS_Fundamentals_Configuration_Guide_Release_6-x_chapter_01011.html) on Cisco Nexus 7000 series switches

Bear in mind that the code is mainly for demonstration purposes and therefore should be adapted before use in any serious situations.

`utilities.py` cointains the pertinent code and `demo.py` contains examples of how it could be used.

A quick example:

```python
from utilities import saves

@saves
def set_hostname(hostname):
    'Set the hostname and then automagically save thanks to the @saves decorator'
    cisco.cli('conf t')
    cisco.cli('hostname %s' % hostname)
```

For more information see the blog at [tim-garner.co.uk](tim-garner.co.uk)

    
