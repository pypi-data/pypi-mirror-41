# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class ComputeClusterVmHostRule(pulumi.CustomResource):
    affinity_host_group_name: pulumi.Output[str]
    """
    When this field is used, the virtual
    machines defined in `vm_group_name` will be run on the
    hosts defined in this host group.
    """
    anti_affinity_host_group_name: pulumi.Output[str]
    """
    When this field is used, the
    virtual machines defined in `vm_group_name` will _not_ be
    run on the hosts defined in this host group.
    """
    compute_cluster_id: pulumi.Output[str]
    """
    The [managed object reference
    ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
    resource if changed.
    """
    enabled: pulumi.Output[bool]
    """
    Enable this rule in the cluster. Default: `true`.
    """
    mandatory: pulumi.Output[bool]
    """
    When this value is `true`, prevents any virtual
    machine operations that may violate this rule. Default: `false`.
    """
    name: pulumi.Output[str]
    """
    The name of the rule. This must be unique in the
    cluster.
    """
    vm_group_name: pulumi.Output[str]
    """
    The name of the virtual machine group to use
    with this rule.
    """
    def __init__(__self__, __name__, __opts__=None, affinity_host_group_name=None, anti_affinity_host_group_name=None, compute_cluster_id=None, enabled=None, mandatory=None, name=None, vm_group_name=None):
        """
        The `vsphere_compute_cluster_vm_host_rule` resource can be used to manage
        VM-to-host rules in a cluster, either created by the
        [`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
        by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.
        
        [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
        [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html
        
        This resource can create both _affinity rules_, where virtual machines run on
        specified hosts, or _anti-affinity_ rules, where virtual machines run on hosts
        outside of the ones specified in the rule. Virtual machines and hosts are
        supplied via groups, which can be managed via the
        [`vsphere_compute_cluster_vm_group`][tf-vsphere-cluster-vm-group-resource] and
        [`vsphere_compute_cluster_host_group`][tf-vsphere-cluster-host-group-resource]
        resources.
        
        [tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html
        [tf-vsphere-cluster-host-group-resource]: /docs/providers/vsphere/r/compute_cluster_host_group.html
        
        > **NOTE:** This resource requires vCenter and is not available on direct ESXi
        connections.
        
        > **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] affinity_host_group_name: When this field is used, the virtual
               machines defined in `vm_group_name` will be run on the
               hosts defined in this host group.
        :param pulumi.Input[str] anti_affinity_host_group_name: When this field is used, the
               virtual machines defined in `vm_group_name` will _not_ be
               run on the hosts defined in this host group.
        :param pulumi.Input[str] compute_cluster_id: The [managed object reference
               ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the virtual machine group to use
               with this rule.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['affinity_host_group_name'] = affinity_host_group_name

        __props__['anti_affinity_host_group_name'] = anti_affinity_host_group_name

        if not compute_cluster_id:
            raise TypeError('Missing required property compute_cluster_id')
        __props__['compute_cluster_id'] = compute_cluster_id

        __props__['enabled'] = enabled

        __props__['mandatory'] = mandatory

        __props__['name'] = name

        if not vm_group_name:
            raise TypeError('Missing required property vm_group_name')
        __props__['vm_group_name'] = vm_group_name

        super(ComputeClusterVmHostRule, __self__).__init__(
            'vsphere:index/computeClusterVmHostRule:ComputeClusterVmHostRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

