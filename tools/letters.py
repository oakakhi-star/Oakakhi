#!/usr/bin/env python3
"""Build "Letters from Oakakhi": the journal index, one page per letter,
the home page teaser, sitemap.xml and robots.txt.

To add a letter: append a dict to POSTS (newest first is not required,
they are sorted by date), then run:  python3 tools/letters.py
"""
import html, json, os, re

SITE = "https://oakakhistays.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA = "https://wa.me/919870213163?text="

POSTS = [
 {
  "slug": "things-to-do-in-ranikhet",
  "date": "2026-11-03",
  "tag": "Guide",
  "title": "Things to do in Ranikhet, the slow way",
  "dek": "Temples, orchards, an old golf course in the pines and the ridge views most visitors drive past. A local's guide to Ranikhet.",
  "description": "A local guide to the best things to do in Ranikhet, Uttarakhand: Kalika Temple, Chaubatia Gardens, Ranikhet Golf Course, Jhula Devi Temple, Bhalu Dam and Himalayan viewpoints.",
  "hero": "expw-sightseeing.webp", "hero_alt": "The Himalaya seen between pines above Ranikhet",
  "read": 5,
  "body": """
<p>Ranikhet is a quiet hill town in the Kumaon Himalaya of Uttarakhand, set among pine and oak at around six thousand feet. It is the kind of place that rewards an unhurried pace. Here is how we suggest spending your days, from the ridge where Oakakhi sits.</p>

<h2>Kalika Temple and the forest around it</h2>
<p>Oakakhi is a short walk from the ancient Kalika Temple. Go early in the morning, when the bells are the only sound and the light falls through the deodar and oak. The path back to the house is one of our favourite short walks in all of Ranikhet.</p>

<h2>Ranikhet Golf Course</h2>
<p>Laid out on an open meadow ringed by pines, the old golf course near Kalika is often described as one of the highest in Asia. Even if you never pick up a club, the walk along its edge on a clear day, with the snow peaks in the distance, is worth the visit.</p>

<h2>Chaubatia Gardens and Bhalu Dam</h2>
<p>Chaubatia is known for its orchards of apple, apricot and plum, and for wide views of the Himalaya. A little beyond lies Bhalu Dam, a small, still lake in the forest that makes a peaceful place for a picnic.</p>

<figure><img src="/assets/img/g-peaks.webp" alt="The Himalayan range at first light, framed by pines near Ranikhet" loading="lazy"><figcaption>First light on the high peaks, from the ridge near Oakakhi</figcaption></figure>

<h2>Jhula Devi Temple</h2>
<p>Close to Chaubatia, this small temple is famous for the thousands of bells tied by devotees whose wishes have been granted. It is a moving place, and a lovely stop on the way back from the orchards.</p>

<h2>The Kumaon Regimental Centre Museum</h2>
<p>Ranikhet is a cantonment town with a long military history. The regimental museum tells the story of the Kumaon and Naga regiments and makes a thoughtful hour on a rainy afternoon.</p>

<h2>Village walks and Kumaoni food</h2>
<p>Some of the best moments are not in any guidebook. Walk through Dadgaliya village with Nishant, see the terraced fields and stone homes, and share tea in a courtyard. Back at Oakakhi, the evening meal is home style Kumaoni food.</p>

<h2>Stargazing and bonfire evenings</h2>
<p>Far from city lights, Ranikhet has wonderfully dark skies, especially from October to March. End the day around the bonfire, then step away from the fire to find Orion rising over the ridge.</p>

<div class="note"><strong>Planning your days.</strong> Nishant arranges a guided half day or full day around Ranikhet, with a comfortable local taxi and stories at every stop. Simply ask when you book.</div>
"""},
 {
  "slug": "birdwatching-in-ranikhet",
  "date": "2026-11-03",
  "tag": "Birds",
  "title": "Birdwatching in Ranikhet: the oak forest at dawn",
  "dek": "From the Khalij pheasant to the blue whistling thrush, the forests around Ranikhet are alive with Himalayan birds. Where, when and what to look for.",
  "description": "A guide to birdwatching in Ranikhet and the Kumaon oak forests: Khalij pheasant, blue whistling thrush, red billed blue magpie, Himalayan bulbul, best season and tips.",
  "hero": "expw-birdwatching.webp", "hero_alt": "A Khalij pheasant among the pines near Oakakhi",
  "read": 4,
  "body": """
<p>The oak and pine forests around Ranikhet are among the most rewarding places in Kumaon for birdwatching. You do not need to travel far: from the terrace at Oakakhi, the morning chorus begins before the light does.</p>

<h2>Birds you are likely to see</h2>
<p>The forest around Oakakhi is home to many Himalayan species through the year. A few of the birds our guests most often see:</p>
<ul>
<li><strong>Khalij pheasant.</strong> Shy and beautiful, often seen at the forest edge in the early morning.</li>
<li><strong>Blue whistling thrush.</strong> You will hear its long, human sounding whistle before you see it.</li>
<li><strong>Red billed blue magpie.</strong> Long tailed, bold and unmistakable as it glides between trees.</li>
<li><strong>Himalayan bulbul.</strong> Cheerful and common, with its swept back white cheeks.</li>
<li><strong>Warblers and flycatchers</strong>, which change with the seasons.</li>
</ul>

<figure><img src="/assets/img/exp-forestwalk.webp" alt="Sunlit pine and oak forest near Oakakhi, Ranikhet, at dawn" loading="lazy"><figcaption>The forest edge near Oakakhi, where many birds feed at first light</figcaption></figure>

<h2>The best time of day</h2>
<p>First light, roughly between 5:30 and 8:00 in the morning, is when the forest is most active. Late afternoon is a quieter second window.</p>

<h2>The best season</h2>
<p>Spring, from March to May, brings breeding plumage and the most song. Winter is excellent too: the air is clear, the forest is open and some higher altitude birds come down into the oaks.</p>

<h2>A dawn walk with Nishant</h2>
<p>Nishant grew up listening to these forests and knows the songs before he sees the birds. A dawn session with him is two to three slow hours through the oak grove. Less a hike, more a listening session.</p>

<div class="note"><strong>What to bring.</strong> Binoculars if you have them, soft coloured clothing, warm layers for the early hour and a little patience. A camera with a zoom lens helps, but is never essential.</div>
"""},
 {
  "slug": "treks-near-ranikhet",
  "date": "2026-11-03",
  "tag": "Treks",
  "title": "Treks near Ranikhet, from forest walks to glaciers",
  "dek": "Pandukholi, Bharatkot, the Mahavtar forest and further, to the Pindari Glacier. Treks of every length that begin from the Kumaon ridges.",
  "description": "The best treks near Ranikhet, Uttarakhand: Pandukholi, Bharatkot, the Mahavtar bamboo forest, and multi day treks to Pindari Glacier and Khalia Top, with local guides.",
  "hero": "nishant-camp.webp", "hero_alt": "A trekker at camp above a sea of Kumaon hills at first light",
  "read": 5,
  "body": """
<p>Ranikhet makes an ideal base for walking in the Kumaon Himalaya. Within an hour or two there are short forest trails and summit viewpoints, and a little further lie some of the most beautiful multi day treks in Uttarakhand.</p>

<h2>Forest walks from Oakakhi</h2>
<p>The gentlest trek begins at the door. A circular walk of two to four kilometres through the oak grove around Oakakhi suits every level of fitness, and Nishant will show you the trees, the medicinal plants and where the deer come to drink.</p>

<h2>Pandukholi</h2>
<p>A forest trail climbs to the high meadow of Pandukholi, linked by legend to the Pandavas. The sunrise and sunset views over the Himalaya from the top are unforgettable, and the walk through the forest is beautiful in every season.</p>

<h2>Bharatkot</h2>
<p>A rewarding day walk to a ridge top with wide views of the snow peaks, including Trishul. A good choice for walkers who want a summit without a long journey.</p>

<figure><img src="/assets/img/nishant-peaks.webp" alt="A trekker resting with the Himalayan range behind, on a trek near Ranikhet" loading="lazy"><figcaption>The high peaks from a Kumaon ridge trail</figcaption></figure>

<h2>The Mahavtar bamboo forest</h2>
<p>A quiet walk through bamboo and pine, valued as much for its stillness as for the trail itself.</p>

<h2>Multi day treks: Pindari Glacier and Khalia Top</h2>
<p>For those who wish to go further, the Pindari Glacier trek follows river valleys and villages to the foot of the glacier over several days. Khalia Top, near Munsiyari, offers a shorter high camp with remarkable views of the Panchachuli peaks.</p>

<div class="note"><strong>Trekking with us.</strong> Longer treks are curated by <a href="https://www.turiyatrails.in" target="_blank" rel="noopener">Turiya Trails</a>, our partner in mountain journeys, with experienced local trek leaders. Nishant, himself a trek leader and mountaineer, will help you choose and arrange the right trek for your stay.</div>
"""},
 {
  "slug": "how-to-reach-ranikhet-oakakhi",
  "date": "2026-11-03",
  "tag": "Guide",
  "title": "How to reach Ranikhet and Oakakhi",
  "dek": "By road from Delhi, by train to Kathgodam, or by air to Pantnagar. Everything you need for the journey, including the short forest walk at the end.",
  "description": "How to reach Ranikhet and Oakakhi Stays: by road from Delhi via NH 9, by train to Kathgodam, by air to Pantnagar, and parking near the homestay.",
  "hero": "mist-house.webp", "hero_alt": "Oakakhi among the trees in monsoon mist",
  "read": 3,
  "faq": [
   ("How far is Ranikhet from Delhi?", "Ranikhet is about 320 km from Delhi by road, via NH 9."),
   ("Which is the nearest railway station to Ranikhet?", "Kathgodam (KGM) is the nearest railway station, about 85 km from Oakakhi, with good connections from Delhi and Lucknow."),
   ("Which is the nearest airport to Ranikhet?", "Pantnagar Airport is the nearest airport, about 120 km away."),
   ("Is there parking at Oakakhi?", "Parking is about 200 metres from the house. From there a short forest trail of around 200 metres leads to Oakakhi, and Nishant will guide you in."),
  ],
  "body": """
<p>Oakakhi sits in Village Dadgaliya, near Kalika, on the ridges of Ranikhet in Uttarakhand. The journey is part of the pleasure: the road climbs from the plains into pine forest, and the final stretch is walked through the trees.</p>

<h2>By road</h2>
<p>From Delhi, Ranikhet is about 320 km by road via NH 9. Most guests drive or take a taxi, and the mountain section of the journey is scenic. Taxis are available from Kathgodam and Ramnagar.</p>

<h2>By train</h2>
<p>Kathgodam (KGM) is the nearest railway station, about 85 km from Oakakhi, with good overnight and day connections from Delhi and Lucknow. From Kathgodam, a taxi brings you up into the hills.</p>

<h2>By air</h2>
<p>Pantnagar Airport is the nearest airport, about 120 km away, followed by a scenic mountain drive.</p>

<figure><img src="/assets/img/reach.webp" alt="The Oakakhi Stays signboard on a stone wall in Ranikhet" loading="lazy"><figcaption>Look for our signboard on the old stone wall</figcaption></figure>

<h2>Parking and the last 200 metres</h2>
<p>Parking is about 200 metres from the house. Leave the car there and follow a short forest trail of around 200 metres to Oakakhi. It is an easy walk, and Nishant will meet you and guide you in. Please pack so that your luggage is comfortable to carry a short distance.</p>
"""},
 {
  "slug": "best-time-to-visit-ranikhet",
  "date": "2026-11-03",
  "tag": "Guide",
  "title": "The best time to visit Ranikhet, season by season",
  "dek": "Clear winter skies, spring birdsong, green monsoon mist and golden autumn. What each season brings to the Kumaon hills.",
  "description": "When is the best time to visit Ranikhet? A season by season guide to weather, Himalayan views, stargazing, birdwatching and monsoon in Ranikhet, Uttarakhand.",
  "hero": "band.webp", "hero_alt": "Trishul glowing rose at dusk, seen from Ranikhet",
  "read": 4,
  "faq": [
   ("When can you see the Himalaya from Ranikhet?", "The clearest views of the snow peaks usually come from October to March, after the monsoon has washed the air clean."),
   ("Is Ranikhet good in the monsoon?", "Yes, for those who love mist and green forests. Views of the peaks are rarer, but the oak forest is at its most beautiful."),
   ("What is the best season for stargazing in Ranikhet?", "October to March offers the clearest night skies."),
  ],
  "body": """
<p>Every season changes the ridge around Oakakhi completely. There is no wrong time to come; there is only the time that suits what you are looking for.</p>

<h2>October to November: the clearest views</h2>
<p>After the monsoon, the air is washed clean and the Himalaya stand out sharply on the horizon. Days are bright and comfortable, evenings are cool, and the night skies begin to clear. For many, this is the finest time of year.</p>

<h2>December to February: winter light</h2>
<p>Cold, crisp and quiet. The snow peaks glow at sunrise and dusk, bonfires feel especially welcome, and the stars are extraordinary. Pack warm layers: nights in the hills are properly cold.</p>

<figure><img src="/assets/img/g-sunset.webp" alt="Sunset over the Kumaon hills from Ranikhet" loading="lazy"><figcaption>A winter sunset over the Kumaon hills</figcaption></figure>

<h2>March to May: spring and birdsong</h2>
<p>The forest wakes. Rhododendrons flower on the hillsides, birds are in full song and the days are warm and pleasant, a welcome escape from the heat of the plains.</p>

<h2>June to September: monsoon mist</h2>
<p>Rain and mist move through the oak forest, and everything turns a deep, vivid green. Views of the peaks are rarer, but for those who love the sound of rain on a timber roof, the monsoon is magical.</p>

<figure><img src="/assets/img/mist-balcony.webp" alt="Rain falling over Oakakhi, seen from a timber balcony" loading="lazy"><figcaption>Monsoon rain from the balcony</figcaption></figure>
"""},
 {
  "slug": "a-letter-from-the-ridge-monsoon-mist",
  "date": "2026-11-03",
  "tag": "Letter",
  "title": "A letter from the ridge: when the mist arrives",
  "dek": "Some mornings the valley disappears, and the house floats in a white silence. A short letter from Oakakhi in the monsoon.",
  "description": "A letter from Oakakhi Stays in Ranikhet: monsoon mist in the oak forest, rain on the roof and slow days at a Kumaon homestay.",
  "hero": "mist-balcony.webp", "hero_alt": "Rain and mist over Oakakhi, seen from the balcony",
  "read": 2,
  "body": """
<p>Some mornings, the valley simply disappears.</p>
<p>The mist rises from below the ridge before dawn and settles among the oaks. The house floats in it. You hear the forest more than you see it: water dripping from the leaves, a whistling thrush somewhere close, the soft drum of rain on the roof.</p>
<p>On days like these there is nowhere to go and nothing to do, and that is exactly the point. Tea tastes better. Books get finished. Conversations run long.</p>

<figure><img src="/assets/img/mist-house.webp" alt="Oakakhi wrapped in monsoon mist among the trees" loading="lazy"><figcaption>Oakakhi in the monsoon mist</figcaption></figure>

<p>Then, often in the afternoon, the white parts like a curtain, and for a few minutes the whole valley returns, rinsed and glittering and impossibly green.</p>
<p>If you have never seen the hills in the monsoon, come and watch the mist arrive. We will keep the chai warm.</p>
<p class="signoff">With warmth, from the Kalika ridge.</p>
"""},
]

