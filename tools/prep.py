import sys,os,re,shutil,html
from PIL import Image
D,NM=sys.argv[1],sys.argv[2]
SITE='https://campaha.org'
# fonts
fd=os.path.join(D,'fonts');os.makedirs(fd,exist_ok=True);css=[]
LATIN='U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD'
for fam,slug,specs in [('Be Vietnam Pro','be-vietnam-pro',[(400,'normal'),(600,'normal'),(800,'normal'),(900,'normal'),(900,'italic')]),('Permanent Marker','permanent-marker',[(400,'normal')])]:
  for w,s in specs:
    fn=f'{slug}-latin-{w}-{s}.woff2';shutil.copy(os.path.join(NM,'@fontsource',slug,'files',fn),fd)
    css.append(f"@font-face{{font-family:'{fam}';font-style:{s};font-weight:{w};font-display:swap;src:url(/fonts/{fn}) format('woff2');unicode-range:{LATIN}}}")
open(os.path.join(fd,'fonts.css'),'w').write('\n'.join(css)+'\n')
# og image
im=Image.open(os.path.join(D,'img/hallway-group-lockers.jpg')).convert('RGB')
im=im.crop((0,170,1400,905)).resize((1200,630),Image.LANCZOS);im.save(os.path.join(D,'img/og-image.jpg'),quality=82,optimize=True)
pages={
 'index':('/','CAMP AHA | Career Role Models in Title I Classrooms','CAMP AHA brings career role models into Title I middle school classrooms in Dallas and Houston, so students can see careers they never knew were possible.'),
 'our-story':('/our-story','Our Story | CAMP AHA','Why CAMP AHA exists and how we close the opportunity gap one classroom at a time, by putting real career role models in front of middle school students.'),
 'impact':('/impact','Our Impact | CAMP AHA','What happens when role models show up: stories from role models and school staff in CAMP AHA classrooms across Dallas and Houston.'),
 'role-model':('/role-model','Become a Role Model | CAMP AHA','Share your career with middle school students for one hour. Sign up for a role model session in Dallas at Royce West or in Houston at Crispus Attucks.'),
 'partner-with-us':('/partner-with-us','Partner With Us | CAMP AHA','Partner with CAMP AHA to bring career role models into Title I classrooms, and put your company\'s name on the classrooms you make possible.'),
 'schools':('/schools','Our Schools | CAMP AHA','The Title I middle schools CAMP AHA serves in Dallas and Houston, and how each school connects students with local career role models.'),
 'privacy-policy':('/privacy-policy','Privacy Policy | CAMP AHA','How CAMP AHA handles the information you share with us. No tracking, no ads, and we never sell your information.'),
}
def meta(path,title,desc,noindex=False):
  e=html.escape
  m=[f'<title>{e(title)}</title>',f'<meta name="description" content="{e(desc)}">']
  if noindex: m.append('<meta name="robots" content="noindex">')
  else: m.append(f'<link rel="canonical" href="{SITE}{path}">')
  m+=[f'<meta property="og:type" content="website">',f'<meta property="og:site_name" content="CAMP AHA">',f'<meta property="og:title" content="{e(title)}">',f'<meta property="og:description" content="{e(desc)}">',f'<meta property="og:url" content="{SITE}{path}">',f'<meta property="og:image" content="{SITE}/img/og-image.jpg">','<meta property="og:image:width" content="1200">','<meta property="og:image:height" content="630">','<meta property="og:image:alt" content="A CAMP AHA role model with middle school students in a school hallway">','<meta name="twitter:card" content="summary_large_image">',f'<meta name="twitter:title" content="{e(title)}">',f'<meta name="twitter:description" content="{e(desc)}">',f'<meta name="twitter:image" content="{SITE}/img/og-image.jpg">']
  return '\n'.join(m)
def fix(h):
  h=re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?','',h)
  h=re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">','<link href="/fonts/fonts.css" rel="stylesheet">',h)
  h=h.replace('href="index.html"','href="/"')
  h=re.sub(r'href="([a-z-]+)\.html(#[^"]*)?"',lambda m:f'href="/{m.group(1)}{m.group(2) or ""}"',h)
  h=re.sub(r'(src|href)="img/',r'\1="/img/',h)
  # privacy link in footer bottom line
  h=h.replace('Gifts are tax deductible.</p>','Gifts are tax deductible. <a href="/privacy-policy" style="color:#ffffff;text-decoration:underline">Privacy Policy</a></p>')
  assert 'fonts.googleapis' not in h and 'fonts.gstatic' not in h
  return h
