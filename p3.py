emp_dict={}
class emp:
 def __init__(self,name,address,pan,basic,tds,da,deduct,hra):
  self.name=name
  self.address=address
  self.pan=pan
  self.basic=basic
  self.hra=hra
  self.da=da
  self.tds=tds
  self.deduct=deduct
  self.gs=self.basic+self.da+self.hra+self.tds+self.deduct
  self.ns=self.gs-(self.tds+self.deduct)
while True:
 enteremp=input("want to enter employee?y/n :")
 if enteremp=='y': 
  name=input("enter name :")
  address=input("enter address :")
  pan=input("enter pan:")
  basic=int(input("enter basic :"))
  da=int(input("enter da:"))
  hra=int(input("enter hra :"))
  tds=int(input("enter tds :"))
  deduct=int(input("enter deduct :"))
  name=emp(name,address,pan,basic,tds,da,deduct,hra)
  if(len(name.name)!=0 and len(pan)!=0): 
   emp_dict.update({pan:name})
   print("dictionary is updated") 
   print(emp_dict[pan].ns) 
  else:
   print("not valid data") 
 else:
  searchemp=input("want to search empyolee?y/n :")
  if searchemp=='y':
   span=input("enter pan no of searching employee")
   for key in emp_dict.keys():
    if key==span:
     print(f'name:{emp_dict[span].name},net salary:{emp_dict[span].ns}')
  else:
   break
print("------------------------------------------------------------------------------------")
print("name\taddress\t\tpan\t\basic\thra\tda\ttds\tdeduct\tgs\tns")
print("-----------------------------------------------------------------------------------")   
for i  in emp_dict:
 print(f'{emp_dict[i].name}\t{emp_dict[i].address}\t\t{emp_dict[i].pan}\t{emp_dict[i].basic}\t{emp_dict[i].hra}\t{emp_dict[i].da}\t{emp_dict[i].tds}\t{emp_dict[i].deduct}\t{emp_dict[i].gs}\t{emp_dict[i].ns}')
    


  

  

