import yaml
import importlib.resources


class DemographicsInfoMW:
    def __init__(self):
        # Load demographics_data.yml from the mwinfo.data package
        with importlib.resources.open_text("mwinfo.data", "demographics_data.yml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)["demographics"]

    def get_all_districts(self):
        """Return a list of all districts"""
        return [d["district"] for d in self.data]

    def get_population(self, district):
        """Return the population of a given district"""
        for item in self.data:
            if item["district"].lower() == district.lower():
                return item["population"]
        return None

    def get_age_distribution(self, district):
        """Return the age distribution of a given district"""
        for item in self.data:
            if item["district"].lower() == district.lower():
                return item["age_distribution"]
        return None

    def get_gender_ratio(self, district):
        """Return the gender ratio of a given district"""
        for item in self.data:
            if item["district"].lower() == district.lower():
                return item["gender_ratio"]
        return None
