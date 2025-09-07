from pyutils_lib.services.StatTimer import StatTimer                   # type: ignore
from pyutils_lib.services.config_manager import ConfigManager          # type: ignore

ConfigManager().define_setting("setting_name",False,'setting_value',"string","This is a normal non-secret setting") 
ConfigManager().define_setting("secret_setting_name",True,None,"string","This is a secret setting") 

ConfigManager().load_configuration()


logs = ConfigManager().get_logger()

this_timer = StatTimer()

logs.info("Starting Example")
print("Hello World")


logs.info(f"Example Processed In: {this_timer.Duration()}")