def esc(x): return html.escape(x, quote=True)

def rfc(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime('%a, %d %b %Y 08:00:00 +0530')

def fmt_date(d):
    y, m, dd = d.split("-")
    months = "January February March April May June July August September October November December".split()
    return f"{int(dd)} {months[int(m)-1]} {y}"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">'

def head(title, desc, url, image, extra_ld):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#2F372D">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}/assets/img/{image}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/brand/favicon.svg">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<link rel="alternate" type="application/rss+xml" title="Letters from Oakakhi" href="/letters/feed.xml">
{FONTS}
<link rel="stylesheet" href="/assets/css/letters.css">
{extra_ld}
</head>
<body>
<header class="lt-nav">
  <a href="/" class="lt-logo" aria-label="Oakakhi Stays, home"><img src="/assets/brand/oakakhi-logo-dark.svg" alt="Oakakhi Stays" width="170" height="64"></a>
  <nav aria-label="Main"><a href="/#rooms">Rooms</a><a href="/#experiences">Experiences</a><a href="/letters/">Letters</a></nav>
  <a class="lt-btn" href="{WA}Hello%20Nishant%2C%20I%20would%20like%20to%20reserve%20a%20stay%20at%20Oakakhi." target="_blank" rel="noopener">Reserve</a>
</header>
"""

FOOT = f"""
<footer class="lt-foot">
  <img src="/assets/brand/oakakhi-logo-light.svg" alt="Oakakhi Stays" width="220" height="84" loading="lazy">
  <p>A forest homestay in the lap of the oaks, on the Kalika ridge of Ranikhet, Uttarakhand.</p>
  <div class="lt-foot-links"><a href="/">Home</a><a href="/#rooms">Rooms</a><a href="/letters/">Letters</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="https://www.instagram.com/Oakakhi_stays" target="_blank" rel="noopener">Instagram</a></div>
  <small>© 2026 Oakakhi Stays · Village Dadgaliya, Kalika, Ranikhet, Uttarakhand 263652</small>
</footer>
<script>
(function(){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('visible');io.unobserve(e.target)}}}})}},{{threshold:.1}});document.querySelectorAll('.reveal').forEach(function(el){{io.observe(el)}})}})();
</script>
</body>
</html>
"""

def card(p, cls="lt-card"):
    return f"""<a class="{cls} reveal" href="/letters/{p['slug']}/">
      <div class="lt-card-img"><img src="/assets/img/{p['hero']}" alt="{esc(p['hero_alt'])}" loading="lazy"></div>
      <div class="lt-card-body"><span class="lt-tag">{p['tag']} · {p['read']} min read</span><h3>{esc(p['title'])}</h3><p>{esc(p['dek'])}</p></div>
    </a>"""

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def build_post(p, posts):
    url = f"{SITE}/letters/{p['slug']}/"
    graph = [{
        "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
        "image": f"{SITE}/assets/img/{p['hero']}", "datePublished": p["date"], "dateModified": p["date"],
        "mainEntityOfPage": url, "inLanguage": "en",
        "author": {"@type": "Organization", "name": "Oakakhi Stays", "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "Oakakhi Stays", "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/brand/oakakhi-logo-dark.png"}},
        "about": {"@type": "Place", "name": "Ranikhet, Uttarakhand"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Oakakhi Stays", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Letters from Oakakhi", "item": SITE + "/letters/"},
        {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}]
    faq_html = ""
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
        faq_html = '<section class="lt-faq"><h2>Questions we are often asked</h2>' + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in p["faq"]) + "</section>"
    related = [x for x in posts if x["slug"] != p["slug"]][:3]
    out = head(f"{p['title']} · Letters from Oakakhi", p["description"], url, p["hero"], ld({"@context": "https://schema.org", "@graph": graph}))
    out += f"""
