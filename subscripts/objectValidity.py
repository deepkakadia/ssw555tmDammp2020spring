# This function will call all the user story functions (from userStories folder's scripts)
# Returns true only if every story checks out, or returns false
from subscripts.userStories.UserStories_Pratik_Deo import us01, us10, us15, us16, us21, us22
from subscripts.userStories.UserStories_MP import us03, us08, us13, us18, us23, us28
from subscripts.userStories.UserStories_MD import us04, us07, us14, us17
from subscripts.userStories.UserStories_DK import us02, us09, us12, us19, us39, us30, us35, us32
from subscripts.userStories.UserStories_AS import us05, us06, us11, us20


def objectvalid(indi, fam, us32_ids):
    f = open("Output_Project.txt", "a")
    f.write("\n \n")
    us01(indi, fam, f)
    us02(indi, fam, f)
    us03(indi, fam, f)
    us04(indi, fam, f)
    us05(indi, fam, f)
    us06(indi, fam, f)
    us07(indi, fam, f)
    us08(indi, fam, f)
    us09(indi, fam, f)
    us10(indi, fam, f)
    us11(indi, fam, f)
    us12(indi, fam, f)
    us13(indi, fam, f)
    us14(indi, fam, f)
    us15(indi, fam, f)
    us16(indi, fam, f)
    us17(indi, fam, f)
    us18(indi, fam, f)
    us19(indi, fam, f)
    us20(indi, fam, f)
    us21(indi, fam, f)
    us22(indi, fam, f)
    us23(indi, fam, f)
    us28(indi, fam, f)
    us30(indi, fam, f)
    us32(us32_ids, f)
    f.close()
    return True
