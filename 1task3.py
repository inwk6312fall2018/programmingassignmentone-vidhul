"""function to create a list of "access-list" for "global_access" and "fw-management_access_in"""
def policy(file_name):
	file=open(file_name)
	list=[]
	for line in file:
		line=line.strip()
		for i in line.split():
			if i=='global_access' or i=='fw-management_access_in':
				list.append(line)
	return list
print(policy('running-config.cfg'))
