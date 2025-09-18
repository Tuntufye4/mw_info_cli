import yaml
import importlib.resources


class DemographicsInfoMW:
    def __init__(self):
        with importlib.resources.open_text("mwinfo.data", "demographics_data.yml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)["demographics"]

    def get_all_districts(self):
        return [d["district"] for d in self.data]

    def get_population(self, district):
        for item in self.data:
            if item["district"].lower() == district.lower():
                return item["population"]
        return None

    def get_age_distribution(self, district):
        for item in self.data:
            if item["district"].lower() == district.lower():
                return item["age_distribution"]
        return None

    def get_gender_ratio(self, district):
        for item in self.data:
            if item["district"].lower() == district.lower():
                return item["gender_ratio"]
        return None
  