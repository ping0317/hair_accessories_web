from pathlib import Path

products = [
 ('奶油碎花蝴蝶結抓夾','奶油花語','細緻碎花與柔和奶油白，為日常半綁髮添一點浪漫。','https://s.shopee.tw/1AXQeEEav',[23,24,25]),
 ('奶油粉珍珠蝴蝶結抓夾','奶油花語','奶白與淡粉緞帶交織，點綴輕盈的珍珠吊飾。','https://s.shopee.tw/9AOmLVs8Hj',[17,21,22]),
 ('水藍花卉雪紡馬尾夾','奶油花語','清透水藍花卉與長飄帶，陪你走進微風裡。','https://s.shopee.tw/2BF20iucpO',[28,26,27]),
 ('奶杏蕾絲飄帶髮夾','法式浪漫','奶杏緞帶拼接透膚蕾絲，留下溫柔的復古細節。','https://s.shopee.tw/AKajjfikZ3',[14,16,15]),
 ('黑色印花蝴蝶結髮夾','法式浪漫','黑底白色印花，為低馬尾與公主頭添上優雅。','https://s.shopee.tw/6L4ayKoqKe',[5,3,4]),
 ('黑色雪紡大蝴蝶結髮夾','法式浪漫','輕盈透紗與細緻點點，讓經典黑色多一份柔美。','https://s.shopee.tw/4LJWafj3ml',[0,2,1]),
 ('奶灰竹葉長飄帶髮夾','水墨竹葉','淡雅竹葉落在奶灰布面，日常也能穿出新中式氣息。','https://s.shopee.tw/50ZDNuFVv9',[8,7,6,9]),
 ('煙灰竹葉蝴蝶結髮夾','水墨竹葉','水墨般的煙灰紋理，隨飄帶勾勒清雅背影。','https://s.shopee.tw/1qcBc68oGw',[11,13,10,12])
]
cards = []
for name, category, desc, product_url, photos in products:
    thumbs = ''
    for i, photo in enumerate(photos):
        alt = name + ' — ' + ('商品細節' if i == 0 else '配戴示範')
        thumbs += f'<button class="thumb" type="button" aria-label="查看{name}第{i+1}張照片" aria-pressed="{str(i == 0).lower()}" data-src="assets/photo-{photo}.jpg" data-alt="{alt}"><img draggable="false" src="assets/photo-{photo}.jpg" alt="" loading="lazy" width="42" height="50"></button>'
    cards.append(f'''<article class="product">
<div class="watermarked product-photo"><img class="product-image" draggable="false" src="assets/photo-{photos[0]}.jpg" alt="{name} — 商品細節" width="600" height="800" loading="lazy"><span class="watermark" aria-hidden="true">初。true</span></div>
<div class="thumbs" role="group" aria-label="{name}照片">{thumbs}</div>
<p class="category">{category}</p><h3>{name}</h3><p class="description">{desc}</p>
<a class="buy" href="{product_url}" target="_blank" rel="noopener noreferrer" aria-label="到蝦皮查看{name}價格與購買（另開分頁）">到蝦皮查看與購買 <span aria-hidden="true">↗</span></a></article>''')

html = '''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>初。true🍃｜把溫柔與浪漫，藏進每一個日常裡</title>
<meta name="description" content="初。true 精選蝴蝶結、奶油碎花、法式蕾絲與水墨竹葉髮飾。找到適合日常、約會與出遊的溫柔配件，前往蝦皮查看價格與購買。">
<meta name="theme-color" content="#faf7f2">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23faf7f2'/%3E%3Ctext x='32' y='46' text-anchor='middle' font-size='43' fill='%23945e48' font-family='serif'%3E初%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="styles.css"><script src="config.js" defer></script><script src="script.js" defer></script>
</head>
<body>
<a href="#collection" class="skip">跳到商品列表</a>
<header class="header"><a class="wordmark" href="#" aria-label="初。true🍃 首頁">初。<i>true</i></a><nav aria-label="主要導覽"><a href="#collection">精選髮飾</a><a href="#about">關於初</a><a class="shop-link" data-shop href="https://s.shopee.tw/qjeM1Vp5d" target="_blank" rel="noopener noreferrer">蝦皮選購 ↗</a></nav></header>
<main>
<section class="hero" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow">TRUE · THE LITTLE THINGS</p><h1 id="hero-title">把溫柔與浪漫，<br>藏進每一個<em>日常</em>裡。</h1><p>一朵碎花、一縷飄帶、一個剛剛好的蝴蝶結。<br>讓喜歡的模樣，從髮間悄悄開始。</p><a class="button" href="#collection">找到你的日常髮飾 <span aria-hidden="true">↓</span></a></div><figure class="hero-art"><div class="watermarked hero-main"><img class="marked-image" draggable="false" src="assets/photo-22.jpg" alt="奶油粉蝴蝶結點綴半綁髮，搭配溫柔白色洋裝" width="800" height="1000" fetchpriority="high"><span class="watermark" aria-hidden="true">初。true</span></div><div class="watermarked hero-detail"><img class="marked-image" draggable="false" src="assets/photo-23.jpg" alt="陽光下的奶油碎花蝴蝶結抓夾" width="400" height="500"><span class="watermark" aria-hidden="true">初。true</span></div><figcaption>A little romance, every day.</figcaption></figure></section>
<section id="collection" class="collection" aria-labelledby="collection-title"><div class="section-top"><div><p class="eyebrow">THE COLLECTION / 01—08</p><h2 id="collection-title">從髮間，遇見喜歡的自己</h2></div><p>八款精選髮飾 · 價格與庫存以蝦皮為準</p></div><div class="grid">'''
html += '\n'.join(cards)
html += '''</div></section>
<section id="about" class="about" aria-labelledby="about-title"><img class="about-logo" src="assets/logo.png" alt="初 true — THE STUDIO" width="500" height="500" loading="lazy"><div><p class="eyebrow" id="about-title">ABOUT TRUE</p><p>想了解款式或搭配？歡迎與我們聊聊。</p></div><a class="button" id="contact-button" href="https://s.shopee.tw/qjeM1Vp5d" target="_blank" rel="noopener noreferrer">到蝦皮詢問髮飾 ↗</a></section>
</main><footer class="footer"><span>© 初。true🍃 · 把溫柔與浪漫，藏進每一個日常裡。</span><a href="#collection">回到精選髮飾 ↑</a></footer>
</body></html>'''
Path(__file__).resolve().parent.joinpath('dist/index.html').write_text(html, encoding='utf-8')
print('Built 8 product cards.')
