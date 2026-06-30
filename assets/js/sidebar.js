/**
 * ChainOps UI Kit — Shared Sidebar Injector
 * Injects consistent navigation markup into all preview pages.
 */
(function () {
  const SIDEBAR_HTML = `
<aside class="sidebar">
  <div class="brand">
    <div class="brand-mark">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
        <rect x="3" y="3" width="8" height="8" rx="2"/>
        <rect x="13" y="3" width="8" height="5" rx="2"/>
        <rect x="13" y="10" width="8" height="11" rx="2"/>
        <rect x="3" y="13" width="8" height="8" rx="2"/>
      </svg>
    </div>
    <div class="brand-copy">
      <strong>ChainOps</strong>
      <span>Web3 + AI Panel</span>
    </div>
  </div>

  <div class="nav-section-label">Dashboard</div>
  <div class="nav-list">
    <a class="nav-link" href="dashboard-overview.html" data-page="dashboard-overview">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="5" rx="2"/><rect x="13" y="10" width="8" height="11" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/></svg>
      <span>Overview</span>
    </a>
  </div>

  <div class="nav-section-label">Web3</div>
  <div class="nav-list">
    <a class="nav-link" href="web3-wallets.html" data-page="web3-wallets">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M16 13a1 1 0 1 0 2 0 1 1 0 0 0-2 0z"/></svg>
      <span>Wallets</span>
    </a>
    <a class="nav-link" href="web3-transactions.html" data-page="web3-transactions">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 16V4m0 0L3 8m4-4 4 4M17 8v12m0 0 4-4m-4 4-4-4"/></svg>
      <span>Transactions</span>
    </a>
  </div>

  <div class="nav-section-label">AI Ops</div>
  <div class="nav-list">
    <a class="nav-link" href="ai-prompts.html" data-page="ai-prompts">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3z"/><path d="M5 19l1 3 1-3 3-1-3-1-1-3-1 3-3 1 3 1z"/></svg>
      <span>Prompt Logs</span>
    </a>
    <a class="nav-link" href="ai-usage.html" data-page="ai-usage">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
      <span>Model Usage</span>
    </a>
  </div>

  <div class="nav-section-label">Settings</div>
  <div class="nav-list">
    <a class="nav-link" href="settings-profile.html" data-page="settings-profile">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
      <span>Profile</span>
    </a>
    <a class="nav-link" href="settings-billing.html" data-page="settings-billing">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
      <span>Billing</span>
    </a>
    <a class="nav-link" href="settings-team.html" data-page="settings-team">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="9" cy="7" r="4"/><path d="M2 21c0-3.5 3-6 7-6"/><circle cx="17" cy="11" r="3"/><path d="M14 21c0-2.8 2-4.5 4.5-4.5"/></svg>
      <span>Team</span>
    </a>
  </div>

  <div class="nav-section-label">Marketing</div>
  <div class="nav-list">
    <a class="nav-link" href="marketing-pricing.html" data-page="marketing-pricing">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6L12 2z"/></svg>
      <span>Pricing</span>
    </a>
    <a class="nav-link" href="components.html" data-page="components">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>
      <span>Components</span>
    </a>
  </div>

  <div class="nav-section-label">Auth</div>
  <div class="nav-list">
    <a class="nav-link" href="auth-login.html" data-page="auth-login"><span>Login</span></a>
    <a class="nav-link" href="auth-signup.html" data-page="auth-signup"><span>Sign Up</span></a>
    <a class="nav-link" href="auth-wallet.html" data-page="auth-wallet"><span>Wallet Connect</span></a>
  </div>

  <div class="sidebar-card">
    <p>Multi-chain analytics and team seat controls are included in the Pro tier.</p>
    <a class="btn btn-primary" href="settings-billing.html">Upgrade Plan</a>
  </div>
</aside>`;

  document.addEventListener('DOMContentLoaded', function () {
    /* Mark the current page's nav link as active */
    const page = location.pathname.split('/').pop().replace('.html','');
    document.querySelectorAll('.nav-link[data-page]').forEach(a => {
      a.classList.toggle('active', a.dataset.page === page);
    });
  });
})();