<main class="lt-post">
  <nav class="lt-crumbs" aria-label="Breadcrumb"><a href="/">Oakakhi</a><span>/</span><a href="/letters/">Letters</a></nav>
  <header class="lt-post-head">
    <span class="lt-tag">{p['tag']} · {fmt_date(p['date'])} · {p['read']} min read</span>
    <h1>{esc(p['title'])}</h1>
    <p class="lt-dek">{esc(p['dek'])}</p>
  </header>
  <figure class="lt-hero"><img src="/assets/img/{p['hero']}" alt="{esc(p['hero_alt'])}"></figure>
  <article class="lt-body">
{p['body']}
{faq_html}
  </article>
  <aside class="lt-stay">
    <span class="lt-tag">Stay with us</span>
    <h2>Oakakhi, <em>in the lap of the oaks</em></h2>
    <p>A forest homestay of five rooms on the Kalika ridge of Ranikhet, facing the Himalaya. Hosted by Nishant.</p>
    <div class="lt-stay-ctas"><a class="lt-btn" href="{WA}Hello%20Nishant%2C%20I%20read%20your%20letter%20and%20would%20like%20to%20plan%20a%20stay%20at%20Oakakhi." target="_blank" rel="noopener">Plan your stay</a><a class="lt-link" href="/#rooms">See the rooms →</a></div>
  </aside>
  <section class="lt-more">
    <h2>More letters</h2>
    <div class="lt-grid">{''.join(card(x) for x in related)}</div>
  </section>
