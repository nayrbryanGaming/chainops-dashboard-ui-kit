const fs = require('fs');
const path = require('path');

const dir = 'preview';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
files.push('../index.html');

files.forEach(file => {
  const filepath = file === '../index.html' ? 'index.html' : path.join(dir, file);
  if (!fs.existsSync(filepath)) return;
  
  let html = fs.readFileSync(filepath, 'utf8');
  
  // Remove .html from internal links
  html = html.replace(/href="([^"]+)\.html"/g, 'href="$1"');
  
  fs.writeFileSync(filepath, html);
});
console.log('Removed .html from all links');
