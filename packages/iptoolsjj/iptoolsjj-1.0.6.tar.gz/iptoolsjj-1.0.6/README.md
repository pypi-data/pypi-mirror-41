I have written my own python ip/subnet tool. It's for python2/3.
Use theese methods to conver ip mask formats and to check if ip/subnet belong to other subnet.
I made it partly for fun and to learn, so perhaps these are not the best, but they get the job done.
Checking if ip belongs to subnet is actually about 20-30% faster, than with tools from netaddr module.

Instalation:

	pip install iptoolsjj

Import:
(I use *, not worrying about namespace because its small script ):

	from iptoolsjj import *
Example:


Check if 192.168.10.10 is inside 192.168.10.0/22:

	if iptoolsjj.is_in_subnet("192.168.10.10", "192.168.10.0/22"):
    		print ("yes")
	
Convert mask '255.255.255.240' to '28':

	print(iptoolsjj.mask255_to_dec("255.255.255.240"))

Convert mask '28' to '['255', '255', '255', '240']' (normally it's list format):

	print(iptoolsjj.dec_to_mask255(28))

or

	print(".".join(iptoolsjj.dec_to_mask255(28)))

