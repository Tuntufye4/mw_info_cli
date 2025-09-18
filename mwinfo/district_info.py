import yaml
import importlib.resources


class DistrictInfoMW:
    def __init__(self):
        with importlib.resources.open_text("mwinfo.data", "health_data.yml", encoding="utf-8") as f:
            self.health_data = yaml.safe_load(f)["health"]

        with importlib.resources.open_text("mwinfo.data", "demographics_data.yml", encoding="utf-8") as f:
            self.demographics_data = yaml.safe_load(f)["demographics"]

    def list_districts(self):
        return sorted({d["district"] for d in self.health_data} | {d["district"] for d in self.demographics_data})

    def get_combined_info(self, district):
        district = district.lower()
        health = next((d for d in self.health_data if d["district"].lower() == district), None)
        demo = next((d for d in self.demographics_data if d["district"].lower() == district), None)

        return {"health": health, "demographics": demo}
