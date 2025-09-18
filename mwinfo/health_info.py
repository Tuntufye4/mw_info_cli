import yaml
import importlib.resources


class HealthInfoMW:
    def __init__(self):
        # Use importlib.resources to open packaged YAML
        with importlib.resources.open_text("mwinfo.data", "health_data.yml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)["health"]

    def get_all_districts(self):
        return [d["district"] for d in self.data]

    def get_health_info(self, district):
        district = district.lower()
        for item in self.data:
            if item["district"].lower() == district:
                return item
        return None
