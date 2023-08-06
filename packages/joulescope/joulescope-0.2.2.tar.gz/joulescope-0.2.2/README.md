
# Joulescope

Welcome to Joulescope™!  Joulescope is an inexpensive, precision DC energy 
analyzer that enables you to build better products.  
Joulescope™ accurately and simultaneously measures the voltage and current 
supplied to your target device, and it then computes power and energy. 
For more information on Joulescope, see 
[www.joulescope.com](https://www.joulescope.com).

This pyjoulescope package contains the driver and command-line utilities that 
run on a host PC and communicate with a Joulescope device over USB. 
Most users will run the graphical user interface which is in the 
pyjoulescope_ui package.  Developers may import this package to automate
and script Joulescope operation. 
The majority of code is written in Python 3.6+, but a small amount is in 
Cython for better performance. 


## Developer

Install normal dependencies

    pip3 install -r requirements.txt


Install Cython

    pip3 install check-manifest Cython coverage wheel


## License

All pyjoulescope code is released under the permissive Apache 2.0 license.
