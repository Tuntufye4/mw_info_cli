from .health_info import HealthInfoMW
from .district_info import DistrictInfoMW  
from .demographics_info import DemographicsInfoMW
from .agriculture_info import AgriInfoMW
from .currency_converter import CurrencyConverter
   
import pkg_resources

def get_data_path(filename):
    return pkg_resources.resource_filename(__name__, f"../data/{filename}")
    

__all__ = [
    "HealthInfoMW",
    "DistrictInfoMW",
    "DemographicsInfoMW",
    "AgriInfoMW",
    "CurrencyConverter"  
]
           