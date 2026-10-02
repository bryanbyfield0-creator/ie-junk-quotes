# Site content for Inland Empire Junk Removal Quotes. Used by build.py.
BASE = "https://bryanbyfield0-creator.github.io/ie-junk-quotes"
BRAND = "Inland Empire Junk Removal Quotes"
SHORT_BRAND = "IE Junk Quotes"
EMOJI = "🚛"
EMAIL = "bryanbyfield0@gmail.com"
PHONE = "909-361-0443"
# FormSubmit endpoint. Plain email until activated; then swap in the hashed alias FormSubmit provides.
FORM_ACTION = "https://formsubmit.co/bryanbyfield0@gmail.com"
FORM_SUBJECT = "New junk removal quote request"
# Google Search Console verification: paste the token (the content="..." value only) here, then rebuild.
# Left empty on purpose, so no verification tag is output until it's filled in.
GOOGLE_VERIFICATION = ""
INDEXNOW_KEY = "b83e5d0c41f94a2e9c7a6d15e2f08b37"
FACTS_CHECKED = "October 2026"
GUIDES_PUBLISHED = "2026-10-02"
PROVIDER_NOUN = "junk removal"
COMPANY_NOUN = "junk removal company"
SERVICE_TYPE = "Junk removal referral"
CTA_TEXT = "Get free junk removal quotes"
ORG_DESCRIPTION = "Free referral service that connects Inland Empire residents with independent local junk removal providers for furniture and appliance removal, cleanouts, yard waste, construction debris, and hot tub or shed removal. Not a hauling company."

PHOTOS = {
 "hero": ("img/movers-carrying-sofa.jpg", 1600, 1066, "Two workers lifting a green sofa to carry it out of an empty room", "RDNE Stock project", "https://www.pexels.com/@rdne/", "Pexels", "https://www.pexels.com/photo/two-men-carrying-a-sofa-7464266/", "Pexels License"),
 "boxes": ("img/pile-of-moving-boxes.jpg", 1600, 1066, "Pile of empty cardboard boxes in the corner of an empty room after a move-out", "SHVETS production", "https://www.pexels.com/@shvets-production/", "Pexels", "https://www.pexels.com/photo/pile-of-brown-empty-boxes-in-the-corner-of-the-room-7203702/", "Pexels License"),
 "yard": ("img/yard-waste-branches.jpg", 1600, 1066, "Pile of cut branches and logs waiting to be hauled away", "K8", "https://unsplash.com/@_k8_", "Unsplash", "https://unsplash.com/photos/9_U9Dt-bKWQ", "Unsplash License"),
}
SVC_IMG = {"furniture-appliance-removal":"hero","yard-waste-removal":"yard","estate-move-out-cleanouts":"boxes"}
HOME_SPLIT_IMG = "boxes"

SERVICES = [
 ("furniture-appliance-removal","Furniture & Appliance Removal","Couches, recliners, mattresses, dressers, tables, refrigerators, washers, dryers, and other bulky items, carried out from wherever they sit, not just from the curb. Appliances with refrigerant, like fridges, freezers, and AC units, need to go to a facility that can handle them safely, so ask where they'll end up."),
 ("garage-home-cleanouts","Garage & Home Cleanouts","Clearing out a packed garage, attic, spare room, or the whole house. Crews can haul everything at once, or work around items you want to keep. Tell providers roughly how much there is (a few items, a pickup load, a full garage) so quotes are accurate."),
 ("yard-waste-removal","Yard Waste Removal","Branches, brush, palm fronds, old sod, dirt, and leftovers from landscaping projects. Good for cleanups that are too big for your green-waste bin, or for clearing out overgrowth before fire season."),
 ("construction-debris","Construction Debris Removal","Drywall, lumber, flooring, cabinets, tile, and other leftovers from a remodel or DIY project. Concrete, dirt, and roofing are heavy, so mention them up front. They often cost more to haul and may need a different truck or trailer."),
 ("hot-tub-shed-removal","Hot Tub & Shed Removal","Taking apart and hauling away old hot tubs, spas, sheds, playsets, and similar structures. Before the crew arrives, the hot tub's power should be disconnected by a qualified electrician. Larger demolition jobs may need a licensed contractor."),
 ("estate-move-out-cleanouts","Estate & Move-Out Cleanouts","Emptying a home after a move, a sale, or the loss of a loved one, or between tenants. Many providers can set aside items for donation or recycling, and some will sweep out the space when they're done."),
]
SVC_SHORT = {
 "furniture-appliance-removal":"couches, mattresses, fridges, washers, and other bulky items carried out for you",
 "garage-home-cleanouts":"packed garages, attics, spare rooms, or whole houses cleared",
 "yard-waste-removal":"branches, brush, sod, and landscaping leftovers hauled off",
 "construction-debris":"drywall, lumber, tile, and remodel leftovers",
 "hot-tub-shed-removal":"old spas, sheds, and playsets taken apart and removed",
 "estate-move-out-cleanouts":"full cleanouts after a move, a sale, or between tenants",
}
def CITY_SVC_LINE(s, n, c): return SVC_SHORT[s]

# ---- sources ----
S_SB=("City of San Bernardino: Keep SB Clean (free bulky item collection)","https://www.sanbernardino.gov/1099/Keep-SB-Clean")
S_FON=("City of Fontana: Residential trash services","https://www.fontanaca.gov/2713/Residential-Trash-Services")
S_FON2=("Burrtec: Fontana residential newsletter, Summer 2026 (PDF)","https://www.burrtec.com/wp-content/uploads/2022/03/Fontana-Summer-2026-6F10_Final.pdf")
S_RIA=("City of Rialto: Large item disposal","https://ca-rialto.civicplus.com/342/Large-Item-Disposal")
S_RED=("City of Redlands: Bulky item special pickup","https://www.redlands.gov/bulky-item-special-pickup/")
S_HIG=("City of Highland: Trash & recycling services","https://highlandca.gov/379/Trash-Recycling-Services")
S_COL=("City of Colton: Refuse and trash","https://coltonca.gov/1088/Refuse-and-Trash")
S_YUC=("City of Yucaipa: Trash, recycling & street sweeping","https://yucaipa.gov/trash-recycling/")
S_RC=("City of Rancho Cucamonga: Residential trash, recycling & organics","https://www.cityofrc.us/healthy-rc/environmental-programs/residential-trash-recycling-organics")
S_RIV=("City of Riverside: Bulky items","https://www.riversideca.gov/publicworks/trash-recycling/trash/bulky-items")
S_RIV2=("City of Riverside: Clean Up Riverside events and drop-off days","https://riversideca.gov/publicworks/trash-recycling/clean-riverside")
S_ONT=("City of Ontario: Bulky item collection","https://www.ontarioca.gov/government/public-works/integrated-waste/bulky-item-collection")
S_COR=("City of Corona: Bulky item pickup (Waste Management)","https://www.coronaca.gov/services/bulky-item-pickup-waste-management")
S_MV=("City of Moreno Valley: Bulky item pickup","https://www.moreno-valley.ca.us/resident_services/waste/trash-bulky-item.html")
S_UPL=("City of Upland: Residential trash services","https://www.uplandca.gov/services/public_works/trash/residential.php")
S_CHI=("City of Chino: Trash","https://www.cityofchino.org/440/Trash")
S_HES=("City of Hesperia: Bulky item pick-up program","https://hesperiaca.gov/494/Large-Item-Pick-Up-Program")
S_VIC=("City of Victorville: Bulky item disposal","https://www.victorvilleca.gov/Government/City-Departments/Environmental-Programs/Residential-Solid-Waste-Services-Resources/Bulky-Item-Disposal")
S_LL=("City of Loma Linda: Bulky item pickup","https://www.lomalinda-ca.gov/services/trash___recycling/bulky_item_pickup")
S_GT=("City of Grand Terrace: Trash, recycling & sewer services","https://www.grandterrace-ca.gov/departments/public_works/trash_recycling")
S_BBM=("Bye Bye Mattress (Mattress Recycling Council): California","https://byebyemattress.com/california/")
S_BBMFAQ=("Bye Bye Mattress: Retailer pick-up FAQ","https://byebyemattress.com/california/ca-faqs/")
S_SBHHW=("San Bernardino County Fire: Household hazardous waste","https://sbcfire.org/hhw/")
S_SBHHW2=("San Bernardino County Fire: HHW collection facilities","https://sbcfire.org/collectionfacilities/")
S_RCHHW=("Riverside County Department of Waste Resources: Household hazardous waste","https://rcwaste.org/household-hazardous-waste")
S_RCHHWF=("Riverside County Waste Resources: 2026 HHW flyer (PDF)","https://rcwaste.org/sites/g/files/aldnop376/files/2026-02/2026%20HHW%20Flyer_V06_02-25-2026_Links.pdf")
S_MINOR=("CSLB: License requirement for minor work increases to $1,000 (PDF)","https://www.cslb.ca.gov/Resources/IndustryBulletins/2024/AB%202622%20Implementation.FINAL.pdf")

