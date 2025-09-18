import argparse
from mwinfo.health_info import HealthInfoMW
from mwinfo.district_info import DistrictInfoMW
from mwinfo.demographics_info import DemographicsInfoMW
from mwinfo.agriculture_info import AgriInfoMW
from mwinfo.currency_converter import CurrencyConverter

def main():   
    parser = argparse.ArgumentParser(
        description="Malawi Info CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Health Info
    health_parser = subparsers.add_parser("health-info", help="Get health info")
    health_parser.add_argument("--district", type=str, help="District name")

    # District Info
    district_parser = subparsers.add_parser("district-info", help="Get district info")
    district_parser.add_argument("--district", type=str, help="District name")
    district_parser.add_argument("--region", type=str, help="Region name")

    # Demographics Info
    demo_parser = subparsers.add_parser("demographics-info", help="Get demographics info")
    demo_parser.add_argument("--district", type=str, help="District name")
    demo_parser.add_argument("--region", type=str, help="Region name")

    # Agriculture Info
    agri_parser = subparsers.add_parser("agriculture-info", help="Get crop/fish info")
    agri_parser.add_argument("--crop", type=str, help="Crop name")
    agri_parser.add_argument("--fish", type=str, help="Fish name")

    # Currency Converter
    currency_parser = subparsers.add_parser("currency", help="Convert currency")
    currency_parser.add_argument("--amount", type=float, required=True, help="Amount to convert")
    currency_parser.add_argument("--from", dest="from_currency", type=str, required=True, help="From currency")
    currency_parser.add_argument("--to", dest="to_currency", type=str, required=True, help="To currency")

    args = parser.parse_args()

    if args.command == "health-info":
        hi = HealthInfoMW()
        if args.district:
            print(hi.get_health_info(args.district))
        else:
            print("Please provide --district for health info.")

    elif args.command == "district-info":
        di = DistrictInfoMW()
        if args.district:
            info = di.get_district_info(args.district)
            print(info if info else f"No info found for district {args.district}")
        elif args.region:
            districts = di.get_districts_by_region(args.region)
            print(districts if districts else f"No districts found in region {args.region}")
        else:
            print("Please provide --district or --region for district info.")

    elif args.command == "demographics-info":
        dm = DemographicsInfoMW()
        if args.district:
            pop = dm.get_population(args.district)
            age = dm.get_age_distribution(args.district)
            gender = dm.get_gender_ratio(args.district)
            if pop is None:
                print(f"No demographics info for district {args.district}")
            else:
                print({
                    "population": pop,
                    "age_distribution": age,
                    "gender_ratio": gender
                })
        elif args.region:
            # Return districts in that region
            di = DistrictInfoMW()
            districts_in_region = di.get_districts_by_region(args.region)
            result = []
            for d in districts_in_region:
                pop = dm.get_population(d)
                age = dm.get_age_distribution(d)
                gender = dm.get_gender_ratio(d)
                result.append({
                    "district": d,
                    "population": pop,
                    "age_distribution": age,
                    "gender_ratio": gender
                })
            print(result if result else f"No districts found in region {args.region}")
        else:
            print("Please provide --district or --region for demographics info.")

    elif args.command == "agriculture-info":
        ag = AgriInfoMW()
        if args.crop:
            print(ag.get_crop_info(args.crop))
        elif args.fish:
            print(ag.get_fish_info(args.fish))
        else:
            print("Please provide --crop or --fish for agriculture info.")

    elif args.command == "currency":
        cc = CurrencyConverter()
        try:
            converted = cc.convert(args.amount, args.from_currency, args.to_currency)
            print(f"{args.amount} {args.from_currency.upper()} = {converted:.2f} {args.to_currency.upper()}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
