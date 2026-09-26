# 初。true🍃

八款髮飾的靜態展示網站。網站檔案全在 `dist/`，不需要 npm、建置工具或後端；可直接開啟 `dist/index.html`，也可用 `python -m http.server 4173 --directory dist` 預覽。

## GitHub Pages

Website: https://ping0317.github.io/hair_accessories_web/
Repository: https://github.com/ping0317/hair_accessories_web

Source is on main. GitHub Pages serves the root of gh-pages. Only the contents of dist are deployed; original spreadsheets and source photos remain local.

To publish an update, commit and push main, then run:

```sh
git subtree split --prefix dist -b pages-release-next
git push origin pages-release-next:gh-pages
```

Use a fresh temporary branch name for each release. GitHub Pages publishes updates pushed to gh-pages automatically.

## 後續更新

- LINE：在 `dist/config.js` 填入 `lineUrl`，例如官方提供的 `https://lin.ee/...`；頁尾詢問按鈕會改為 LINE。尚未設定時使用蝦皮詢問入口，不顯示無效按鈕。
- 賣場：同一設定檔的 `shopeeUrl`。
- 商品：可修改 `build.py` 商品清單及文案，再執行 `python build.py` 產生 `dist/index.html`；發布時不需執行建置。Product URLs use the owner-provided Shopee short links.
- 圖片：`dist/assets/` 是縮小與壓縮後的網站用圖，原始圖片保留不變。奶油粉資料夾內重複的黑色印花照片只用於黑色印花商品。
- 價格與庫存：以蝦皮頁面為準，本站不保留價格。

文字及商品圖可在停用 JavaScript 時正常閱讀；JavaScript 用於切換商品照片與套用聯絡設定。


## 搜尋收錄與 SEO

首頁具有 canonical、搜尋摘要、Organization / CollectionPage / ItemList JSON-LD 與圖片 sitemap。商品價格與庫存由蝦皮提供，因此不建立虛構的 Offer、評分或評論，也不宣稱具備 Google 商品複合搜尋結果資格。

### Google Search Console

1. 新增「網址前置字元」資源：`https://ping0317.github.io/hair_accessories_web/`。
2. 使用 HTML 標記驗證。將 Google 提供的 content 值填入專案根目錄 `search-console-verification.txt`，執行 `python build.py` 並發布。驗證碼會出现在公開 HTML，屬於 Google 所要求的公開驗證資料。
3. 返回 Search Console 驗證，提交 `https://ping0317.github.io/hair_accessories_web/sitemap.xml`。
4. 使用網址審查檢查首頁，測試即時網址後按「要求建立索引」。記錄 Google 選用的標準網址與收錄狀態。
5. 收錄後觀察「成效」中的實際查詢字詞、曝光、點擊與排名，再決定需要哪些有實質商品資訊的專頁。

網站位於 GitHub Pages 子目錄。有效 robots.txt 必須位於 `https://ping0317.github.io/robots.txt`，在本專案子目錄新增 robots.txt 並不能設定主機爬蟲規則。檢查時根目錄回應 404，並未發現封鎖；sitemap 以 Search Console 提交。不要為了 SEO 隱藏文字、堆疊關鍵字或虛構價格、評論。

原始素材已是公開網頁圖片；右鍵限制不是 robots 封鎖，不妨礙搜尋引擎讀取 HTML 的圖片網址。既有浮水印與圖片比例規則不變。