def C_(name, county, intro, local, nearby, faq, sources, bulky):
    return dict(name=name, county=county, intro=intro, local=local, nearby=nearby, faq=faq, sources=sources, bulky=bulky)
SBHHW_P = '<p>Paint, chemicals, motor oil, batteries, and other household hazardous waste can go to San Bernardino County Fire\'s free household hazardous waste (HHW) collection sites for county residents. See our <a href="../guides/household-hazardous-waste-disposal-inland-empire.html">hazardous waste guide</a>.</p>'
RCHHW_P = '<p>Paint, chemicals, motor oil, batteries, and other household hazardous waste go to Riverside County\'s free HHW facilities and events, which have a per-trip limit of 15 gallons or 125 pounds. See our <a href="../guides/household-hazardous-waste-disposal-inland-empire.html">hazardous waste guide</a>.</p>'

# bulky = (hauler, free pickups, items per pickup) for the comparison table
CITIES = {
"san-bernardino": C_("San Bernardino","San Bernardino",
 "San Bernardino has a large stock of older single-family homes and rentals, plus student housing near Cal State San Bernardino. Cleanouts between tenants, estate cleanouts, and hauling off old furniture and appliances come up constantly, and foothill homes in areas like Verdemont and Del Rosa add yard debris and old sheds to the list.",
 [("Free city bulky-item pickup first", '''<p>The City of San Bernardino gives residents <strong>two free bulky-item collections per year, up to five items each</strong>, through Burrtec. Schedule at least a week before your regular collection day. Accepted items include furniture, mattresses, appliances, TVs and monitors, scrap metal, wood, tree branches, and up to two tires. Concrete, rock, dirt, and construction or demolition materials are not accepted.</p><p>When it makes sense to hire a hauler: more than five items, items that need to be carried out of the house, construction debris, or anything you need gone before the next available pickup date.</p>'''),
  ("Hazardous items", SBHHW_P)],
 ["Highland","Rialto","Colton","Loma Linda","Redlands"],
 [("Does San Bernardino have free bulky item pickup?","Yes. Residents get two free bulky-item collections per year, up to five items each, through Burrtec. Schedule at least a week before your collection day."),
  ("Will the San Bernardino bulky pickup take construction debris?","No. The city says concrete, rock, dirt, and construction or demolition materials aren't included. A private hauler can take them.")],
 [S_SB,S_SBHHW], ("Burrtec","2 per year","5")),
"fontana": C_("Fontana","San Bernardino",
 "Fontana mixes established neighborhoods with large lots, newer tracts in north Fontana, and lots of families moving in and out. Common requests include clearing packed garages, hauling off old patio sets and playsets, removing yard waste after a big cleanup, and taking away leftover materials after a remodel.",
 [("Fontana's free bulky-item pickups", '''<p>The City of Fontana lists free curbside removal of large or bulky items three times per year as part of residential trash service. Burrtec's Fontana newsletter describes <strong>up to three collections in a 12-month period, with a limit of five items per collection</strong>, including electronic waste. Call Burrtec about a week before your regular collection day.</p>'''),
  ("When a hauler makes more sense", '''<p>Use a private crew for whole-garage cleanouts, remodel debris, items that need to be carried out from inside, or when you've used up your free pickups.</p>'''+SBHHW_P)],
 ["Rialto","Rancho Cucamonga","Ontario","San Bernardino","Upland"],
 [("How many free bulky pickups does Fontana get?","The city lists three free bulky-item pickups per year, and Burrtec's newsletter caps each collection at five items. Call Burrtec to schedule.")],
 [S_FON,S_FON2,S_SBHHW], ("Burrtec","3 per 12 months","5")),
"rialto": C_("Rialto","San Bernardino",
 "In Rialto, junk removal requests often start with a garage that's become a storage unit, a backyard with years of accumulated stuff, or a broken washer, dryer, or fridge that won't fit in the trash bin. Landlords also book quick turnovers between tenants.",
 [("Rialto's bulky-item program", '''<p>The City of Rialto says single-family residential customers can get <strong>up to two free bulky-item pickups per calendar year</strong> through Burrtec, with additional pickups available for a fee. The service won't take vehicle parts, construction materials, or hazardous waste, and it picks up rimless tires (up to two per pickup) at no charge.</p>'''),
  ("Bigger jobs", '''<p>For whole-house or garage cleanouts, or anything the city won't take (like remodel debris), get quotes from a private hauler.</p>'''+SBHHW_P)],
 ["Fontana","San Bernardino","Colton","Grand Terrace"],
 [("Does Rialto offer free bulky item pickup?","Yes. Single-family residential customers get up to two free bulky-item pickups per calendar year through Burrtec, with extra pickups for a fee.")],
 [S_RIA,S_SBHHW], ("Burrtec","2 per year","see city page")),
"redlands": C_("Redlands","San Bernardino",
 "Redlands' older homes and long-time residents mean a lot of estate and downsizing cleanouts: full houses of furniture, attics and sheds, and decades of garage storage. Families often want items that can be donated sorted out from what has to be hauled away.",
 [("Redlands runs its own bulky pickup", '''<p>The City of Redlands says single-family residential customers receive <strong>two free bulky-item pickups per year, with up to three items per collection</strong>. Other items can be collected for a fee as a "special haul." City crews can't go inside a building to collect items, so everything has to be at the curb.</p>'''),
  ("Estate and downsizing cleanouts", '''<p>For a full-house cleanout, ask providers whether they sort donations, how they handle personal papers and photos, and whether they'll sweep out when done. Get the scope in writing, especially if the home is being sold.</p>'''+SBHHW_P)],
 ["Loma Linda","Highland","Yucaipa","San Bernardino"],
 [("How many items can I put out for Redlands bulky pickup?","Up to three items per collection, with two free collections per year for single-family customers. More items can be picked up for a fee."),
  ("Will Redlands crews come inside to get furniture?","No. The city says crews can't enter a building. A private junk removal crew can carry items out.")],
 [S_RED,S_SBHHW], ("City of Redlands","2 per year","3")),
"highland": C_("Highland","San Bernardino",
 "Highland homes near the foothills and in East Highlands Ranch tend to generate a lot of outdoor debris: cut branches, old fencing, worn-out sheds, and leftover materials from yard projects. Inside, garage and move-out cleanouts are the most common jobs.",
 [("Four free pickups a year", '''<p>The City of Highland says each residential customer gets <strong>four free curbside bulky-item collections per calendar year, up to five items each</strong>, through Burrtec. Extra items and extra trips cost more.</p>'''),
  ("Yard and fire-season cleanup", '''<p>Before fire season, many Highland owners clear brush, branches, and dead plants from the yard. Large green-waste loads that won't fit in carts are a good job for a hauler.</p>'''+SBHHW_P)],
 ["San Bernardino","Redlands","Yucaipa","Loma Linda"],
 [("How many free bulky pickups does Highland get?","Four per calendar year, up to five items each, through Burrtec, according to the city.")],
 [S_HIG,S_SBHHW], ("Burrtec","4 per year","5")),
"colton": C_("Colton","San Bernardino",
 "Colton has many older homes, rentals, and small commercial properties. Typical jobs include tenant move-out cleanouts, removing old appliances and mattresses, clearing debris from side yards and lots, and hauling off small renovation leftovers.",
 [("Colton's generous bulky program", '''<p>The City of Colton says each single-family household is entitled to <strong>up to eight bulky-item curbside pickups per year, with a maximum of four items per pickup</strong> (up to 32 items a year), by appointment through CR&amp;R. The city also hosts community dump days four times a year for residents, and CR&amp;R takes old mattresses and box springs free from Colton residents at its Steel Road yard as a Bye Bye Mattress site.</p>'''),
  ("When to hire help", '''<p>Private crews are useful for rental turnovers on a deadline, anything that has to be carried out of a building, and construction debris, which the community dump days don't accept.</p>'''+SBHHW_P)],
 ["San Bernardino","Rialto","Loma Linda","Grand Terrace","Riverside"],
 [("Can I get rid of a mattress for free in Colton?","Yes. The city says CR&R accepts old mattresses and box springs free from Colton residents at its disposal site as part of the Bye Bye Mattress program. Bulky pickups are another option.")],
 [S_COL,S_BBM,S_SBHHW], ("CR&R","up to 8 per year","4")),
"yucaipa": C_("Yucaipa","San Bernardino",
 "Yucaipa's bigger lots leave plenty of room for things to pile up. Homeowners commonly ask for old hot tubs, sheds, and playsets to be taken apart and hauled off, along with brush and yard waste, and full cleanouts when a property changes hands.",
 [("Quarterly bulky pickups", '''<p>The City of Yucaipa says residents can request <strong>up to four curbside bulky-item collections in a 12-month period, up to five items each</strong>, through Yucaipa Disposal (Burrtec). Pickups happen during the second week of February, May, August, and November, and the program also covers electronic waste. Yucaipa Disposal also rents 3-cubic-yard bins for cleanups.</p>'''),
  ("Hot tubs, sheds, and big yard jobs", '''<p>Spas and sheds need to be taken apart, which is beyond curbside pickup. See our <a href="../guides/hot-tub-removal-guide.html">hot tub removal guide</a>. Get quotes from crews that handle demolition and haul-away together.</p>'''+SBHHW_P)],
 ["Redlands","Highland","Loma Linda"],
 [("When are bulky pickups in Yucaipa?","The city says they're scheduled during the second week of February, May, August, and November, up to four per 12 months, with five items each.")],
 [S_YUC,S_SBHHW], ("Yucaipa Disposal (Burrtec)","4 per 12 months","5")),
"rancho-cucamonga": C_("Rancho Cucamonga","San Bernardino",
 "Many Rancho Cucamonga neighborhoods, from Alta Loma to Etiwanda, have HOAs that don't want junk sitting on the driveway or curb for long, so quick, scheduled pickups are popular. Common jobs include furniture and appliance removal, garage cleanouts, and hauling debris after a kitchen or bathroom remodel.",
 [("Four free bulky pickups", '''<p>The City of Rancho Cucamonga says single-family residential customers are eligible for <strong>bulky-item pickups four times per calendar year at no charge</strong> through Burrtec. Furniture and appliances are among the allowable items.</p>'''),
  ("HOA timing", '''<p>If your HOA limits how long items can sit outside, book a hauler for a set time window, or put items out only the night before a scheduled city pickup.</p>'''+SBHHW_P)],
 ["Upland","Fontana","Ontario","Chino"],
 [("Does Rancho Cucamonga have free bulky pickup?","Yes. Single-family residential customers can get four bulky-item pickups per calendar year at no charge through Burrtec, according to the city.")],
 [S_RC,S_SBHHW], ("Burrtec","4 per year","see city page")),
"riverside": C_("Riverside","Riverside",
 "Riverside is a big, varied city, from the historic Wood Streets and downtown to Canyon Crest, Orangecrest, La Sierra, and student rentals near UC Riverside. Move-out cleanouts, furniture and mattress removal, estate cleanouts, and remodel debris are among the most common requests.",
 [("City of Riverside options", '''<p>The City of Riverside offers <strong>two bulky-item appointments per address per year, with up to five items each</strong>. Items must be at the curb (not in the street) by 5:30 a.m., and can't go out more than 24 hours early. Yard waste must be bundled (18 inches across, 36 inches long at most). The city also runs free <strong>drop-off days on the third Saturday of each month at the Agua Mansa Transfer Station</strong> for residents, plus periodic Clean Up Riverside bulky-item and e-waste events.</p>'''),
  ("Student move-outs and rentals", '''<p>End-of-lease periods near UC Riverside bring a rush of couches, mattresses, and desks. If you need things gone the same day you move, a private hauler is usually faster than waiting for a city appointment.</p>'''+RCHHW_P)],
 ["Moreno Valley","Corona","Colton","Grand Terrace"],
 [("How many free bulky pickups does Riverside allow?","Two appointments per address per year, up to five items each. Call the city to schedule."),
  ("Can I drop off bulky items for free in Riverside?","City residents can drop off bulky items and yard waste for free on the third Saturday of each month at Agua Mansa Transfer Station, and at Clean Up Riverside events. Proof of residency is required.")],
 [S_RIV,S_RIV2,S_RCHHW], ("City of Riverside","2 per year","5")),
"ontario": C_("Ontario","San Bernardino",
 "Ontario has established older neighborhoods as well as fast-growing new communities in the south end around Ontario Ranch. Requests range from garage and whole-home cleanouts to hauling off packing materials and old furniture after a move, plus construction leftovers from new builds and remodels.",
 [("Ontario's city-run bulky program", '''<p>The City of Ontario says single-family residents can schedule <strong>up to four bulky-item appointments per calendar year, with five large items per appointment</strong>. Apartment and condo residents go through their property or association manager. The city also holds quarterly Community Cleanup events for residents, and those accept extra items like car tires, scrap metal, and lumber.</p>'''),
  ("New-home moves", '''<p>Moving into a new south Ontario home can leave piles of boxes, packing materials, and old furniture. A single hauler visit can clear it all, and HOA rules often favor quick removal.</p>'''+SBHHW_P)],
 ["Upland","Rancho Cucamonga","Chino","Fontana"],
 [("How many bulky pickups do Ontario residents get?","Single-family residents can schedule up to four per calendar year, five items each. Apartment and condo residents should contact their manager.")],
 [S_ONT,S_SBHHW], ("City of Ontario","4 per year","5")),
"corona": C_("Corona","Riverside",
 "Corona's mix of established neighborhoods near downtown's Grand Boulevard circle and newer hillside communities in south Corona generates steady demand for garage cleanouts, furniture removal, and remodel debris hauling.",
 [("Bulky pickup through Waste Management", '''<p>The City of Corona directs residents to Waste Management for bulky-item pickup. WM's Corona service guide lists the current number of free pickups and item limits, so check it or call WM before scheduling. Hazardous waste, tires, and construction debris generally aren't part of curbside bulky service.</p>'''),
  ("Remodel debris", '''<p>Kitchen and bath remodels leave drywall, cabinets, tile, and flooring that curbside programs won't take. Get quotes that spell out how heavy materials like tile and concrete are priced.</p>'''+RCHHW_P)],
 ["Riverside","Chino","Ontario"],
 [("Who handles bulky item pickup in Corona?","Waste Management, per the City of Corona. Check WM's Corona service guide for current limits.")],
 [S_COR,S_RCHHW], ("Waste Management","see city/WM guide","see city/WM guide")),
"moreno-valley": C_("Moreno Valley","Riverside",
 "Moreno Valley is a large, fast-growing city with many family homes built in the last few decades, from Sunnymead to Moreno Valley Ranch. Garage cleanouts, furniture and appliance removal, and backyard cleanups are the most common requests.",
 [("Frequent free bulky pickups", '''<p>The City of Moreno Valley says residents can request <strong>up to four bulky and/or e-waste pickups per month at no charge</strong> through Waste Management, with additional pickups for a small charge. Items go at the curb by 6 a.m. on your collection day.</p><p>Know the limits: the program <strong>won't take jacuzzi tubs or spas</strong>, trailers, camper shells, hazardous waste, or anything that can't be safely lifted by one person. Those are jobs for a private crew.</p>'''),
  ("Hot tubs and heavy items", '''<p>Since spas are excluded from city pickup, Moreno Valley homeowners usually hire a crew to cut up and haul the tub. See our <a href="../guides/hot-tub-removal-guide.html">hot tub removal guide</a>.</p>'''+RCHHW_P)],
 ["Riverside","Corona","Loma Linda"],
 [("Will Moreno Valley pick up an old hot tub?","No. The city's bulky-item list excludes jacuzzi tubs and spas. Hire a junk removal crew that does spa demolition."),
  ("How many free bulky pickups does Moreno Valley allow?","Up to four bulky and/or e-waste pickups per month at no charge, according to the city.")],
 [S_MV,S_RCHHW], ("Waste Management","up to 4 per month","see city page")),
"upland": C_("Upland","San Bernardino",
 "Upland's older neighborhoods near downtown and the Euclid Avenue corridor, along with foothill homes in north Upland, produce a steady stream of estate cleanouts, garage cleanouts, and yard debris.",
 [("Upland's bulky pickups", '''<p>The City of Upland says residential barrel customers can request <strong>free bulky-item pickups up to four times in a rolling calendar year, with a limit of five items per collection</strong>, through Burrtec. Accepted items include furniture, mattresses, appliances, and electronic waste.</p>'''),
  ("Estate cleanouts", '''<p>Long-held family homes often need a full cleanout before a sale. Ask providers about donation sorting and how they handle documents and keepsakes.</p>'''+SBHHW_P)],
 ["Rancho Cucamonga","Ontario","Chino","Fontana"],
 [("How many free bulky pickups does Upland allow?","Up to four per rolling calendar year, five items each, through Burrtec, according to the city.")],
 [S_UPL,S_SBHHW], ("Burrtec","4 per rolling year","5")),
"chino": C_("Chino","San Bernardino",
 "Chino blends older homes and big agricultural-era parcels with newer neighborhoods like The Preserve. Large-lot cleanups, old sheds and outbuildings, and post-move junk are common jobs.",
 [("Bulky pickup through Waste Management", '''<p>The City of Chino partners with Waste Management for residential bulky-item collection. Eligible residents get a limited number of free pickups each year for furniture, mattresses, appliances, and other large items. Check WM's Chino page for current limits.</p>'''),
  ("Big lots and outbuildings", '''<p>Clearing old sheds, fencing, and decades of stored equipment on a large parcel is usually a multi-load job. Ask for quotes based on truckloads, and mention any heavy metal, concrete, or dirt.</p>'''+SBHHW_P)],
 ["Ontario","Upland","Corona","Rancho Cucamonga"],
 [("Who handles bulky pickup in Chino?","Waste Management, in partnership with the city. Eligible residents get a limited number of free pickups per year.")],
 [S_CHI,S_SBHHW], ("Waste Management","limited free pickups (see WM)","see WM page")),
"hesperia": C_("Hesperia","San Bernardino",
 "Hesperia's large High Desert lots often collect old vehicles' worth of parts, sheds, fencing, and household items over the years. Property cleanups, move-out cleanouts, and hauling off old appliances and furniture are common requests.",
 [("Hesperia's bulky program", '''<p>The City of Hesperia says single-family residents can schedule <strong>four bulky pickups per year, with a maximum of eight bulky items per year</strong>, through Advance Disposal. Schedule at least a week ahead and have items at the curb by 6 a.m. Mattresses, appliances, furniture, carpet, water heaters, and tree stumps over 3 inches in diameter are accepted. TVs, computer monitors, tires, oil, paint, thinners, and glass are not. The city also holds quarterly Neighborhood Beautification Day events for free disposal of mattresses, carpet, furniture, and appliances.</p>'''),
  ("Large-lot cleanups", '''<p>Clearing a big desert lot often means several truckloads plus metal recycling. Ask providers how they handle scrap metal and whether they can separate it.</p>'''+SBHHW_P)],
 ["Victorville"],
 [("How many items can I get picked up for free in Hesperia?","Up to eight bulky items per year, spread over as many as four pickups, through Advance Disposal, according to the city.")],
 [S_HES,S_SBHHW], ("Advance Disposal","4 per year (8 items/year max)","8 per year total")),
"victorville": C_("Victorville","San Bernardino",
 "Victorville's mix of Old Town, newer subdivisions, and rental homes creates steady demand for move-out cleanouts, furniture and appliance removal, and yard and lot cleanups.",
 [("City options for bulky items", '''<p>The City of Victorville's environmental programs pages describe bulky-item disposal options for residents, including scheduled curbside pickup through the city's hauler, a recycling drop-off center, and free dump day events. Check the city's bulky-item page for current limits before you schedule.</p>'''),
  ("Rental turnovers", '''<p>Landlords often need a unit emptied fast between tenants. A hauler can clear everything in one visit and send photos when it's done.</p>'''+SBHHW_P)],
 ["Hesperia"],
 [("Does Victorville offer bulky item pickup?","Yes. The city's bulky-item disposal page describes curbside pickup through its hauler and drop-off options for residents. Check the page for current limits.")],
 [S_VIC,S_SBHHW], ("Victorville's city hauler","see city page","see city page")),
"loma-linda": C_("Loma Linda","San Bernardino",
 "Loma Linda's mix of family homes, hillside properties, and rentals near Loma Linda University and its medical center means regular move-outs, furniture removal, and cleanouts between tenants.",
 [("Two free pickups a year", '''<p>The City of Loma Linda says residents with the three-cart trash, recycling, and green waste service get <strong>two free bulky-item pickups per calendar year</strong> through CR&amp;R. Televisions, computer monitors, tires, and concrete are among the items not accepted.</p>'''),
  ("Student and staff move-outs", '''<p>University and hospital-related moves often come with tight timelines. If you need items gone on moving day, schedule a hauler in advance.</p>'''+SBHHW_P)],
 ["Redlands","San Bernardino","Colton","Grand Terrace","Highland"],
 [("Does Loma Linda offer free bulky item pickup?","Yes. Residents with the three-cart service get two free bulky-item pickups per calendar year through CR&R, according to the city.")],
 [S_LL,S_SBHHW], ("CR&R","2 per year","see city page")),
"grand-terrace": C_("Grand Terrace","San Bernardino",
 "Grand Terrace is a small hillside city between Colton and Riverside. Sloped lots and tight side yards can make hauling harder, and common jobs include garage cleanouts, furniture removal, and yard debris.",
 [("City bulky collection", '''<p>The City of Grand Terrace lists bulky-item collection and e-waste collection among its residential trash services, through Burrtec. Contact Burrtec before your collection day to schedule, and check the city's page for current limits.</p>'''),
  ("Access matters", '''<p>Stairs, steep driveways, and long carries affect quotes. Mention them in your request so providers can price the job accurately.</p>'''+SBHHW_P)],
 ["Colton","Riverside","Loma Linda","San Bernardino"],
 [("Does Grand Terrace have bulky item pickup?","Yes. The city lists bulky-item collection among its Burrtec residential services. Contact Burrtec to schedule.")],
 [S_GT,S_SBHHW], ("Burrtec","see city page","see city page")),
}
for k,v in CITIES.items():
    assert v["name"].lower().replace(" ","-")==k, k

