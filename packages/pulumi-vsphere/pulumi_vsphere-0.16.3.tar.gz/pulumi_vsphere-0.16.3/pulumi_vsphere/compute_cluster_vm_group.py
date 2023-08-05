# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class ComputeClusterVmGroup(pulumi.CustomResource):
    compute_cluster_id: pulumi.Output[str]
    """
    The [managed object reference
    ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
    resource if changed.
    """
    name: pulumi.Output[str]
    """
    The name of the VM group. This must be unique in the
    cluster. Forces a new resource if changed.
    """
    virtual_machine_ids: pulumi.Output[list]
    """
    The UUIDs of the virtual machines in this
    group.
    """
    def __init__(__self__, __name__, __opts__=None, compute_cluster_id=None, name=None, virtual_machine_ids=None):
        """
        The `vsphere_compute_cluster_vm_group` resource can be used to manage groups of
        virtual machines in a cluster, either created by the
        [`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
        by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.
        
        [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
        [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html
        
        This resource mainly serves as an input to the
        [`vsphere_compute_cluster_vm_dependency_rule`][tf-vsphere-cluster-vm-dependency-rule-resource]
        and
        [`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
        resources. See the individual resource documentation pages for more information.
        
        [tf-vsphere-cluster-vm-dependency-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_dependency_rule.html
        [tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html
        
        > **NOTE:** This resource requires vCenter and is not available on direct ESXi
        connections.
        
        > **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The [managed object reference
               ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] name: The name of the VM group. This must be unique in the
               cluster. Forces a new resource if changed.
        :param pulumi.Input[list] virtual_machine_ids: The UUIDs of the virtual machines in this
               group.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not compute_cluster_id:
            raise TypeError('Missing required property compute_cluster_id')
        __props__['compute_cluster_id'] = compute_cluster_id

        __props__['name'] = name

        __props__['virtual_machine_ids'] = virtual_machine_ids

        super(ComputeClusterVmGroup, __self__).__init__(
            'vsphere:index/computeClusterVmGroup:ComputeClusterVmGroup',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

