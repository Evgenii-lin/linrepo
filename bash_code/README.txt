This script allows to auto create virtual machine in Proxmox server.
First of all, user types the starting index to create VMs from template in Proxmox, then the template id itself.

The array is populated with indexes and Proxmox creates VMs from template automatically. Normaly, if index intersects with another VM id, Proxmox will say that this VM is already existing.
