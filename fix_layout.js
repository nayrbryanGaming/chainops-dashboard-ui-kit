const fs = require('fs');
const path = require('path');

// 1. Fix CSS for min-height
let cssPath = path.join('assets', 'css', 'chainops.css');
let css = fs.readFileSync(cssPath, 'utf8');
if (!css.includes('.app-shell { min-height: 100vh;')) {
  css = css.replace('.app-shell {', '.app-shell { min-height: 100vh;');
}
if (!css.includes('.main { min-height: 100vh;')) {
  css = css.replace('.main {', '.main { min-height: 100vh;');
}
fs.writeFileSync(cssPath, css);

// 2. Add link to brand in all preview files
const dir = 'preview';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
  const filepath = path.join(dir, file);
  let html = fs.readFileSync(filepath, 'utf8');
  
  html = html.replace(
    '<div class="brand"><div class="brand-mark">', 
    '<a href="/" class="brand" style="text-decoration:none;"><div class="brand-mark">'
  );
  html = html.replace(
    '</div><div class="brand-copy"><strong>ChainOps</strong><span>Web3 + AI Panel</span></div></div>',
    '</div><div class="brand-copy"><strong>ChainOps</strong><span>Web3 + AI Panel</span></div></a>'
  );
  
  fs.writeFileSync(filepath, html);
});
console.log('Fixed CSS and added links to brand');
