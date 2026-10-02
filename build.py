import os, json, datetime
BASE = "https://bryanbyfield0-creator.github.io/ie-junk-quotes"
BRAND = "Inland Empire Junk Removal Quotes"
EMAIL = "bryanbyfield0@gmail.com"
PHONE = "909-361-0443"
# FormSubmit endpoint. Plain email for now; after activation, FormSubmit gives a hashed alias you can swap in here.
FORM_ACTION = "https://formsubmit.co/f205ca1265cc5630d4c6253a9913f917"
# Free-license photos (self-hosted in img/). Pexels License / Unsplash License: commercial use OK, no attribution required; credited anyway.
# (src, w, h, alt, photographer, photographer_url, site, photo_url, license)
PHOTOS = {
 "hero": ("img/movers-carrying-sofa.jpg", 1600, 1066, "Two workers lifting a green sofa to carry it out of an empty room", "RDNE Stock project", "https://www.pexels.com/@rdne/", "Pexels", "https://www.pexels.com/photo/two-men-carrying-a-sofa-7464266/", "Pexels License"),
 "boxes": ("img/pile-of-moving-boxes.jpg", 1600, 1066, "Pile of empty cardboard boxes in the corner of an empty room after a move-out", "SHVETS production", "https://www.pexels.com/@shvets-production/", "Pexels", "https://www.pexels.com/photo/pile-of-brown-empty-boxes-in-the-corner-of-the-room-7203702/", "Pexels License"),
 "yard": ("img/yard-waste-branches.jpg", 1600, 1066, "Pile of cut branches and logs waiting to be hauled away", "K8", "https://unsplash.com/@_k8_", "Unsplash", "https://unsplash.com/photos/9_U9Dt-bKWQ", "Unsplash License"),
}
def img(key, rel="", cls="photo"):
    src,w,h,alt,*_ = PHOTOS[key]
    return f'<img class="{cls}" src="{rel}{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">'
def hidden_fields():
    return f"""<input type="hidden" name="_subject" value="New junk removal quote request">
<input type="hidden" name="_next" value="{BASE}/thank-you.html">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">"""
TODAY = datetime.date.today().isoformat()

# slug: (name, blurb, nearby)
CITIES = {
 "san-bernardino": ("San Bernardino", "San Bernardino has a large stock of older single-family homes and rentals, so cleanouts between tenants, estate cleanouts, and hauling off old furniture and appliances come up constantly. Owners of foothill properties also deal with yard debris and the occasional old shed or fence that needs to go.", ["Highland","Rialto","Colton","Loma Linda"]),
 "fontana": ("Fontana", "Fontana mixes established neighborhoods with large lots and newer tracts. Common requests include clearing out packed garages, hauling off old patio sets and playsets, removing yard waste after a big cleanup, and taking away leftover materials after a remodel.", ["Rialto","Rancho Cucamonga","Ontario","San Bernardino"]),
 "rialto": ("Rialto", "In Rialto, junk removal requests often start with a garage that's become a storage unit, a backyard with years of accumulated stuff, or a broken washer, dryer, or fridge that won't fit in the trash bin. Landlords also book quick turnovers between tenants.", ["Fontana","San Bernardino","Colton"]),
 "redlands": ("Redlands", "Redlands' older homes and long-time residents mean a lot of estate and downsizing cleanouts: full houses of furniture, attics and sheds, and decades of garage storage. Families often want items that can be donated sorted out from what has to be hauled away.", ["Loma Linda","Highland","Yucaipa","San Bernardino"]),
 "highland": ("Highland", "Highland homes near the foothills tend to generate a lot of outdoor debris: cut branches, old fencing, worn-out sheds, and leftover materials from yard projects. Inside, garage and move-out cleanouts are the most common jobs.", ["San Bernardino","Redlands","Yucaipa"]),
 "colton": ("Colton", "Colton has many older homes, rentals, and small commercial properties. Typical jobs include tenant move-out cleanouts, removing old appliances and mattresses, clearing debris from side yards and lots, and hauling off small renovation leftovers.", ["San Bernardino","Rialto","Loma Linda","Grand Terrace"]),
 "yucaipa": ("Yucaipa", "Yucaipa's bigger lots leave plenty of room for things to pile up. Homeowners commonly ask for old hot tubs, sheds, and playsets to be taken apart and hauled off, along with brush and yard waste, and full cleanouts when a property changes hands.", ["Redlands","Calimesa","Highland"]),
 "rancho-cucamonga": ("Rancho Cucamonga", "Many Rancho Cucamonga neighborhoods have HOAs that don't want junk sitting on the driveway or curb for long, so quick pickups are popular. Common jobs include furniture and appliance removal, garage cleanouts, and hauling debris after a kitchen or bathroom remodel.", ["Fontana","Ontario","Upland"]),
 "riverside": ("Riverside", "Riverside is a big, varied city, from historic neighborhoods to student rentals near UC Riverside. Move-out cleanouts, furniture and mattress removal, estate cleanouts, and remodel debris are among the most common requests.", ["Jurupa Valley","Moreno Valley","Corona","Colton"]),
 "ontario": ("Ontario", "Ontario has established older neighborhoods as well as fast-growing new communities in the south end. Requests range from garage and whole-home cleanouts to hauling off packing materials and old furniture after a move, plus construction leftovers from new builds and remodels.", ["Rancho Cucamonga","Fontana","Upland","Chino"]),
}

