.. image:: http://www.radappliances.com/images/radware-logo.gif

====================================================
Radware driver for Openstack Kilo Neutron LBaaS v2
====================================================

This Radware driver is the LBaaS v2 service provider driver for openstack KILO release.


***********************************************************
Activate and configure Radware's LBaaS v2 service provider:
***********************************************************

- Install the radware_os_lb_v2_kilo package by executing the following command (use sudo if needed):

	.. code-block:: python

		pip install radware_os_lb_v2_kilo

- Open the neutron configuration file named neutron_lbaas.conf. Under *[service_providers]* section, next to already defined providers, add a new line, declaring the Radware LOADBALANCER v2 provider. The neutron service provider configuration line format consists of three identifiers delimited by a colon:

	- The service name, for LBaaS v2 service it's LOADBALANCERV2.
	- The service provider name, in the example we will use "rdwr"
	- The service provider driver FQN. *radware_os_lb_v2_kilo.v2_driver.RadwareLBaaSV2Driver* is the driver class FQN

	.. code-block:: python

		service_provider = LOADBALANCERV2:rdwr:radware_os_lb_v2_kilo.v2_driver.RadwareLBaaSV2Driver

	You may add the ":default" at the end of the line for making this service provider a default service provider.
	For a reference:

	.. code-block:: python

		service_provider = LOADBALANCERV2:rdwr:radware_os_lb_v2_kilo.v2_driver.RadwareLBaaSV2Driver:default

	**Note: There may be only one default service provider.**

- In neutron.conf file, add a new section where driver's configuration parameters will be set.
	The name of the section should be radware_v2_driver, where "*radware\_*" is a mandatory prefix and the "*v2_driver*" is the driver's python module name.
	Add driver's parameters under this section, for a reference:

	.. code-block:: python

		[radware_v2_driver]
		vdirect_address = 192.168.10.20

	See all possible parameters description in this README.rst file

- Restart the neutron-server service
	
**********************************
Using Radware's LBaaS v2 provider:
**********************************

For LB creation with Radware provider specify the radware provider in lbaas-loadbalancer-create CLI command.
For example, if the name of the radware provider is **rdwr**, provider configuration
line in neutron configuration file will be:

.. code-block:: python

	service_provider = LOADBALANCERV2:rdwr:radware_os_lb_v2_kilo.v2_driver.RadwareLBaaSV2Driver:default


CLI command will be:

.. code-block:: python

	neutron lbaas-loadbalancer-create --provider rdwr ...


************************************************
Driver's configuration parameters specification:
************************************************

Following is a list of all driver configuration parameters.
The only mandatory parameter is vdirect_address. Other parameters have default values

* *vdirect_address*: The primary / standalone vDirect server IP address. **This parameter is mandatory**.
* *ha_secondary_address*:  The secondary vDirect server IP address when vDirect HA pair is used.
* *vdirect_user*: The vDirect server user name, the default is root.
* *vdirect_password*: The vDirect server user password, the default is radware.
* *port*: The vDirect server port. The default is the default vDirect server HTTPS port 2189.
* *ssl*: Use HTTPS for vDirect server connections, the default is True. If False is set, HTTP connections will be used.
* *ssl_verify_context*: Verify SSL certificates on HTTPS connections. the default is True. 
* *timeout*: vDirect server HTTP[S] connection timeout, the default is 5000 milliseconds.
* *base_uri*: vDirect server REST API base uri, the default is ''.
* *service_adc_type*: ADC service type. Options are: VA or VX, the default is VA.
* *service_ha_pair*: Enables or disables ADC service HA-pair, the default is False.
* *configure_allowed_address_pairs*: configure specific allowed address pairs on VIP and PIP ports, in addition to a general CIDR allowed address pair configuration, the default is False.
* *service_throughput*: Service throughput, the default is 1000.
* *service_ssl_throughput*: Service SSL throughput, the default is 100.
* *service_compression_throughput*: Service compression throughput, the default is 100.
* *service_cache*: The size of ADC service cache, the default is 20.
* *service_resource_pool_ids*: The list of vDirect server's resource pools to use for ADC service provissioning, the default is empty.
* *service_isl_vlan*: A required VLAN for the interswitch link to use, the default is -1.
* *service_session_mirroring_enabled*: Enable or disable Alteon interswitch link for stateful session failover the default is False.


***********************************************************************
Creating another Radware service provider with different configuration:
***********************************************************************

Since no flavoring mechanism is currently available for service providers and driver FQN is unique,
another Radware driver may be created and set as another LBAAS v2 service provider in neutron.

This driver package already contains an example python module called **my_driver**.
Those are the steps to create and configure another Radware LBaaS v2 service provider with different configuration:

- The **radware_os_lb_v2_kilo** package contains following modules:

	- *exceptions.py*
	- *rest_client.py*
	- *base_v2_driver.py*
	- *v2_driver.py*
	- *my_driver.py*

- Create a new python module which will contain your new driver class.

	For example, the name will be *"my_driver"*.
	The driver class should be implemented by following rules:

	* It should import the **v2_driver** module and inherit from **v2_driver.RadwareLBaaSV2Driver** class.
	* the **__init__** function should get the plugin as parameter and call the base class **__init__** function with the plugin and the module **__name__** attribute.

	Example of *my_driver.py* module file:

	.. code-block:: python

		import v2_driver


		class MyRadwareLBaaSV2Driver(v2_driver.RadwareLBaaSV2Driver):
			def __init__(self, plugin):
				v2_driver.RadwareLBaaSV2Driver.__init__(self, plugin, __name__)

- Configure the new driver as another LBaaS v2 service provider in neutron configuration file

	The service provider configuration line for this driver will be:

	.. code-block:: python

		service_provider = LOADBALANCERV2:my_rdwr:radware_os_lb_v2_kilo.my_driver.MyRadwareLBaaSV2Driver

	The service provider configuration parameter for this driver will be, for example:

		.. code-block:: python
		   
			[radware_my_driver]
			vdirect_address = 192.168.10.20
			service_adc_type = VX
			service_ha_pair = true
			ssl_verify_context = false
		
	   
	The LB creation CLI command for creating a new LB with this new provider will be:

	.. code-block:: python

		neutron lbaas-loadbalancer-create --provider my_rdwr ...

	**After changing the service providers configuration in neutron configuration file, neutron server service restart is needed.**
