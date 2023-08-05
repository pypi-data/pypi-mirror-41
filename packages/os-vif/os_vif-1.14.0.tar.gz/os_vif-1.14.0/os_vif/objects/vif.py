#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from debtcollector import removals

from oslo_utils import versionutils
from oslo_versionedobjects import base
from oslo_versionedobjects import fields

from os_vif.objects import base as osv_base
from os_vif.objects import fields as osv_fields


@base.VersionedObjectRegistry.register
class VIFBase(osv_base.VersionedObject, base.ComparableVersionedObject):
    """Represents a virtual network interface."""
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        # Unique identifier of the VIF port
        'id': fields.UUIDField(),

        # The guest MAC address
        'address': fields.MACAddressField(nullable=True),

        # The network to which the VIF is connected
        'network': fields.ObjectField('Network', nullable=True),

        # Name of the registered os_vif plugin
        'plugin': fields.StringField(),

        # Whether the VIF is initially online
        'active': fields.BooleanField(default=True),

        # Whether the host VIF should be preserved on unplug
        'preserve_on_delete': fields.BooleanField(default=False),

        # Whether the network service has provided traffic filtering
        'has_traffic_filtering': fields.BooleanField(default=False),

        # The virtual port profile metadata
        'port_profile': fields.ObjectField('VIFPortProfileBase',
                                           subclasses=True)
    }


@base.VersionedObjectRegistry.register
class VIFGeneric(VIFBase):
    # For libvirt drivers, this maps to type="ethernet" which
    # just implies a bare TAP device, all setup delegated to
    # the plugin

    VERSION = '1.0'

    fields = {
        # Name of the device to create
        'vif_name': fields.StringField()
    }


@base.VersionedObjectRegistry.register
class VIFBridge(VIFBase):
    # For libvirt drivers, this maps to type='bridge'

    VERSION = '1.0'

    fields = {
        # Name of the virtual device to create
        'vif_name': fields.StringField(),

        # Name of the physical device to connect to (eg br0)
        'bridge_name': fields.StringField(),
    }


@base.VersionedObjectRegistry.register
class VIFOpenVSwitch(VIFBase):
    # For libvirt drivers, this also maps to type='bridge'

    VERSION = '1.0'

    fields = {
        # Name of the virtual device to create
        'vif_name': fields.StringField(),

        # Name of the physical device to connect to (eg br0)
        'bridge_name': fields.StringField(),
    }


@base.VersionedObjectRegistry.register
class VIFDirect(VIFBase):
    # For libvirt drivers, this maps to type='direct'

    VERSION = '1.0'

    fields = {
        # Name of the device to create
        'vif_name': fields.StringField(),

        # The PCI address of the host device
        'dev_address': fields.PCIAddressField(),

        # Port connection mode
        'mode': osv_fields.VIFDirectModeField(),

        # The VLAN device name to use
        'vlan_name': fields.StringField(),
    }


@base.VersionedObjectRegistry.register
class VIFVHostUser(VIFBase):
    # For libvirt drivers, this maps to type='vhostuser'

    VERSION = '1.1'

    fields = {
        # Name of the vhostuser port to create
        'vif_name': fields.StringField(),

        # UNIX socket path
        'path': fields.StringField(),

        # UNIX socket access permissions
        'mode': osv_fields.VIFVHostUserModeField(),
    }

    def obj_make_compatible(self, primitive, target_version):
        super(VIFVHostUser, self).obj_make_compatible(primitive,
                                                      target_version)
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1) and 'vif_name' in primitive:
            del primitive['vif_name']


@base.VersionedObjectRegistry.register
class VIFHostDevice(VIFBase):
    # For libvirt drivers, this maps to type='hostdev'

    VERSION = '1.0'

    fields = {

        # The type of the host device.
        # Valid values are ethernet and generic.
        # Ethernet is <interface type='hostdev'>
        # Generic is <hostdev mode='subsystem' type='pci'>
        'dev_type': osv_fields.VIFHostDeviceDevTypeField(),

        # The PCI address of the host device
        'dev_address': fields.PCIAddressField(),
    }


@base.VersionedObjectRegistry.register
class VIFNestedDPDK(VIFBase):
    # For kuryr-kubernetes nested DPDK interfaces

    VERSION = '1.0'

    fields = {
        # PCI address of the device.
        'pci_address': fields.StringField(),

        # Name of the driver the device was previously bound to; it makes
        # the controller driver agnostic (virtio, sr-iov, etc.)
        'dev_driver': fields.StringField(),
    }


@base.VersionedObjectRegistry.register
class DatapathOffloadBase(osv_base.VersionedObject,
                              base.ComparableVersionedObject):
    # Base class for all types of datapath offload
    VERSION = '1.0'


@base.VersionedObjectRegistry.register
class DatapathOffloadRepresentor(DatapathOffloadBase):
    # Offload type for VF Representors conforming to the switchdev model
    VERSION = '1.0'

    fields = {
        # Name to set on the representor (if set)
        'representor_name': fields.StringField(nullable=True),

        # The PCI address of the Virtual Function
        'representor_address': fields.StringField(nullable=True),
    }


@base.VersionedObjectRegistry.register
class VIFPortProfileBase(osv_base.VersionedObject,
                         base.ComparableVersionedObject):
    # Base class for all types of port profile
    # Version 1.0: Initial release
    # Version 1.1: Added 'datapath_offload'
    VERSION = '1.1'

    fields = {
        # Datapath offload type of the port
        'datapath_offload': fields.ObjectField('DatapathOffloadBase',
                                                nullable=True,
                                                subclasses=True),
    }

    obj_relationships = {
        'datapath_offload': (('1.1', '1.0'),),
    }