src=open(os.path.join(D,'schools.html')).read()
head_end=src.find('</header>')+len('</header>')
foot_start=src.find('<footer class="foot')
P=lambda s:f'<p style="margin:0;font-size:18px;line-height:1.65">{s}</p>'
H=lambda s:f'<h2 style="margin:12px 0 0;font-weight:900;font-style:italic;font-size:28px;text-transform:uppercase">{s}</h2>'
body=f'''
<section class="dots-navy" aria-labelledby="pp-h" style="color:#ffffff;padding:72px 24px 80px">
<div style="max-width:900px;margin:0 auto;display:flex;flex-direction:column;gap:16px">
<h1 id="pp-h" class="misreg" style="margin:0;font-weight:900;font-style:italic;font-size:clamp(48px,7vw,96px);line-height:.95;letter-spacing:-2px;text-transform:uppercase">Privacy Policy</h1>
<p style="margin:0;font-size:18px;font-weight:700">Effective November 6, 2026</p>
</div></section>
<section class="dots-light" style="padding:72px 24px 100px;border-top:4px solid #282734">
<div style="max-width:900px;margin:0 auto;display:flex;flex-direction:column;gap:18px;background:#ffffff;border:4px solid #282734;border-radius:28px;padding:40px;box-shadow:8px 8px 0 #282734">
{P("CAMP AHA is a 501(c)(3) nonprofit that brings career role models into Title I classrooms in Dallas and Houston. We keep this site simple and we respect your privacy. This page explains what we collect and how we use it.")}
{H("What we collect")}
{P("We only collect what you choose to share with us: when you email us, when you sign up for a role model session, or when you join our newsletter. That can include your name, email address, phone number, employer, and career field.")}
{H("No tracking on this site")}
{P("This site does not use cookies, analytics, advertising pixels, or tracking scripts. Our fonts and images are hosted on our own site, so nothing loads from another company when you visit. Our hosting provider keeps standard server logs, such as IP addresses, for security and reliability.")}
{H("Services we use")}
{P("Role model sign ups run through Calendly. Our newsletter runs through MailerLite. Our email runs through Google Workspace. When you use one of these, that company handles your information under its own privacy policy. You leave our site when you click to sign up on Calendly.")}
{H("How we use your information")}
{P("We use your information to schedule sessions, send session reminders, share the district volunteer and background check steps, follow up after sessions, and send our newsletter. We never sell, rent, or trade your information.")}
{H("Students")}
{P("This site is written for adults: role models, partners, and school leaders. We do not collect information from students through this site. Photos of students appear with permission. To request that a photo be removed, email info@campaha.org and we will take it down.")}
{H("Your choices")}
{P("You can unsubscribe from our newsletter at any time using the link in any email. To see, correct, or delete the information we hold about you, email info@campaha.org.")}
{H("Contact")}
{P('Questions about this policy? Email <a href="mailto:info@campaha.org">info@campaha.org</a>.')}
</div></section>
'''
open(os.path.join(D,'privacy-policy.html'),'w').write(src[:head_end]+body+'\n'+src[foot_start:])
nf=f'''
<section class="dots-navy" style="color:#ffffff;padding:100px 24px 120px;text-align:center">
<div style="max-width:800px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:24px">
<img src="/img/char-waving-boy.png" alt="" class="idle" style="height:220px;width:auto;filter:drop-shadow(6px 6px 0 #1caeed)">
<h1 class="misreg" style="margin:0;font-weight:900;font-style:italic;font-size:clamp(48px,8vw,110px);line-height:.95;text-transform:uppercase">Page not found</h1>
<p style="margin:0;font-size:20px;font-weight:700">This page took a different career path. Let's get you back on track.</p>
<a class="btn" href="/" style="display:inline-flex;align-items:center;min-height:56px;padding:0 28px;background:#ffd23f;color:#282734;font-weight:900;font-size:18px;text-decoration:none;border:4px solid #282734;border-radius:999px;box-shadow:6px 6px 0 #1caeed">Back to Home</a>
</div></section>
'''
open(os.path.join(D,'404.html'),'w').write(src[:head_end]+nf+'\n'+src[foot_start:])
pages_all=dict(pages);pages_all['404']=('/404','Page Not Found | CAMP AHA','This page could not be found.')
for name,(path,title,desc) in pages_all.items():
  f=os.path.join(D,name+'.html');h=open(f).read()
  h=re.sub(r'<title>[^<]*</title>',lambda m:meta(path,title,desc,noindex=(name=='404')),h,count=1)
  h=fix(h);open(f,'w').write(h)
open(os.path.join(D,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
urls=''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>2026-11-06</lastmod></url>\n' for n,(p,_,_) in pages.items())
open(os.path.join(D,'sitemap.xml'),'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(D,'_redirects'),'w').write('''http://www.campaha.org/*   https://campaha.org/:splat  301!
https://www.campaha.org/*  https://campaha.org/:splat  301!

/aha-mentor-postive-feedback/*   /impact  301
/school-positive-feedback-aha/*  /impact  301
/index.html                      /        301
/home                            /        301

/*  /404.html  404
''')
print('ok')
