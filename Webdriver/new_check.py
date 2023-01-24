from configparser import ConfigParser

# Create object of Configparser class
config = ConfigParser()

# To read data from config file
config.read('./OtherFiles/config.cfg')
print(config.get('Section1', 'username'))


