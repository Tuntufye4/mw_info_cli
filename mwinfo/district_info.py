import yaml
import importlib.resources

class DistrictInfoMW:
    def __init__(self):
        with importlib.resources.open_text("mwinfo.data", "district_data.yml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)["districts"]

    def get_all_districts(self):
        return [d["district"] for d in self.data]

    def get_district_info(self, district_name):
        for d in self.data:
            if d["district"].lower() == district_name.lower():
                return d
        return None

    def get_districts_by_region(self, region_name):
        """Return a list of districts in the given region"""
        return [d["district"] for d in self.data if d["region"].lower() == region_name.lower()]
