from datetime import datetime

# Birth before death
<<<<<<< HEAD
def us3(indi, fam):
    print("User Story 2 - Birth before death, Running")
=======
from dateutil.relativedelta import relativedelta


def us3(indi, fam):
    print("User Story 3 - Birth before death, Running")
>>>>>>> 8499c4a14e14e479e2f93ee83eea789d2f4bf983
    for person in indi:
        m = person['DEAT']
        if person['DEAT'] == 'NA':
            m = datetime.now()

        if person['BIRT'] > m:
            print(
                f"{person['INDI']} {person['NAME']} were born before they died")

    print("User Story 3 Completed")
    return True


# Birth before marriage of parent
def us8(indi, fam):
    print("User Story 8 - Birth before marriage of parent, Running")
    for family in fam:
        marriagedate = family["MARR"]
        for child in family["CHIL"]:
            childobj = next(
                (item for item in indi if item["INDI"] == child), False)

            if childobj and childobj["BIRT"] > marriagedate:
                if family["DIV"] != "NA" and childobj["BIRT"] > family["DIV"] + relativedelta(months=+9):
                    print(f"Indi id -> {childobj['INDI']}, Birth after divorce")
                    return False
                continue
            elif childobj["BIRT"] < marriagedate:
                print(f"Indi id -> {childobj['INDI']}, Birth before marriage")
                return False
            else:
                print(f'child with id {child} does not exist in indi list')
                return False

    print("User Story 8 Completed")
    return True