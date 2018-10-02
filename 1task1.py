""" this function returns list that contains the tuple (interfacename,"nameif"- value)"""
def int_and_int_name(file_name):
	file=open(file_name)
	l1=[]   #empty list1
	l2=[]	#making all the interface in list2
	l3=[]	#making all interface name in list3
	l4=[]	#making all the interface and interface name in list4
	for line in file:
		line=line.strip()
		for word in line.split():
			l1.append(word)	#list1 contains all the words
	for i in range(len(l1)):
		if l1[i]=='interface':
			l2.append(l1[i+1])	#list2 contains all the interface
		elif l1[i]=='nameif' or (l1[i]=='no' and l1[i+1]=='nameif'):
			#contains all the interface name
			if l1[i]=='no' and l1[i+1]=='nameif':
				l3.append('no name')
			elif l1[i-1]!='no' and l1[i]=='nameif':
				l3.append(l1[i+1])
	for i in range(len(l2)):			#create list of tuple as (interface,interface name)
		l4.append((l2[i],l3[i]))
	return l4

"""this function scan the configuration and return a dictionary that contains the "interface" as
the key and "nameif,VLAN,IPaddress,NetMask" list as the value"""
def list_ifname_ip(file_name):
	file=open(file_name)
	l1=[]   #empty list1
	l2=[]	#making all the list of interface
	l3=[]	#making all the interface name
	l4=[]	#making vlan
	l5=[]	#making ip add
	l6=[]	#making netmask
	l7=[]	#list of intName,vlan,ip add, netMask
	dict={}	# create a dict
	for line in file:
		line=line.strip()
		for word in line.split():
			l1.append(word)
	for i in range(len(l1)):
		if l1[i]=='interface':
			l2.append(l1[i+1])  #making list ofall the interface
		elif l1[i]=='nameif' or (l1[i]=='no' and l1[i+1]=='nameif'):
			#make list of interface name
			if l1[i]=='no' and l1[i+1]=='nameif':
				l3.append('no name')
				l4.append('no vlan')	# only for the networks which has no name,no ip, no netmask
				l5.append('no ip address')
				l6.append('no netmask')
			elif l1[i-1]!='no' and l1[i]=='nameif':
				l3.append(l1[i+1])
				l5.append(l1[i+6])
				l6.append(l1[i+7])
				if l1[i-1]=='management-only':	#only for  management network
					l4.append('no vlan')
				else:
					l4.append(l1[i-2]+l1[i-1])
	for i in range(len(l2)):
		l7=[]
		l7.append(l3[i])
		l7.append(l4[i])
		l7.append(l5[i])
		l7.append(l6[i])
		dict[l2[i]]=l7	#add list of  all nameif,ip,netMask as value in dict
	return dict

if __name__=='__main__':
	print('list that contains the tuple (interfacename,"nameif"- value) is:\n',int_and_int_name('running-config.cfg'))
	print('a dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value is :\n',list_ifname_ip('running-config.cfg'))
