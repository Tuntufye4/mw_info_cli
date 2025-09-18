import argparse
from mwinfo.health_info import HealthInfoMW
from mwinfo.district_info import DistrictInfoMW   
from mwinfo.demographics_info import DemographicsInfoMW   
from mwinfo.agriculture_info import AgriInfoMW    
from mwinfo.currency_converter import CurrencyConverter


def main():     
    parser = argparse.ArgumentParser(description="Malawi Info CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Health Info
    health_parser = subparsers.add_parser("health-info", help="Get health info")
    health_parser.add_argument("--district", type=str, help="District name")

    # District Info
    district_parser = subparsers.add_parser("district-info", help="Get district info")
    district_parser.add_argument("--district", type=str, help="District name")

    # Demographics Info
    demo_parser = subparsers.add_parser("demographics-info", help="Get demographics info")
    demo_parser.add_argument("--district", type=str, help="District name")

    # Agriculture Info
    agri_parser = subparsers.add_parser("agriculture-info", help="Get crop/fish info")
    agri_parser.add_argument("--crop", type=str, help="Crop name")
    agri_parser.add_argument("--fish", type=str, help="Fish name")

    # Currency Converter
    currency_parser = subparsers.add_parser("currency", help="Convert currency")
    currency_parser.add_argument("amount", type=float, help="Amount to convert")
    currency_parser.add_argument("to_currency", type=str, help="Currency code")

    args = parser.parse_args()

    if args.command == "health-info":
        hi = HealthInfoMW()
        if args.district:
            print(hi.get_district_health(args.district))
        else:
            print(hi.get_all_health_data())

    elif args.command == "district-info":
        di = DistrictInfoMW()
        if args.district:
            print(di.get_district_info(args.district))
        else:
            print(di.get_all_district_data())

    elif args.command == "demographics-info":
        dm = DemographicsInfoMW()
        if args.district:
            print(dm.get_district_data(args.district))
        else:
            print([d["district"] for d in dm.get_all_districts()])

    elif args.command == "agriculture-info":
        ai = AgriInfoMW()
        if args.crop:
            print(ai.find_crop(args.crop))
        elif args.fish:
            print(ai.find_fish(args.fish))
        else:
            print({"crops": ai.get_all_crops(), "fish": ai.get_all_fish()})

    elif args.command == "currency":
        cc = CurrencyConverter()
        print(cc.convert_from_base(args.amount, args.to_currency))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