SERVICES = [
 ("furniture-appliance-removal","Furniture & Appliance Removal","Couches, recliners, mattresses, dressers, tables, refrigerators, washers, dryers, and other bulky items, carried out from wherever they sit, not just from the curb. Appliances with refrigerant, like fridges, freezers, and AC units, need to go to a facility that can handle them safely, so ask where they'll end up."),
 ("garage-home-cleanouts","Garage & Home Cleanouts","Clearing out a packed garage, attic, spare room, or the whole house. Crews can haul everything at once, or work around items you want to keep. Tell providers roughly how much there is (a few items, a pickup load, a full garage) so quotes are accurate."),
 ("yard-waste-removal","Yard Waste Removal","Branches, brush, palm fronds, old sod, dirt, and leftovers from landscaping projects. Good for cleanups that are too big for your green-waste bin, or for clearing out overgrowth before fire season."),
 ("construction-debris","Construction Debris Removal","Drywall, lumber, flooring, cabinets, tile, and other leftovers from a remodel or DIY project. Concrete, dirt, and roofing are heavy, so mention them up front. They often cost more to haul and may need a different truck or trailer."),
 ("hot-tub-shed-removal","Hot Tub & Shed Removal","Taking apart and hauling away old hot tubs, spas, sheds, playsets, and similar structures. Before the crew arrives, the hot tub's power should be disconnected by a qualified electrician. Larger demolition jobs may need a licensed contractor."),
 ("estate-move-out-cleanouts","Estate & Move-Out Cleanouts","Emptying a home after a move, a sale, or the loss of a loved one, or between tenants. Many providers can set aside items for donation or recycling, and some will sweep out the space when they're done."),
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

def page(path, title, desc, body, schema=None, mcta=True):
    depth = path.count("/")
    rel = "../"*depth
    canon = f"{BASE}/{path}".replace("index.html","")
    body_cls = ' class="has-mcta"' if mcta else ""
    mcta_href = "#quote" if path == "index.html" else f"{rel}contact.html"
    mcta_html = f'<div class="mobile-cta"><a href="{mcta_href}">Get free quotes</a></div>' if mcta else ""
    credits = ", ".join(dict.fromkeys(f'<a href="{v[5]}" rel="nofollow">{v[4]}</a> ({v[6]})' for v in PHOTOS.values()))
    sch = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="stylesheet" href="{rel}style.css">{sch}</head><body{body_cls}>
<header><div class="wrap"><a class="brand" href="{rel}index.html">🚛 {BRAND}</a>
<nav aria-label="Main"><a href="{rel}services.html">Services</a><a href="{rel}areas.html">Service Areas</a><a href="{rel}how-it-works.html">How It Works</a><a class="nav-cta" href="{rel}contact.html">Get Quotes</a></nav></div></header>
{body}
<footer><div class="wrap"><p><strong>{BRAND}</strong> is a free referral service. We are <strong>not a junk removal company</strong>: we don't haul anything, and we don't hold a contractor's license. When you send a request, we pass it to independent local junk removal providers who can contact you with quotes. Any provider you hire is solely responsible for its work, licensing, insurance, and how it disposes of your items. Ask for proof of insurance before hiring, and for demolition work (sheds, decks, built-in spas), check the contractor's license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a>.</p>
<p><a href="{rel}services.html">Services</a> · <a href="{rel}areas.html">Service Areas</a> · <a href="{rel}how-it-works.html">How It Works</a> · <a href="{rel}privacy.html">Privacy</a> · <a href="{rel}contact.html">Contact</a></p>
<p class="small">© {datetime.date.today().year} {BRAND}. Serving San Bernardino County, Riverside, and nearby Inland Empire communities.</p>
<p class="credits">Photos: {credits}, used under free licenses. People shown are not affiliated with this site. <a href="{rel}privacy.html#photos">Photo credits</a></p></div></footer>
{mcta_html}
</body></html>"""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path,"w").write(html)

def cta(rel=""):
    return f'<p><a class="btn" href="{rel}contact.html">Get free junk removal quotes</a></p>'

CITY_OPTS = "".join(f"<option>{v[0]}</option>" for v in CITIES.values()) + "<option>Other Inland Empire city</option>"
SVC_OPTS = "".join(f'<option value="{n}">{n}</option>' for s,n,d in SERVICES) + "<option>Other / not sure</option>"
CONSENT = f"I agree that {BRAND} may share my request and contact info with independent local junk removal providers so they can contact me about this job. *"
quick_form = f"""<div class="quote-card" id="quote"><h2>Get free quotes</h2><p class="small">Takes about 30 seconds. Free, no obligation.</p>
<form action="{FORM_ACTION}" method="POST">
{hidden_fields()}
<input type="hidden" name="form" value="Homepage quick form">
<div class="row"><div><label for="q-name">Your name *</label><input id="q-name" name="name" autocomplete="name" required></div>
<div><label for="q-phone">Phone *</label><input id="q-phone" name="phone" type="tel" autocomplete="tel" required></div></div>
<div class="row"><div><label for="q-city">City *</label><select id="q-city" name="city" required><option value="">Choose your city</option>{CITY_OPTS}</select></div>
<div><label for="q-service">Service *</label><select id="q-service" name="service" required><option value="">Choose a service</option>{SVC_OPTS}</select></div></div>
<label for="q-details">What needs to go?</label><textarea id="q-details" name="details" placeholder="e.g. old couch, broken fridge, and about half a garage of boxes"></textarea>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{CONSENT}</span></label>
<p style="margin:.7rem 0 .2rem"><button class="btn btn-block" type="submit">Get my free quotes</button></p>
<p class="small">Want to add email, timing, or more details? Use the <a href="contact.html">full request form</a>. See our <a href="privacy.html">privacy policy</a>.</p></form></div>"""

# HOME
svc_cards="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p><a href="services.html#{s}">Learn more</a></div>' for s,n,d in SERVICES)
city_links="".join(f'<li><a href="areas/{k}.html">{v[0]} junk removal</a></li>' for k,v in CITIES.items())
faq=[("Is this service free?","Yes. Requesting quotes through this site is free, and you don't have to hire anyone."),
("Are you a junk removal company?","No. We're a referral service that connects you with independent local junk removal providers. We don't haul anything ourselves."),
("How much does junk removal cost?","It depends mostly on how much space your items take up in the truck, plus what they are (heavy materials like concrete, dirt, or roofing cost more), how far they have to be carried, stairs, and local disposal fees. Photos and an honest description of the amount help you get accurate quotes. Comparing more than one quote is the best way to know what's fair."),
("What won't junk haulers take?","Most won't take hazardous materials such as paint, solvents, motor oil, pesticides, pool chemicals, propane tanks, car batteries, or anything that might contain asbestos. Your county's household hazardous waste program can usually take those. Ask the provider for its list before the pickup."),
("Do I need to be home for the pickup?","Not always. If everything is outside or in an unlocked garage, some providers can do the job while you're away. Agree on the price and the exact items ahead of time."),
("Where does my stuff go?","It depends on the provider. Reputable haulers take loads to licensed transfer stations, landfills, recyclers, and donation centers. If donation or recycling matters to you, ask about it when you compare quotes.")]
faq_html="".join(f"<h3>{q}</h3><p>{a}</p>" for q,a in faq)
faq_schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
tips_html='''<ul><li>Get two or three quotes, and make sure each one says what's included: loading, carrying from inside or upstairs, sweeping up, and disposal or recycling fees.</li><li>Ask how pricing works (by truck volume, by item, or by weight) and whether the price can change once the crew sees the load.</li><li>Ask for proof of liability insurance, especially if the crew will be working inside your home.</li><li>For demolition (sheds, decks, built-in spas), ask whether the company holds a contractor's license and look it up at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a>.</li><li>Ask where the load goes. A hauler who dumps illegally to save on fees is a red flag.</li><li>For just one or two bulky items, check with your city's trash service first. Many offer bulky-item pickups.</li><li>Keep hazardous materials (paint, chemicals, batteries, propane) separate. Most haulers can't take them.</li></ul>'''
page("index.html", f"Junk Removal Quotes | San Bernardino, Fontana, Riverside & Inland Empire | {BRAND}",
 "Get free quotes from local junk removal providers for furniture and appliance removal, garage and home cleanouts, yard waste, construction debris, and hot tub or shed removal in the Inland Empire.",
f"""<section class="hero"><img class="hero-bg" src="{PHOTOS['hero'][0]}" width="1600" height="1066" alt="{PHOTOS['hero'][3]}" fetchpriority="high"><div class="wrap"><div><h1>Junk removal and cleanout quotes in the Inland Empire</h1>
<p>Tell us what needs to go, once, and we'll connect you with local junk removal providers in San Bernardino, Fontana, Riverside, Redlands, and nearby cities. It's free, and you don't have to hire anyone.</p>
<ul class="checks"><li>One short request, free quotes from local haulers</li><li>Furniture, appliances, cleanouts, yard waste, debris</li><li>No cost and no obligation to hire</li></ul></div>
{quick_form}</div></section>
<main class="wrap">
<p class="note"><strong>Plain-English disclosure:</strong> {BRAND} is a referral service, not a junk removal company. We pass your request to independent local providers who can contact you. We don't do the work, and we can't vouch for any provider's pricing, insurance, or disposal practices, so please check before you hire.</p>
<h2>Junk removal services we can help you find</h2><div class="grid">{svc_cards}</div>
<div class="split"><div><h2>How it works</h2><ol><li><strong>Tell us what needs to go</strong>: the items, roughly how much, where they are (curb, garage, inside, upstairs), and when you need it done.</li><li><strong>We match you</strong> with independent junk removal providers who serve your city.</li><li><strong>Compare quotes</strong> and hire whoever you choose, or nobody at all.</li></ol>
{cta()}</div>{img("boxes")}</div>
<h2>Cities we cover</h2><ul class="cities">{city_links}</ul>
<h2>Tips before you hire a junk removal service</h2>{tips_html}
<h2>Frequently asked questions</h2>{faq_html}{cta()}</main>""", faq_schema)

# SERVICES
SVC_IMG = {"furniture-appliance-removal":"hero","yard-waste-removal":"yard","estate-move-out-cleanouts":"boxes"}
svc_html="".join((f'<section id="{s}" class="svc">{img(SVC_IMG[s])}<div>' if s in SVC_IMG else f'<section id="{s}"><div>')+f'<h2>{n}</h2><p>{d}</p><p><a href="contact.html?service={s}">Get {n.lower()} quotes</a></p></div></section>' for s,n,d in SERVICES)
page("services.html", f"Junk Removal Services: Furniture, Appliances, Cleanouts, Yard Waste, Debris | {BRAND}",
 "Furniture and appliance removal, garage and home cleanouts, yard waste, construction debris, hot tub and shed removal, and estate cleanout quotes from local Inland Empire providers.",
f'<main class="wrap"><h1>Junk removal services in the Inland Empire</h1><p>These are the jobs people ask about most. Send one request, and local providers can quote it.</p>{svc_html}<p class="note">Prices depend on how much there is, what it is, how hard it is to reach, and disposal fees. The only reliable number is a written quote from a provider who has seen the items or clear photos of them.</p><h2>Not sure what can go?</h2><p>Most providers take furniture, appliances, electronics, mattresses, boxes, yard waste, and construction leftovers. Hazardous materials such as paint, chemicals, oil, batteries, propane tanks, and anything that might contain asbestos usually need to go through your county\'s household hazardous waste program instead.</p>{cta()}</main>')

# AREAS index
page("areas.html", f"Service Areas: Inland Empire Junk Removal Quotes | {BRAND}",
 "Junk removal quotes for San Bernardino, Fontana, Rialto, Redlands, Highland, Colton, Yucaipa, Rancho Cucamonga, Riverside, and Ontario.",
f'<main class="wrap"><h1>Service areas</h1><p>We currently take requests from these Inland Empire communities. If your city isn\'t listed, send a request anyway and we\'ll try to find a provider nearby.</p><ul class="cities">{"".join(f"<li><a href=areas/{k}.html>{v[0]}</a></li>" for k,v in CITIES.items())}</ul>{cta()}</main>')

for k,(name,blurb,near) in CITIES.items():
    svc_list="".join(f"<li><strong>{n}</strong>: {d}</li>" for s,n,d in SERVICES)
    near_links=", ".join(f'<a href="{(c.lower().replace(" ","-"))}.html">{c}</a>' if c.lower().replace(" ","-") in CITIES else c for c in near)
    sch={"@context":"https://schema.org","@type":"Service","serviceType":"Junk removal referral","name":f"Junk removal quotes in {name}, CA","areaServed":{"@type":"City","name":f"{name}, California"},"provider":{"@type":"Organization","name":BRAND,"url":BASE+"/"},"description":f"Free referral service that connects {name} residents and property owners with independent local junk removal providers."}
    page(f"areas/{k}.html", f"Junk Removal Quotes in {name}, CA | {BRAND}",
     f"Free quotes for furniture and appliance removal, garage cleanouts, yard waste, and debris hauling from local providers serving {name}, California.",
f"""<main class="wrap"><h1>Junk removal quotes in {name}, CA</h1>
<p>{blurb}</p>
<p>Send us one request and we'll pass it to independent junk removal providers who work in {name}. It's free, and you don't have to hire anyone.</p>
{cta("../")}
<h2>Common junk removal jobs in {name}</h2><ul>{svc_list}</ul>
<h2>Before you hire in {name}</h2><ul><li>For one or two bulky items, ask your trash service whether {name} offers bulky-item pickup first.</li><li>Get the scope in writing: which items, carrying from inside or upstairs, cleanup, and disposal fees.</li><li>Ask for proof of insurance, and for demolition work, check the license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a>.</li><li>If you rent or live in an HOA, check any rules about where items can be staged before pickup.</li></ul>
<p>Nearby areas: {near_links}.</p>
<p class="note">{BRAND} is a referral service, not a junk removal company. Independent providers do all the work.</p>{cta("../")}</main>""", sch)

# HOW IT WORKS
page("how-it-works.html", f"How It Works | {BRAND}", "How our free junk removal referral works and what we do with your request.",
f"""<main class="wrap"><h1>How {BRAND} works</h1>
<p>We're a small, independent referral service in the Inland Empire. We built this site so you can find someone to haul away junk without calling a dozen companies.</p>
<ol><li>You fill out the <a href="contact.html">quote request form</a>.</li><li>We review it and share your job details and contact information with one or more independent junk removal providers who serve your area.</li><li>Providers contact you directly to ask questions, look at photos, or schedule a quick estimate.</li><li>You decide who to hire, if anyone. Your agreement is directly with that provider.</li></ol>
<h2>Getting accurate quotes</h2><ul><li>Describe the amount in plain terms: "a few items," "about a pickup truck load," "a full one-car garage."</li><li>Mention anything heavy (concrete, dirt, tile, a piano) or hard to reach (stairs, a long walk from the truck, a tight side yard).</li><li>Have photos ready. Many providers can quote from photos.</li></ul>
<h2>What we are, and what we aren't</h2><ul><li>We're <strong>not</strong> a junk removal company and we don't haul anything.</li><li>We don't guarantee any provider's work, price, insurance, or disposal practices.</li><li>We may receive a fee from providers for referrals. It never costs you anything.</li><li>We don't post fake reviews or ratings.</li></ul>
<h2>Junk removal companies</h2><p>Do you run an insured junk removal or hauling business in the Inland Empire and want more local jobs? <a href="contact.html?type=provider">Get in touch</a>.</p>{cta()}</main>""")

# CONTACT
form=f"""<form action="{FORM_ACTION}" method="POST">
{hidden_fields()}
<label for="name">Your name *</label><input id="name" name="name" autocomplete="name" required>
<label for="phone">Phone *</label><input id="phone" name="phone" type="tel" autocomplete="tel" required>
<label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email">
<label for="city">City *</label><select id="city" name="city" required><option value="">Choose your city</option>{CITY_OPTS}</select>
<label for="service">What do you need? *</label><select id="service" name="service" required><option value="">Choose a service</option>{SVC_OPTS}<option>I'm a junk removal provider</option></select>
<label for="location">Where are the items?</label><select id="location" name="location"><option>Curb or driveway</option><option>Garage</option><option selected>Inside the home</option><option>Upstairs / no elevator</option><option>Backyard or side yard</option><option>Several places</option></select>
<label for="timing">How soon?</label><select id="timing" name="timing"><option>As soon as possible</option><option>Within a week</option><option selected>Within a month</option><option>Just getting prices</option></select>
<label for="details">What needs to go? (items, rough amount like "half a pickup" or "a full garage," anything heavy like concrete or a piano)</label><textarea id="details" name="details"></textarea>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{CONSENT}</span></label>
<p><button class="btn" type="submit">Send my request</button></p>
<p class="small">We'll use your information only to connect you with providers for this request. See our <a href="privacy.html">privacy policy</a>.</p></form>"""
page("contact.html", f"Get Free Junk Removal Quotes | {BRAND}", "Request free quotes for furniture and appliance removal, cleanouts, yard waste, construction debris, or hot tub and shed removal in the Inland Empire.",
f'<main class="wrap"><h1>Get free junk removal quotes</h1><p>Fill out the form and we\'ll pass your request to independent local junk removal providers. There\'s no cost and no obligation.</p><p class="note">Have hazardous materials (paint, chemicals, oil, batteries, propane, or possible asbestos)? Most haulers can\'t take them. Contact your county\'s household hazardous waste program for those.</p>{form}<p class="small">Prefer to call? {PHONE} (optional; the form is the fastest way to reach us).</p></main>', mcta=False)

page("thank-you.html", f"Thanks, we got your request | {BRAND}", "Thank you for your junk removal request.",
 f"""<main class="wrap"><h1>Thanks! Your request was sent.</h1><p>We'll review it and pass it to local junk removal providers who serve your area. They'll contact you directly. Before you hire, confirm the price, what's included, and how your items will be disposed of.</p><p><a href="index.html">Back to home</a></p></main>""", mcta=False)

page("privacy.html", f"Privacy Policy | {BRAND}", f"Privacy policy for {BRAND}.",
f"""<main class="wrap"><h1>Privacy policy</h1><p>Last updated {TODAY}.</p>
<p><strong>What we collect:</strong> the information you enter in our form (name, phone, email, city, and job details). Our form is processed by FormSubmit (formsubmit.co), which emails it to us. Our host (GitHub Pages) may log basic technical data such as IP addresses.</p>
<p><strong>How we use it:</strong> only to respond to your request and to share it with independent junk removal providers in your area so they can contact you about your job. We don't sell your information to data brokers and we don't use it for unrelated marketing.</p>
<p><strong>Your choices:</strong> email {EMAIL} to ask us to delete your information or to stop sharing it. California residents may have additional rights under the CCPA/CPRA.</p>
<p><strong>Contact:</strong> {EMAIL}</p>
<h2 id="photos">Photo credits</h2><p>Photos on this site are stock photos used under free licenses that allow commercial use without attribution. We credit the photographers anyway. The people shown are not affiliated with {BRAND} or with any provider we refer you to.</p>
<ul>{"".join(f'<li>{v[3]}: photo by <a href="{v[5]}" rel="nofollow">{v[4]}</a> on <a href="{v[7]}" rel="nofollow">{v[6]}</a> ({v[8]})</li>' for v in PHOTOS.values())}</ul></main>""")

open("style.css","w").write(CSS)
urls=["","services.html","areas.html","how-it-works.html","contact.html","privacy.html"]+[f"areas/{k}.html" for k in CITIES]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(".nojekyll","w").write("")
print("built")
