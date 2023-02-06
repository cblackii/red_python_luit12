# Start with an empty list of AWS services
aws_services = []
print(aws_services)
print("The list is empty.")

#Populate the list using append or insert
aws_services.insert(0, 'EC2')
aws_services.insert(1, 'VPC')
aws_services.insert(2, 'IAM')
aws_services.insert(3, 'Lambda')
aws_services.insert(4, 'Cloudformation')

#Print the List
print(aws_services)

#Print the list length
print(len(aws_services))

#Insert items to the list
aws_services.insert(5, 'Cloud9')
print(aws_services)

#List length
print(len(aws_services))

#Remove last two services from the list
aws_services[2:]= []

#Print new list and length of the list
print(aws_services)
print(len(aws_services))