def CITY_TITLE(c): return f"Junk Removal in {c['name']}, CA | Free Quotes & Bulky Pickup"
def CITY_DESC(c): return f"Free junk removal quotes in {c['name']}, CA for furniture, appliances, cleanouts, and debris, plus how the city's free bulky-item pickup works."
def CITY_H1(c): return f"Junk removal quotes in {c['name']}, CA"
CITY_JOBS_H2 = "Junk removal services in {city}"
CITY_LINK_TEXT = "{city} junk removal"
def CITY_FAQ_COMMON(c):
    return [(f"How much does junk removal cost in {c['name']}?", f"Pricing mostly depends on how much truck space your items take, plus heavy materials, stairs or long carries, and disposal fees. Compare a few quotes from {c['name']}-area providers. See our <a href=\"../guides/junk-removal-cost-factors.html\">cost factors guide</a>.")]

HOME_TITLE = "Junk Removal Quotes | San Bernardino, Riverside & IE | IE Junk Quotes"
HOME_DESC = "Free junk removal quotes for furniture, appliances, cleanouts, yard waste, debris, and hot tubs in 18 Inland Empire cities, plus guides to free city bulky pickup."
HERO_HTML = '''<h1>Junk removal and cleanout quotes in the Inland Empire</h1>
<p>Tell us what needs to go, once, and we'll connect you with local junk removal providers in San Bernardino, Fontana, Riverside, Redlands, and nearby cities. It's free, and you don't have to hire anyone.</p>
<ul class="checks"><li>One short request, free quotes from local haulers</li><li>Furniture, appliances, cleanouts, yard waste, debris</li><li>No cost and no obligation to hire</li></ul>'''
QUICK_DETAILS_LABEL = "What needs to go?"
QUICK_DETAILS_PLACEHOLDER = "e.g. old couch, broken fridge, and about half a garage of boxes"
HOME_DISCLOSURE = f"<strong>Plain-English disclosure:</strong> {BRAND} is a referral service, not a junk removal company. We pass your request to independent local providers who can contact you. We don't do the work, and we can't vouch for any provider's pricing, insurance, or disposal practices, so please check before you hire."
HOME_SERVICES_H2 = "Junk removal services we can help you find"
HOME_HOW_HTML = '''<h2>How it works</h2><ol><li><strong>Tell us what needs to go</strong>: the items, roughly how much, where they are (curb, garage, inside, upstairs), and when you need it done.</li><li><strong>We match you</strong> with independent junk removal providers who serve your city.</li><li><strong>Compare quotes</strong> and hire whoever you choose, or nobody at all.</li></ol><p>Only a few items? Your city may pick them up for free. See our <a href="guides/free-bulky-item-pickup-inland-empire.html">bulky pickup guide</a>.</p>'''
TIPS_H2 = "Tips before you hire a junk removal service"
TIPS_HTML = '''<ul><li>Get two or three quotes, and make sure each one says what's included: loading, carrying from inside or upstairs, sweeping up, and disposal or recycling fees.</li><li>Ask how pricing works (by truck volume, by item, or by weight) and whether the price can change once the crew sees the load.</li><li>Ask for proof of liability insurance, especially if the crew will be working inside your home.</li><li>For demolition (sheds, decks, built-in spas), ask whether the company holds a contractor's license and look it up at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a>.</li><li>Ask where the load goes. A hauler who dumps illegally to save on fees is a red flag.</li><li>For just a few bulky items, check your city's free bulky pickup first. See our <a href="guides/free-bulky-item-pickup-inland-empire.html">city-by-city guide</a>.</li><li>Keep hazardous materials (paint, chemicals, batteries, propane) separate. Most haulers can't take them.</li></ul>'''
HOME_FAQ = [("Is this service free?","Yes. Requesting quotes through this site is free, and you don't have to hire anyone."),
("Are you a junk removal company?","No. We're a referral service that connects you with independent local junk removal providers. We don't haul anything ourselves."),
("How much does junk removal cost?","It depends mostly on how much space your items take up in the truck, plus what they are (heavy materials like concrete, dirt, or roofing cost more), how far they have to be carried, stairs, and local disposal fees. See our <a href=\"guides/junk-removal-cost-factors.html\">cost factors guide</a>."),
("What won't junk haulers take?","Most won't take hazardous materials such as paint, solvents, motor oil, pesticides, pool chemicals, propane tanks, car batteries, or anything that might contain asbestos. San Bernardino and Riverside counties run free household hazardous waste programs for residents."),
("Can my city pick up bulky items for free?","Most Inland Empire cities offer some free bulky-item pickups through their trash hauler, usually a few per year with item limits. See our <a href=\"guides/free-bulky-item-pickup-inland-empire.html\">city-by-city guide</a>."),
("Where does my stuff go?","It depends on the provider. Reputable haulers take loads to licensed transfer stations, landfills, recyclers, and donation centers. If donation or recycling matters to you, ask about it when you compare quotes.")]

