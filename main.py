from pyutils_lib.services.StatTimer import StatTimer
from pyutils_lib.services.config_manager import ConfigManager


#ConfigManager().define_setting(key,is_secret,value,datatype,Description)


this_timer = StatTimer()

ConfigManager.load_configuration()

print("Hello World")

print(f"Total Time: {this_timer.Duration()}")