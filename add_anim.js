const fs = require('fs');
const path = require('path');
const dir = 'preview';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
files.forEach(file => {
  const filepath = path.join(dir, file);
  let html = fs.readFileSync(filepath, 'utf8');
  html = html.replace(/class="main-header"/g, 'class="main-header anim-fade-up"');
  html = html.replace(/class="stat-card"/g, 'class="stat-card hover-tilt anim-fade-up"');
  html = html.replace(/class="table-container"/g, 'class="table-container hover-glow anim-fade-up" style="animation-delay: 0.1s"');
  html = html.replace(/class="auth-wrap"/g, 'class="auth-wrap anim-fade-up hover-glow"');
  html = html.replace(/class="pricing-tier"/g, 'class="pricing-tier hover-glow anim-fade-up"');
  fs.writeFileSync(filepath, html);
});
console.log('Added animations to all preview pages');