SERVICES_TITLE = "Junk Removal Services: Furniture, Cleanouts, Debris | IE Junk Quotes"
SERVICES_DESC = "Furniture and appliance removal, garage and home cleanouts, yard waste, construction debris, hot tub and shed removal, and estate cleanouts in the Inland Empire."
SERVICES_H1 = "Junk removal services in the Inland Empire"
SERVICES_INTRO = "These are the jobs people ask about most. Send one request, and local providers can quote it."
SERVICES_NOTE = "Prices depend on how much there is, what it is, how hard it is to reach, and disposal fees. The only reliable number is a written quote from a provider who has seen the items or clear photos of them."
SERVICES_EXTRA = '''<h2>Not sure what can go?</h2><p>Most providers take furniture, appliances, electronics, mattresses, boxes, yard waste, and construction leftovers. Hazardous materials usually need to go through your county's program instead. See our <a href="guides/household-hazardous-waste-disposal-inland-empire.html">hazardous waste guide</a>, plus our guides to <a href="guides/old-mattress-disposal-riverside-county.html">mattress disposal</a> and <a href="guides/hot-tub-removal-guide.html">hot tub removal</a>.</p>'''
AREAS_TITLE = "Junk Removal Service Areas: 18 Inland Empire Cities | IE Junk Quotes"
AREAS_DESC = "Junk removal quotes in 18 Inland Empire cities, including San Bernardino, Riverside, Fontana, Ontario, Corona, Moreno Valley, Redlands, and Rancho Cucamonga."
GUIDES_TITLE = "Junk Disposal Guides for Inland Empire Residents | IE Junk Quotes"
GUIDES_DESC = "Sourced guides on free city bulky-item pickup, mattress disposal, hot tub removal, hazardous waste drop-off, junk removal costs, and estate cleanouts."
GUIDES_INTRO = "Practical, sourced answers about getting rid of stuff in the Inland Empire, including the free options many people don't know about."
HOW_TITLE = "How It Works | IE Junk Quotes"
HOW_DESC = "How our free junk removal referral works: what we do with your request, how to get accurate quotes, and what we are and aren't."
HOW_BODY = f'''<h1>How {BRAND} works</h1>
<p>We're a small, independent referral service in the Inland Empire. We built this site so you can find someone to haul away junk without calling a dozen companies.</p>
<ol><li>You fill out the <a href="contact.html">quote request form</a>.</li><li>We review it and share your job details and contact information with one or more independent junk removal providers who serve your area.</li><li>Providers contact you directly to ask questions, look at photos, or schedule a quick estimate.</li><li>You decide who to hire, if anyone. Your agreement is directly with that provider.</li></ol>
<h2>Getting accurate quotes</h2><ul><li>Describe the amount in plain terms: "a few items," "about a pickup truck load," "a full one-car garage."</li><li>Mention anything heavy (concrete, dirt, tile, a piano) or hard to reach (stairs, a long walk from the truck, a tight side yard).</li><li>Have photos ready. Many providers can quote from photos.</li></ul>
<h2>What we are, and what we aren't</h2><ul><li>We're <strong>not</strong> a junk removal company and we don't haul anything.</li><li>We don't guarantee any provider's work, price, insurance, or disposal practices.</li><li>We may receive a fee from providers for referrals. It never costs you anything.</li><li>We don't post fake reviews or ratings.</li></ul>
<h2>Junk removal companies</h2><p>Do you run an insured junk removal or hauling business in the Inland Empire and want more local jobs? <a href="contact.html?type=provider">Get in touch</a>.</p>'''
CONTACT_TITLE = "Get Free Junk Removal Quotes | IE Junk Quotes"
CONTACT_DESC = "Request free quotes for furniture and appliance removal, cleanouts, yard waste, construction debris, or hot tub and shed removal in the Inland Empire."
CONTACT_H1 = "Get free junk removal quotes"
CONTACT_NOTE = "Have hazardous materials (paint, chemicals, oil, batteries, propane, or possible asbestos)? Most haulers can't take them. Use your county's household hazardous waste program for those."
CONTACT_EXTRA_FIELDS = '<label for="location">Where are the items?</label><select id="location" name="location"><option>Curb or driveway</option><option>Garage</option><option selected>Inside the home</option><option>Upstairs / no elevator</option><option>Backyard or side yard</option><option>Several places</option></select>\n<label for="timing">How soon?</label><select id="timing" name="timing"><option>As soon as possible</option><option>Within a week</option><option selected>Within a month</option><option>Just getting prices</option></select>'
CONTACT_DETAILS_LABEL = 'What needs to go? (items, rough amount like "half a pickup" or "a full garage," anything heavy like concrete or a piano)'
THANKS_TEXT = "We'll review it and pass it to local junk removal providers who serve your area. They'll contact you directly. Before you hire, confirm the price, what's included, and how your items will be disposed of."
FOOTER_DISCLOSURE = f'<strong>{BRAND}</strong> is a free referral service. We are <strong>not a junk removal company</strong>: we don\'t haul anything, and we don\'t hold a contractor\'s license. When you send a request, we pass it to independent local junk removal providers who can contact you with quotes. Any provider you hire is solely responsible for its work, licensing, insurance, and how it disposes of your items. Ask for proof of insurance before hiring, and for demolition work (sheds, decks, built-in spas), check the contractor\'s license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a>.'
FOOTER_AREA = "Serving San Bernardino County, western Riverside County, and the High Desert."

