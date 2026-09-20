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

// Limit casual image saving while preserving text selection and normal links.
function isProtectedImage(target) {
  return target instanceof Element && Boolean(target.closest('img, .watermarked, .thumb'));
}
for (const eventName of ['contextmenu', 'dragstart']) {
  document.addEventListener(eventName, event => {
    if (isProtectedImage(event.target)) {
      event.preventDefault();
      event.stopPropagation();
    }
  }, { capture: true });
}
document.querySelectorAll('img').forEach(image => { image.draggable = false; });
