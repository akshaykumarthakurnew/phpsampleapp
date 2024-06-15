# diagram.py

from diagrams import Diagram, Cluster
from diagrams.azure.compute import VM
from diagrams.azure.network import VirtualNetworks, Subnets
from diagrams.azure.database import SQLDatabases
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.storage import StorageAccounts

with Diagram("Azure Infrastructure", show=False):
    with Cluster("Resource Group: example-resources"):
        with Cluster("VirtualNetworks: example-network"):
            subnet = Subnets("example-subnet")

            vm1 = VM("example-vm")
            new_vm = VM("new-vm")

            subnet - [vm1, new_vm]
        
        sql_db = SQLDatabase("example-db")
        ad = ActiveDirectory("example-ad")

        storage = StorageAccounts("examplestorageacct")

    subnet >> sql_db
    vm1 >> ad
    new_vm >> ad
    vm1 >> storage
    new_vm >> storage