def _bulky_table():
    rows = "".join(f'<tr><td><a href="../areas/{k}.html">{c["name"]}</a></td><td>{c["bulky"][0].replace("&","&amp;")}</td><td>{c["bulky"][1]}</td><td>{c["bulky"][2]}</td><td><a href="{c["sources"][0][1]}" rel="nofollow noopener" target="_blank">city page</a></td></tr>' for k,c in CITIES.items())
    return f'<div class="tablewrap"><table><thead><tr><th>City</th><th>Hauler</th><th>Free pickups</th><th>Items per pickup</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>'

GUIDES = [
dict(slug="free-bulky-item-pickup-inland-empire", nav="Free bulky pickup by city", img="hero", all_cities=True,
 title="Free Bulky Item Pickup: San Bernardino, Riverside & IE (2026)",
 h1="Free bulky item pickup in San Bernardino, Riverside, and other Inland Empire cities",
 desc="City-by-city guide to free bulky-item pickup in the Inland Empire: how many free pickups you get, item limits, what's excluded, and when to hire a hauler instead.",
 blurb="How many free curbside pickups your city gives you, item limits, and what they won't take.",
 body='''<p>Before paying anyone to haul away a couch or a fridge, check your city's bulky-item program. Most Inland Empire cities include some free curbside pickups with residential trash service. Here's what each city's official page says.</p>
<h2>City-by-city summary</h2>'''+_bulky_table()+'''<p class="small">Where we couldn't confirm a number on an official page, we say "see city page." Programs usually apply to single-family residential trash customers; apartment residents often go through their property manager.</p>
<h2>What's usually excluded</h2><ul><li>Construction and demolition debris, concrete, rock, and dirt (San Bernardino, Rialto, and Loma Linda say so explicitly)</li><li>Household hazardous waste: paint, oil, batteries, chemicals</li><li>Hot tubs and spas (Moreno Valley lists them as excluded) and anything one or two workers can't safely lift</li><li>Some cities exclude TVs and monitors from curbside bulky pickup (Hesperia, Loma Linda), so ask about e-waste</li></ul>
<h2>Tips for a smooth pickup</h2><ol><li>Schedule ahead. Many cities ask for a week's notice.</li><li>List every item when you call. Extra items can be left behind or count as another pickup.</li><li>Put items out only when your city allows. Riverside, for example, says no more than 24 hours early.</li><li>Bundle yard waste to the city's size limits.</li></ol>
<h2>When to hire a hauler instead</h2><p>Private junk removal makes sense when you have more than the item limit, need things carried out of the house (Redlands says its crews can't enter buildings), have remodel debris or a hot tub, or can't wait for the next available pickup date.</p>''',
 faq=[("Does San Bernardino have free bulky item pickup?","Yes. Two free collections per year, up to five items each, through Burrtec."),("Does Riverside have free bulky item pickup?","Yes. Two appointments per address per year, up to five items each, plus free drop-off days at Agua Mansa Transfer Station on the third Saturday of each month for city residents."),("Which IE city has the most free bulky pickups?","Among the cities we checked, Moreno Valley allows up to four bulky or e-waste pickups per month, and Colton allows up to eight pickups (32 items) per year.")],
 sources=[S_SB,S_RIV,S_RIV2,S_FON,S_RIA,S_RED,S_HIG,S_COL,S_YUC,S_RC,S_ONT,S_COR,S_MV,S_UPL,S_CHI,S_HES,S_VIC,S_LL,S_GT]),
dict(slug="old-mattress-disposal-riverside-county", nav="Mattress disposal", img="hero",
 cities=["riverside","moreno-valley","corona","colton","san-bernardino","ontario","fontana","hesperia"],
 title="How to Get Rid of an Old Mattress in Riverside County",
 h1="How to get rid of an old mattress in Riverside County and the Inland Empire",
 desc="Free ways to dispose of a mattress in Riverside and San Bernardino counties: retailer take-back, Bye Bye Mattress drop-off sites, and city bulky pickup.",
 blurb="Retailer take-back, free Bye Bye Mattress drop-off sites, and city pickup options.",
 body='''<p>Mattresses are one of the most common items people want hauled away, and California has free options most people don't know about.</p>
<h2>1. Make the retailer take it when you buy a new one</h2><p>Under California's mattress recycling program, a retailer delivering a new mattress must offer to pick up your used one at no charge. For online orders shipped by carrier, pickup must be arranged within 30 days. Delivery or setup fees can still apply, and a retailer can refuse a mattress that's contaminated (for example with bedbugs) or poses a safety risk.</p>
<h2>2. Drop it off free at a Bye Bye Mattress site</h2><p>The Mattress Recycling Council's Bye Bye Mattress program runs no-cost collection sites across California, which you can find on its locator. In San Bernardino County, Colton's hauler CR&amp;R takes mattresses and box springs free from Colton residents. Limits and appointments vary by site.</p>
<h2>3. Use your city's bulky-item pickup</h2><ul><li><strong>Riverside:</strong> two bulky appointments per year, up to five items each (no more than five mattresses per appointment), plus free drop-off days on the third Saturday of each month at Agua Mansa Transfer Station for residents.</li><li><strong>Moreno Valley:</strong> up to four bulky or e-waste pickups per month at no charge. Mattresses are on the accepted list.</li><li><strong>Corona:</strong> bulky pickup through Waste Management. Check WM's Corona guide for mattress prep rules.</li></ul><p>See all cities in our <a href="free-bulky-item-pickup-inland-empire.html">bulky pickup guide</a>.</p>
<h2>4. Hire a hauler</h2><p>If the mattress is upstairs, you have several, or you're clearing a whole room, a junk removal crew can carry it out. Ask whether they recycle mattresses.</p>
<p><strong>Don't dump it.</strong> Illegally dumped mattresses are a big problem in the region, and cities pay to clean them up.</p>''',
 faq=[("Do mattress stores have to take my old mattress in California?","When delivering a new mattress, a retailer must offer to pick up your used one at no charge, though delivery fees may apply and contaminated mattresses can be refused."),("Where can I drop off a mattress for free near Riverside?","Use the Bye Bye Mattress locator for no-cost sites. City of Riverside residents can also use the free third-Saturday drop-off at Agua Mansa Transfer Station.")],
 sources=[S_BBM,S_BBMFAQ,S_RIV,S_RIV2,S_MV,S_COR,S_COL]),
dict(slug="hot-tub-removal-guide", nav="Hot tub removal", img="yard",
 cities=["moreno-valley","yucaipa","riverside","corona","rancho-cucamonga","hesperia","fontana","redlands"],
 title="Hot Tub Removal in the Inland Empire: Steps, Costs & Tips",
 h1="Hot tub and spa removal: what to know before you hire",
 desc="How old hot tubs get removed in the Inland Empire: power disconnect, draining, demolition, what drives the price, and why city pickup won't take spas.",
 blurb="Power disconnect, draining, demolition, cost factors, and why city pickup won't take a spa.",
 body='''<p>An old hot tub is one of the hardest things to get rid of yourself. Spas are heavy, bulky, and wired into your electrical system, and city bulky programs generally won't take them. Moreno Valley's bulky-item list, for example, explicitly excludes jacuzzi tubs and spas.</p>
<h2>Step by step</h2><ol><li><strong>Disconnect power.</strong> Have a qualified electrician shut off and disconnect the spa's dedicated circuit before anyone starts cutting. Don't let a hauler cut live wiring.</li><li><strong>Drain it.</strong> Drain the water a day or two ahead. Check your city's rules on where pool and spa water can go. Many cities don't allow chlorinated water into storm drains.</li><li><strong>Whole removal or cut-up.</strong> If there's a clear path, some crews remove the spa whole on a dolly or trailer. Otherwise they cut it into sections on site.</li><li><strong>Haul and clean up.</strong> Make sure the quote covers debris, the cover and steps, and sweeping the pad.</li><li><strong>The pad.</strong> Removing a concrete pad is a separate, heavier job. Mention it if you want it gone.</li></ol>
<h2>What drives the price</h2><ul><li>Size and weight of the spa</li><li>Access: gates, stairs, slopes, and distance to the truck</li><li>Whether it's above-ground or built into a deck or the ground (in-ground or deck-built spas are demolition work)</li><li>Electrical disconnect (usually a separate electrician)</li><li>Concrete pad or deck removal</li></ul>
<h2>Licensing</h2><p>Simple haul-away isn't usually contractor work, but tearing out a built-in spa, deck, or concrete can be. California requires a CSLB license for jobs of $1,000 or more in labor and materials (or any job needing a permit). Ask, and check the license at cslb.ca.gov.</p>''',
 faq=[("Will the city pick up my old hot tub?","Usually not. Moreno Valley's bulky program explicitly excludes spas, and most programs exclude items too heavy for the crew to lift safely. Hire a junk removal crew."),("Do I need an electrician to remove a hot tub?","Yes, have a qualified electrician disconnect the spa's circuit before removal.")],
 sources=[S_MV,S_MINOR]),
dict(slug="junk-removal-cost-factors", nav="Junk removal cost", img="boxes", all_cities=True,
 title="How Much Does Junk Removal Cost? Inland Empire Price Factors",
 h1="How much does junk removal cost in the Inland Empire?",
 desc="What drives junk removal prices in the Inland Empire: truck volume, heavy materials, stairs, disposal fees, and same-day service, plus how to compare quotes.",
 blurb="Volume, weight, access, and disposal fees: what really drives the price, and how to compare quotes.",
 body='''<p>We don't publish price ranges, because we haven't found a reliable, current, Inland Empire-specific source, and national averages can be misleading. Here's what actually drives the price so you can compare quotes fairly. Remember that a few items may be free through your city. See our <a href="free-bulky-item-pickup-inland-empire.html">bulky pickup guide</a>.</p>
<h2>The main cost factors</h2><ul><li><strong>Volume.</strong> Many haulers price by how much of the truck your items fill (a few items, a quarter load, a full load).</li><li><strong>Weight and material.</strong> Concrete, dirt, tile, roofing, and other dense materials cost more to haul and dispose of, and may need a different truck or several trips.</li><li><strong>Labor and access.</strong> Items inside, upstairs, or far from the truck take longer than a curbside pile. Mention stairs and long carries.</li><li><strong>Disassembly.</strong> Hot tubs, sheds, playsets, and built-ins need to be taken apart first.</li><li><strong>Special handling.</strong> Appliances with refrigerant, mattresses, tires, and electronics may carry extra disposal or recycling fees.</li><li><strong>Timing.</strong> Same-day or weekend service may cost more.</li></ul>
<h2>How to compare quotes</h2><ol><li>Send the same photos and description to each provider.</li><li>Ask whether the quote is a firm price or an estimate that can change when they see the load.</li><li>Ask what's included: loading, sweeping, disposal fees, and recycling or donation.</li><li>Ask for proof of insurance, and ask where the load will go.</li></ol>''',
 faq=[("Is junk removal priced by weight or volume?","Usually by volume (how much truck space you fill), with extra charges for heavy materials or special items. Ask each provider how they price."),("Can I get a junk removal quote from photos?","Many providers will quote from clear photos and a description, then confirm on site.")],
 sources=[S_SB,S_RIV]),
dict(slug="household-hazardous-waste-disposal-inland-empire", nav="Hazardous waste disposal", img="boxes", all_cities=True,
 title="Household Hazardous Waste Drop-Off in San Bernardino & Riverside",
 h1="Where to take paint, chemicals, batteries, and other hazardous waste in the Inland Empire",
 desc="What junk haulers can't take, and where Inland Empire residents can drop off paint, oil, batteries, and chemicals free through county programs.",
 blurb="What haulers won't take, and the free county drop-off programs for paint, oil, batteries, and chemicals.",
 body='''<p>Most junk removal crews can't legally take household hazardous waste (HHW) to a regular landfill, and California bans throwing many of these items in the trash. Both counties in the Inland Empire run free programs for residents.</p>
<h2>What counts as household hazardous waste</h2><ul><li>Paint, stains, and solvents</li><li>Motor oil, oil filters, and antifreeze</li><li>Batteries (California prohibits putting any batteries in the trash)</li><li>Pesticides, pool chemicals, and cleaners</li><li>Fluorescent bulbs</li><li>Propane cylinders (ask the facility)</li></ul>
<h2>San Bernardino County</h2><p>San Bernardino County Fire runs household hazardous waste collection facilities that are free for county residents. Proof of residency may be requested, and business waste isn't accepted. Check the county's facility list for the nearest site and its hours, which include a central site at San Bernardino International Airport and a Saturday site at the Redlands city yard.</p>
<h2>Riverside County</h2><p>The Riverside County Department of Waste Resources runs free permanent HHW facilities (including Agua Mansa near Riverside) and temporary collection events. There's a limit of 15 gallons or 125 pounds per resident per trip.</p>
<h2>Tips</h2><ul><li>Keep products in their original containers with lids on, and never mix chemicals.</li><li>Transport containers upright and secured, away from passengers if possible.</li><li>Tell your junk removal provider about any HHW in advance so they can quote the rest of the job without it.</li></ul>''',
 faq=[("Will junk removal companies take paint?","Usually not. Most can't take wet paint or other hazardous waste. Use your county's free HHW program."),("Is hazardous waste drop-off free in Riverside County?","Yes, for residents, at county HHW facilities and events, with a limit of 15 gallons or 125 pounds per trip.")],
 sources=[S_SBHHW,S_SBHHW2,S_RCHHW,S_RCHHWF,S_YUC]),
dict(slug="estate-cleanout-checklist", nav="Estate cleanout checklist", img="boxes", all_cities=True,
 title="Estate Cleanout Checklist for Inland Empire Families",
 h1="Estate cleanout checklist: how to clear a loved one's home",
 desc="A step-by-step estate cleanout checklist: securing documents and valuables, sorting keep, donate, and toss, free city disposal options, and hiring a cleanout crew.",
 blurb="Documents first, then keep, donate, and toss. A practical order of operations, plus when to bring in a crew.",
 body='''<p>Clearing out a parent's or relative's home is emotional and often time-sensitive, especially when the house is being sold or a rental lease is ending. This checklist covers the practical side.</p>
<h2>Before anything leaves the house</h2><ol><li><strong>Confirm who has authority</strong> to remove property (executor, trustee, or the heirs together). When in doubt, ask the estate's attorney.</li><li><strong>Secure documents and valuables:</strong> wills and trust papers, deeds, titles, bank and tax records, jewelry, photos, keys, and passwords.</li><li><strong>Photograph rooms</strong> before sorting, for records and to settle family questions later.</li></ol>
<h2>Sort into four groups</h2><ul><li><strong>Keep:</strong> items family members want. Label them and move them first.</li><li><strong>Sell:</strong> valuable furniture, collectibles, and vehicles. Consider an appraiser or estate sale company.</li><li><strong>Donate:</strong> usable furniture, clothing, and housewares.</li><li><strong>Dispose:</strong> broken items, trash, and anything left over.</li></ul>
<h2>Use free options for part of the load</h2><p>Your city's free bulky-item pickups can take some furniture and appliances. See our <a href="free-bulky-item-pickup-inland-empire.html">city-by-city guide</a>. Paint, chemicals, and batteries should go to the county's free <a href="household-hazardous-waste-disposal-inland-empire.html">hazardous waste program</a>.</p>
<h2>Bringing in a cleanout crew</h2><ul><li>Ask whether they sort donations and recycling, and whether they provide donation receipts.</li><li>Ask how they handle papers and photos they find (set aside, never discarded).</li><li>Get a firm written price and scope, including sweeping out.</li><li>Ask for proof of insurance.</li></ul>''',
 faq=[("Should I hire an estate sale company or a junk removal company?","Often both: an estate sale company to sell valuable items first, then a cleanout crew for what's left."),("Can a junk removal crew donate items from an estate?","Many can set aside usable items for donation. Ask when you compare quotes.")],
 sources=[S_SB,S_SBHHW]),
]