</main>
"""
    out += FOOT
    d = os.path.join(ROOT, "letters", p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(out)

def build_index(posts):
    url = f"{SITE}/letters/"
    blog = {"@context": "https://schema.org", "@type": "Blog", "name": "Letters from Oakakhi", "url": url,
            "description": "Guides, letters and photographs from Oakakhi Stays in Ranikhet: things to do, treks, birdwatching and the seasons of the Kumaon Himalaya.",
            "publisher": {"@type": "Organization", "name": "Oakakhi Stays", "url": SITE + "/"},
            "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{url}{p['slug']}/", "datePublished": p["date"]} for p in posts]}
    lead, rest = posts[0], posts[1:]
    out = head("Letters from Oakakhi · Ranikhet Travel Guides, Treks and Birdwatching", blog["description"], url, lead["hero"], ld(blog))
    out += f"""
<main class="lt-index">
  <header class="lt-index-head reveal">
    <span class="lt-tag">The Journal</span>
    <h1>Letters from <em>Oakakhi</em></h1>
    <p class="lt-dek">Notes from the Kalika ridge: guides to Ranikhet, the trails and birds of the Kumaon Himalaya, and small letters from a forest homestay.</p>
  </header>
  {card(lead, "lt-feature")}
  <div class="lt-grid">{''.join(card(p) for p in rest)}</div>
