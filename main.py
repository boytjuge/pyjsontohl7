import wmi

def get_iis_information():
    iis_connection = wmi.WMI(namespace="root\\WebAdministration")
    
    # Example: Get information about IIS Sites
    sites = iis_connection.Site()
    for site in sites:
        print("Name:", site.Name)
        print("State:", site.State)
        print("Physical Path:", site.PhysicalPath)
        print("")

    # Example: Get information about IIS Application Pools
    #app_pools = iis_connection.ApplicationPool()
    #for app_pool in app_pools:
    #    print("Name:", app_pool.Name)
    #    print("State:", app_pool.State)
    #    print("Managed Runtime Version:", app_pool.ManagedRuntimeVersion)
    #    print("")

get_iis_information()