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
- 商品：可修改 `build.py` 商品清單及文案，再執行 `python build.py` 產生 `dist/index.html`；發布時不需執行建置。商品連結依提供的賣家 ID 與 Excel 商品 ID 組成，需在可登入蝦皮的瀏覽器確認商品落點。
- 圖片：`dist/assets/` 是縮小與壓縮後的網站用圖，原始圖片保留不變。奶油粉資料夾內重複的黑色印花照片只用於黑色印花商品。
- 價格與庫存：以蝦皮頁面為準，本站不保留價格。

文字及商品圖可在停用 JavaScript 時正常閱讀；JavaScript 用於切換商品照片與套用聯絡設定。