CSS = """
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1c2633;line-height:1.6;background:#fff}
a{color:#1f5f99}img{max-width:100%;height:auto}
header{background:#1b3554;color:#fff}header .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding-top:.7rem;padding-bottom:.7rem}
.brand{color:#fff;text-decoration:none;font-weight:700;font-size:1.15rem;white-space:nowrap}
nav{display:flex;gap:1.1rem}nav a{color:#e3ecf6;text-decoration:none;font-size:.95rem;white-space:nowrap}nav a:hover{color:#fff;text-decoration:underline}
nav a.nav-cta{background:#f2b33d;color:#1c2633;font-weight:700;padding:.3rem .8rem;border-radius:999px}nav a.nav-cta:hover{color:#1c2633;text-decoration:none;background:#f7c45e}
.wrap{max-width:1080px;margin:0 auto;padding:1rem 1.25rem}
.hero{position:relative;overflow:hidden;color:#fff;background:#1b3554}.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 45%;z-index:0}
.hero:before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(100deg,rgba(14,30,50,.92) 0%,rgba(20,42,68,.82) 50%,rgba(20,42,68,.55) 100%)}
.hero .wrap{position:relative;z-index:2;display:grid;grid-template-columns:1.15fr 1fr;gap:2rem;align-items:center;padding-top:2.5rem;padding-bottom:2.5rem}
.hero h1{font-size:2.2rem;line-height:1.2;margin:.25rem 0 .75rem;text-shadow:0 1px 3px rgba(0,0,0,.35)}.hero p{font-size:1.1rem;max-width:620px;text-shadow:0 1px 2px rgba(0,0,0,.35)}
.hero ul.checks{list-style:none;padding:0;margin:1rem 0}.hero ul.checks li{margin:.3rem 0;padding-left:1.6rem;position:relative}.hero ul.checks li:before{content:"\\2713";position:absolute;left:0;color:#f2b33d;font-weight:700}
.quote-card{background:#fff;color:#1c2633;border-radius:12px;padding:1.25rem 1.25rem 1rem;box-shadow:0 10px 30px rgba(0,0,0,.28)}
.quote-card h2{margin:0 0 .25rem;font-size:1.3rem}.quote-card p,.quote-card p.small{font-size:.85rem;text-shadow:none;margin:.4rem 0}.quote-card form label{margin-top:.55rem;font-size:.93rem}
.quote-card form textarea{min-height:70px}.quote-card .row{display:grid;grid-template-columns:1fr 1fr;gap:0 .75rem}
.btn{display:inline-block;background:#f2b33d;color:#1c2633;padding:.8rem 1.4rem;border-radius:6px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:1rem}.btn:hover{background:#f7c45e}
.btn-block{display:block;width:100%;text-align:center}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}.card{border:1px solid #dbe4ee;border-radius:8px;padding:1rem;background:#f8fbfe}
.card h3{margin-top:0}.note{background:#fff8e6;border-left:4px solid #f2b33d;padding:.8rem 1rem;border-radius:4px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;align-items:center}.photo{display:block;width:100%;border-radius:10px;object-fit:cover}
.split .photo{aspect-ratio:3/2}.svc{display:grid;grid-template-columns:260px 1fr;gap:1.25rem;align-items:start;margin:1.5rem 0}.svc .photo{aspect-ratio:4/3;margin-top:1.2rem}.svc h2{margin-top:.6rem}
form label{display:block;font-weight:600;margin-top:.8rem}form input,form select,form textarea{width:100%;padding:.6rem;border:1px solid #b6c4d3;border-radius:6px;font:inherit;background:#fff;color:inherit}
form label.consent{font-weight:400;font-size:.88rem;display:flex;gap:.5rem;align-items:flex-start}form label.consent input{width:auto;margin-top:.3rem;flex:none}
form textarea{min-height:110px}.small{font-size:.85rem;color:#4a5868}footer{background:#eef3f8;margin-top:2rem;font-size:.9rem}footer .credits{font-size:.78rem;color:#5a6878}
.crumbs{font-size:.85rem;margin:.25rem 0 .5rem;color:#4a5868}.crumbs a{color:inherit}
ul.sources{font-size:.85rem;padding-left:1.2rem}h2.h3{font-size:1.15rem;margin-top:0}.card h3 a,.card h2 a{text-decoration:none}
.guide>.photo{aspect-ratio:16/9;max-height:440px;margin:1rem 0}
.tablewrap{overflow-x:auto;margin:1rem 0}table{border-collapse:collapse;width:100%;font-size:.92rem}th,td{border:1px solid #dbe4ee;padding:.45rem .6rem;text-align:left;vertical-align:top}th{background:#eef3f8}
ul.cities{columns:2;padding-left:1.2rem}.mobile-cta{display:none}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr;gap:1.25rem;padding-top:1.5rem;padding-bottom:1.75rem}.split{grid-template-columns:1fr}}
@media(max-width:640px){
header .wrap{flex-direction:column;align-items:stretch;gap:.35rem;padding-top:.6rem;padding-bottom:0}.brand{font-size:1.05rem;white-space:normal}
nav{overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;gap:1rem;padding:.25rem 0 .6rem;margin:0 -1.25rem;padding-left:1.25rem;padding-right:1.25rem}nav::-webkit-scrollbar{display:none}nav a{font-size:.92rem}nav a.nav-cta{display:none}
.hero h1{font-size:1.6rem}.hero p{font-size:1rem}.hero ul.checks{display:none}.quote-card{padding:1rem}.quote-card .row{grid-template-columns:1fr}
.svc{grid-template-columns:1fr;gap:0}.svc .photo{margin-top:.5rem}
body.has-mcta{padding-bottom:76px}.mobile-cta{display:block;position:fixed;left:0;right:0;bottom:0;z-index:50;padding:.6rem 1rem calc(.6rem + env(safe-area-inset-bottom));background:rgba(255,255,255,.96);box-shadow:0 -2px 12px rgba(0,0,0,.15)}
.mobile-cta a{display:block;text-align:center;background:#f2b33d;color:#1c2633;font-weight:700;text-decoration:none;padding:.75rem;border-radius:8px;font-size:1.05rem}
}
"""