</main>
"""
    out += FOOT
    open(os.path.join(ROOT, "letters", "index.html"), "w").write(out)

def build_feed(posts):
    items = "".join(f"<item><title>{esc(p['title'])}</title><link>{SITE}/letters/{p['slug']}/</link><guid>{SITE}/letters/{p['slug']}/</guid><description>{esc(p['description'])}</description><pubDate>{rfc(p['date'])}</pubDate></item>" for p in posts)
    open(os.path.join(ROOT, "letters", "feed.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Letters from Oakakhi</title><link>{SITE}/letters/</link><description>Guides and letters from Oakakhi Stays, Ranikhet.</description>{items}</channel></rss>')

def build_sitemap(posts):
    newest = max(p["date"] for p in posts)
    urls = [(SITE + "/", newest, "1.0"), (SITE + "/letters/", newest, "0.8")] + [(f"{SITE}/letters/{p['slug']}/", p["date"], "0.7") for p in posts]
    body = "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>" for u, d, pr in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n')
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

def build_teaser(posts):
    p = os.path.join(ROOT, "index.html"); s = open(p).read()
    cards = "".join(f"""<a class="lt-mini reveal" href="letters/{x['slug']}/"><img src="assets/img/{x['hero']}" alt="{esc(x['hero_alt'])}" loading="lazy"><span class="lt-mini-tag">{x['tag']}</span><h3>{esc(x['title'])}</h3></a>""" for x in posts[:3])
    block = f"""<!-- LETTERS:START -->
<section class="light letters-teaser" id="letters">
  <div class="lt-teaser-head reveal">
    <div><span class="eyebrow">Letters from Oakakhi</span><h2>Notes from <em>the ridge</em></h2></div>
    <a class="link" href="letters/">Read all letters <span aria-hidden="true">→</span></a>
  </div>
  <div class="lt-teaser-grid">{cards}</div>
</section>
<!-- LETTERS:END -->"""
    if "<!-- LETTERS:START -->" in s:
        s = re.sub(r"<!-- LETTERS:START -->.*?<!-- LETTERS:END -->", block, s, flags=re.S)
    else:
        s = s.replace("<!-- REACH -->", block + "\n\n<!-- REACH -->", 1)
    open(p, "w").write(s)

if __name__ == "__main__":
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    for p in posts: build_post(p, posts)
    build_index(posts); build_feed(posts); build_sitemap(posts); build_teaser(posts)
    print(f"Built {len(posts)} letters")
