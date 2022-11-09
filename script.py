import yaml #imports the yaml module from pyyaml
import json #imports the json module from pyyaml

#A dictionary (data)
data = {
    'Name':'john doe',
    'Position':'DevOps Engineer',
    'Location':'England',
    'Age':'26',
    'Experience': {'gitHub':'software engineer', 'google':'technical engineer', 'linkedin':'data analyst'},
    'Languages': {'markup':['html'], 'programming':['python', 'javascript','golang']}
}

# A list of dictionaries (data2)
data2 = [
    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mongodb-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'3Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    },


    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mysql-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'2Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    }
   
]

# Create YAML for block of YAML data
yaml_output = yaml.dump(data, sort_keys=False) # stores the yaml.dump(data) value in a variable "yaml_output"
# Create YAML for multiple block of YAML data
yaml_output2 = yaml.dump_all(data2, sort_keys=False) # stores the yaml.dump(data) value in a variable "yaml_output"
print(yaml_output) 
print(yaml_output2) 

# Write one block of YAML data to a file
def write_yaml_to_file(x):
# x here reprents the python object
    with open('output.yaml', 'w',) as f :
        yaml.dump(x,f,sort_keys=False) 

write_yaml_to_file(data)

# Write multiple block of YAML to a file
def write_yaml_to_file(x):
    with open('output2.yaml', 'w',) as f :
        yaml.dump_all(x,f,sort_keys=False)
    print('written to file successfully')

write_yaml_to_file(data2)

# Read one block of YAML data
def read_one_block_of_yaml_data(x):
    with open(x,'r') as f:
        output = yaml.safe_load(f)
    print(output) 
    
read_one_block_of_yaml_data('output.yaml')

#Read one block of YAML data and write to a file
def read_and_write_one_block_of_yaml_data(x):
    with open(x,'r') as f:
        data = yaml.safe_load(f)
    with open('output3.yaml', 'w') as file:
        yaml.dump(data,file,sort_keys=False)
    print('done!') 

read_and_write_one_block_of_yaml_data('output.yaml')

# Read multiple block of YAML data
def read_multiple_block_of_yaml_data(x):
    with open(x,'r') as f:
        data = yaml.safe_load_all(f)
        print(list(data)) 
    
read_multiple_block_of_yaml_data('output2.yaml')

# Read multiple block of YAML data and write to a file
def read_multiple_block_of_yaml_data(x):
    with open(x,'r') as f:
        data = yaml.safe_load_all(f)
        loaded_data = list(data)
    with open('output4.yaml', 'w') as file:
        yaml.dump_all(loaded_data,file, sort_keys=False)
    print('done!') 

read_multiple_block_of_yaml_data('output2.yaml')

# Modify one block of YAML data
def read_and_modify_one_block_of_yaml_data(x, key, value):
    with open(x, 'r') as f:
        data = yaml.safe_load(f)
        data[f'{key}'] = f'{value}'
        print(data) 
    print('done!')
    
read_and_modify_one_block_of_yaml_data('output.yaml', key='Age', value=30)

# Modify one block of YAML data and read to a file
def read_and_modify_one_block_of_yaml_data(x,key,value):
    with open(x, 'r') as f:
        data = yaml.safe_load(f)
        data[f'{key}'] = f'{value}'
        print(data)
    with open('output5.yaml', 'w') as file:
        yaml.dump(data,file,sort_keys=False)
    print('done!') 
    
read_and_modify_one_block_of_yaml_data('output.yaml',key='Age', value=30 )

# Modify multiple block of YAML data
def read_and_modify_multiple_block_of_yaml_data(x, index, key, value):
    with open(x,'r') as f:
        data = yaml.safe_load_all(f)
        loaded_data = list(data)
        loaded_data[index][f'{key}'].append(f'{value}')
    print(loaded_data) 
    
    
read_and_modify_multiple_block_of_yaml_data('output2.yaml', 0, 'accessModes', 'ReadOnlyMany')

# Modify multiple block of YAML data and write to a file

def read_and_modify_and_write_multiple_block_of_yaml_data(x, index, key, value):
    with open(x,'r') as f:
        data = yaml.safe_load_all(f)
        loaded_data = list(data)
        loaded_data[index][f'{key}'].append(f'{value}')
    with open('output6.yaml', 'w') as file:
        yaml.dump_all(loaded_data,file, sort_keys=False)
    print(loaded_data)

read_and_modify_and_write_multiple_block_of_yaml_data('output2.yaml', 0, 'accessModes', 'ReadOnlyMany') 

def convert_yaml_to_json(x):
    with open(x, 'r') as f:
        yaml_file = yaml.safe_load(f)
    with open('output.json', 'w') as json_file:
        json.dump(yaml_file, json_file, indent=3)
    print('done!')
convert_yaml_to_json('output.yaml')


