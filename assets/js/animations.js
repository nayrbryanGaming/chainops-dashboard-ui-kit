/**
 * ChainOps UI Kit — Shared Animation Engine
 * Runs on all preview pages automatically.
 */
(function () {
  'use strict';

  /* ──────────────────────────────────────────────
     1. SCROLL REVEAL
  ────────────────────────────────────────────── */
  function initReveal() {
    const els = document.querySelectorAll(
      '.card, .stat-card, article.card, .topbar, .sidebar, .page-title, section'
    );
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

    els.forEach((el, i) => {
      if (!el.classList.contains('stat-card-anim')) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(14px)';
        el.style.transition = `opacity 0.5s ease ${i * 45}ms, transform 0.5s ease ${i * 45}ms`;
      }
      obs.observe(el);
    });

    new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'none';
        }
      });
    }, { threshold: 0.08 }).observe;
  }

  /* ──────────────────────────────────────────────
     2. CARD ENTRANCE — fires immediately
  ────────────────────────────────────────────── */
  function initCardEntrance() {
    const cards = document.querySelectorAll(
      'article.card, .card, .pricing-card, .auth-card'
    );
    cards.forEach((c, i) => {
      c.style.animationDelay = `${i * 55}ms`;
      c.classList.add('anim-fade-up', 'anim-both');
    });
  }

  /* ──────────────────────────────────────────────
     3. SIDEBAR SLIDE-IN
  ────────────────────────────────────────────── */
  function initSidebar() {
    const sb = document.querySelector('.sidebar');
    if (sb) sb.classList.add('sidebar-anim-in');
    const tb = document.querySelector('.topbar');
    if (tb) tb.classList.add('topbar-anim-in');
    const main = document.querySelector('.main');
    if (main) main.classList.add('main-anim-in');
  }

  /* ──────────────────────────────────────────────
     4. STAT CARD COUNTER ANIMATION
  ────────────────────────────────────────────── */
  function initCounters() {
    const statValues = document.querySelectorAll('.stat-value');
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const raw = el.textContent.trim();
        const prefix = raw.match(/^[^0-9]*/)?.[0] ?? '';
        const suffix = raw.match(/[^0-9.]*$/)?.[0] ?? '';
        const numStr = raw.replace(/[^0-9.]/g, '');
        const target = parseFloat(numStr);
        if (isNaN(target) || target === 0) return;

        let cur = 0;
        const dur = 1200;
        const steps = 50;
        const inc = target / steps;
        const interval = dur / steps;

        const tick = () => {
          cur = Math.min(cur + inc, target);
          const display = Number.isInteger(target)
            ? Math.round(cur).toLocaleString()
            : cur.toFixed(2);
          el.textContent = prefix + display + suffix;
          if (cur < target) setTimeout(tick, interval);
        };
        tick();
        obs.unobserve(el);
      });
    }, { threshold: 0.4 });
    statValues.forEach((el) => obs.observe(el));
  }

  /* ──────────────────────────────────────────────
     5. SVG CHART LINE DRAW
  ────────────────────────────────────────────── */
  function initCharts() {
    const paths = document.querySelectorAll('.chart-path');
    paths.forEach((path) => {
      const len = path.getTotalLength ? path.getTotalLength() : 800;
      path.style.strokeDasharray = len;
      path.style.strokeDashoffset = len;
      path.style.transition = 'stroke-dashoffset 2s cubic-bezier(0.4,0,0.2,1)';

      const obs = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            setTimeout(() => { path.style.strokeDashoffset = '0'; }, 300);
            obs.unobserve(path);
          }
        });
      }, { threshold: 0.2 });
      obs.observe(path);
    });

    /* Auto-draw all animated charts */
    document.querySelectorAll('.chart-line-draw').forEach((path) => {
      const obs2 = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            path.style.animationPlayState = 'running';
            obs2.unobserve(path);
          }
        });
      }, { threshold: 0.1 });
      obs2.observe(path);
    });
  }

  /* ──────────────────────────────────────────────
     6. PROGRESS BAR FILL
  ────────────────────────────────────────────── */
  function initProgressBars() {
    const bars = document.querySelectorAll('.progress-bar, .bar-fill');
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          const el = e.target;
          const w = el.dataset.w || el.style.getPropertyValue('--target-w') || '75%';
          el.style.transform = 'scaleX(0)';
          el.style.transformOrigin = 'left center';
          el.style.transition = 'transform 1.2s cubic-bezier(0.4,0,0.2,1)';
          requestAnimationFrame(() => {
            el.style.transform = 'scaleX(1)';
          });
          obs.unobserve(el);
        }
      });
    }, { threshold: 0.2 });
    bars.forEach((b) => obs.observe(b));
  }

  /* ──────────────────────────────────────────────
     7. 3D TILT — all cards
  ────────────────────────────────────────────── */
  function initTilt() {
    document.querySelectorAll('.card, article.card').forEach((card) => {
      card.style.transition = 'transform 0.12s ease';
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width;
        const y = (e.clientY - r.top)  / r.height;
        const tX = (y - 0.5) * -6;
        const tY = (x - 0.5) *  6;
        card.style.transform = `perspective(600px) rotateX(${tX}deg) rotateY(${tY}deg) translateZ(4px)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  /* ──────────────────────────────────────────────
     8. TABLE ROW HOVER HIGHLIGHT
  ────────────────────────────────────────────── */
  function initTableRows() {
    document.querySelectorAll('table tr, .table tr').forEach((row) => {
      row.classList.add('table-hover-row');
    });
  }

  /* ──────────────────────────────────────────────
     9. BADGE LIVE PULSE
  ────────────────────────────────────────────── */
  function initBadges() {
    document.querySelectorAll('.badge.info').forEach((b) => {
      if (b.textContent.trim().toLowerCase() === 'live') {
        b.classList.add('badge-live');
      }
    });
  }

  /* ──────────────────────────────────────────────
     10. STAT DELTA MICRO-ANIMATION
  ────────────────────────────────────────────── */
  function initStatDeltas() {
    document.querySelectorAll('.stat-delta.up').forEach((el) => {
      el.style.animation = 'fadeRight 0.5s ease both';
    });
    document.querySelectorAll('.stat-delta.down').forEach((el) => {
      el.style.animation = 'fadeLeft 0.5s ease both';
    });
  }

  /* ──────────────────────────────────────────────
     11. NAV LINK ACTIVE UNDERLINE
  ────────────────────────────────────────────── */
  function initNavLinks() {
    document.querySelectorAll('.nav-link').forEach((a) => {
      a.classList.add('nav-link-animated');
    });
  }

  /* ──────────────────────────────────────────────
     12. CURSOR GLOW (light follow)
  ────────────────────────────────────────────── */
  function initCursorGlow() {
    const glow = document.createElement('div');
    glow.id = 'page-cursor-glow';
    glow.style.cssText = `
      position:fixed;width:300px;height:300px;border-radius:50%;pointer-events:none;z-index:9999;
      background:radial-gradient(circle at center,rgba(34,211,238,0.05) 0%,transparent 65%);
      transform:translate(-50%,-50%);transition:left 0.05s,top 0.05s;
    `;
    document.body.appendChild(glow);
    document.addEventListener('mousemove', (e) => {
      glow.style.left = e.clientX + 'px';
      glow.style.top  = e.clientY + 'px';
    });
  }

  /* ──────────────────────────────────────────────
     INIT
  ────────────────────────────────────────────── */
  function boot() {
    initSidebar();
    initCardEntrance();
    initCounters();
    initCharts();
    initProgressBars();
    initTilt();
    initTableRows();
    initBadges();
    initStatDeltas();
    initNavLinks();
    initCursorGlow();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
