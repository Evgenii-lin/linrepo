vmclones=()

vm_index=0
temp_index = 0
vm_amount = 0

read -p "Please enter the initial index to build VMs: " vm_index
read -p "Please enter the index of VM template: " temp_index
read -p "How many VMs needed: " vm_amount  

for vm in {1..$vm_amount}
do
  vmclones+=($temp_index)
  temp_index = $((temp_index+1))
  vm=$((vm+1))
done

for vmId in ${vmclones[@]}; do
	qm qlone $temp_index $vmId --name=vmclone
	echo "Created VM clone $vmId"
done