@base.VersionedObjectRegistry.register
class VIFPortProfileOpenVSwitch(VIFPortProfileBase):
    # Port profile info for OpenVSwitch networks
    # Version 1.0: Initial release
    # Version 1.1: Added 'datapath_type'
    # Version 1.2: VIFPortProfileBase updated to 1.1
    VERSION = '1.2'

    fields = {
        'interface_id': fields.UUIDField(),
        'profile_id': fields.StringField(),

        # Datapath type of the bridge
        'datapath_type': fields.StringField(nullable=True),
    }

    def obj_make_compatible(self, primitive, target_version):
        super(VIFPortProfileOpenVSwitch, self).obj_make_compatible(
            primitive, target_version)
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1) and 'datapath_type' in primitive:
            del primitive['datapath_type']
        if target_version < (1, 2):
            super(VIFPortProfileOpenVSwitch, self).obj_make_compatible(
                primitive, "1.0")


@base.VersionedObjectRegistry.register
class VIFPortProfileFPOpenVSwitch(VIFPortProfileOpenVSwitch):
    # Port profile info for OpenVSwitch networks using fastpath
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileOpenVSwitch updated to 1.1
    # Version 1.2: VIFPortProfileOpenVSwitch updated to 1.2
    VERSION = '1.2'

    fields = {
        # Name of the bridge (managed by fast path) to connect to
        'bridge_name': fields.StringField(),

        # Whether the OpenVSwitch network is using hybrid plug
        'hybrid_plug': fields.BooleanField(default=False),
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfileFPOpenVSwitch, self).obj_make_compatible(
                primitive, "1.0")
        if target_version < (1, 2):
            super(VIFPortProfileFPOpenVSwitch, self).obj_make_compatible(
                primitive, "1.1")


@removals.removed_class("VIFPortProfileOVSRepresentor",
                        category=PendingDeprecationWarning)
@base.VersionedObjectRegistry.register
class VIFPortProfileOVSRepresentor(VIFPortProfileOpenVSwitch):
    # Port profile info for OpenVSwitch networks using a representor
    # This class is now frozen and retained for backwards compatibility. The
    # 'datapath_offload' field in port profiles should be used instead.
    #
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileOpenVSwitch updated to 1.1
    # Version 1.2: VIFPortProfileOpenVSwitch updated to 1.2
    VERSION = '1.2'

    fields = {
        # Name to set on the representor (if set)
        'representor_name': fields.StringField(nullable=True),

        # The PCI address of the Virtual Function
        'representor_address': fields.PCIAddressField(nullable=True),
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfileOVSRepresentor, self).obj_make_compatible(
                primitive, "1.0")
        if target_version < (1, 2):
            super(VIFPortProfileOVSRepresentor, self).obj_make_compatible(
                primitive, "1.1")


@base.VersionedObjectRegistry.register
class VIFPortProfileFPBridge(VIFPortProfileBase):
    # Port profile info for LinuxBridge networks using fastpath
    #
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileBase updated to 1.1
    VERSION = '1.1'

    fields = {
        # Name of the bridge (managed by fast path) to connect to
        'bridge_name': fields.StringField(),
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfileFPBridge, self).obj_make_compatible(
                primitive, "1.0")


@base.VersionedObjectRegistry.register
class VIFPortProfileFPTap(VIFPortProfileBase):
    # Port profile info for Calico networks using fastpath
    #
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileBase updated to 1.1
    VERSION = '1.1'

    fields = {
        # The mac address of the host vhostuser port
        'mac_address': fields.MACAddressField(nullable=True),
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfileFPTap, self).obj_make_compatible(
                primitive, "1.0")


@base.VersionedObjectRegistry.register
class VIFPortProfile8021Qbg(VIFPortProfileBase):
    # Port profile info for VEPA 802.1qbg networks
    #
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileBase updated to 1.1
    VERSION = '1.1'

    fields = {
        'manager_id': fields.IntegerField(),
        'type_id': fields.IntegerField(),
        'type_id_version': fields.IntegerField(),
        'instance_id': fields.UUIDField(),
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfile8021Qbg, self).obj_make_compatible(
                primitive, "1.0")


@base.VersionedObjectRegistry.register
class VIFPortProfile8021Qbh(VIFPortProfileBase):
    # Port profile info for VEPA 802.1qbh networks
    #
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileBase updated to 1.1
    VERSION = '1.1'

    fields = {
        'profile_id': fields.StringField()
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfile8021Qbh, self).obj_make_compatible(
                primitive, "1.0")


@base.VersionedObjectRegistry.register
class VIFPortProfileK8sDPDK(VIFPortProfileBase):
    # Port profile info for Kuryr-Kubernetes DPDK ports
    #
    # Version 1.0: Initial release
    # Version 1.1: VIFPortProfileBase updated to 1.1
    VERSION = '1.1'

    fields = {
        # Specify whether this vif requires L3 setup.
        'l3_setup': fields.BooleanField(),

        # String containing URL representing object in Kubernetes API.
        'selflink': fields.StringField(),

        # String used in Kubernetes v1 API to identifies
        # the server's internal version of this object.
        'resourceversion': fields.StringField()
    }

    def obj_make_compatible(self, primitive, target_version):
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 1):
            super(VIFPortProfileK8sDPDK, self).obj_make_compatible(
                primitive, "1.0")
