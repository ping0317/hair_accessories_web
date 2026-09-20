document.querySelectorAll('.thumb').forEach(button => {
  button.addEventListener('click', () => {
    const card = button.closest('.product');
    const main = card.querySelector('.product-image');
    main.src = button.dataset.src;
    main.alt = button.dataset.alt;
    card.querySelectorAll('.thumb').forEach(thumb => thumb.setAttribute('aria-pressed', String(thumb === button)));
  });
});
const config = window.TRUE_CONFIG || {};
function safeHttps(value) {
  try { const url = new URL(value); return url.protocol === 'https:' ? url.href : null; }
  catch { return null; }
}
const lineUrl = safeHttps(config.lineUrl);
if (lineUrl) {
  const contact = document.querySelector('#contact-button');
  contact.href = lineUrl;
  contact.textContent = 'LINE 詢問髮飾';
}
const shopUrl = safeHttps(config.shopeeUrl);
if (shopUrl) document.querySelectorAll('[data-shop]').forEach(link => { link.href = shopUrl; });
