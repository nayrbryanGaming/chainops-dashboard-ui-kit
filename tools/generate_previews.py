#!/usr/bin/env python3
"""Generate ChainOps preview HTML screens."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREVIEW = ROOT / "preview"

NAV = [
    ("Overview", "dashboard-overview.html", "dashboard"),
    ("Wallets", "web3-wallets.html", "dashboard"),
    ("Transactions", "web3-transactions.html", "dashboard"),
    ("Prompt Logs", "ai-prompts.html", "ai"),
    ("Model Usage", "ai-usage.html", "ai"),
    ("Profile", "settings-profile.html", "settings"),
    ("Billing", "settings-billing.html", "settings"),
    ("Team", "settings-team.html", "settings"),
    ("Pricing Page", "marketing-pricing.html", "marketing"),
    ("Components", "components.html", "marketing"),
]

AUTH_LINKS = [
    ("Login", "auth-login.html"),
    ("Sign Up", "auth-signup.html"),
    ("Wallet Connect", "auth-wallet.html"),
]


def icon(name: str) -> str:
    icons = {
        "dashboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="5" rx="2"/><rect x="13" y="10" width="8" height="11" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/></svg>',
        "ai": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3z"/><path d="M5 19l1 3 1-3 3-1-3-1-1-3-1 3-3 1 3 1z"/></svg>',
        "settings": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
        "marketing": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V5a2 2 0 012-2h9l5 5v11a2 2 0 01-2 2H6a2 2 0 01-2-2z"/><path d="M14 3v5h5"/></svg>',
    }
    return icons.get(name, icons["dashboard"])


def sidebar(active: str) -> str:
    sections = [
        ("Dashboard", "dashboard"),
        ("AI Ops", "ai"),
        ("Settings", "settings"),
        ("Marketing", "marketing"),
    ]
    links_html = ""
    for label, group in sections:
        links_html += f'<div class="nav-section-label">{label}</div><div class="nav-list">'
        for name, href, g in NAV:
            if g != group:
                continue
            cls = "nav-link active" if href == active else "nav-link"
            links_html += f'<a class="{cls}" href="{href}">{icon(g)}<span>{name}</span></a>'
        links_html += "</div>"

    auth_html = '<div class="nav-section-label">Auth Screens</div><div class="nav-list">'
    for name, href in AUTH_LINKS:
        cls = "nav-link active" if href == active else "nav-link"
        auth_html += f'<a class="{cls}" href="{href}"><span>{name}</span></a>'
    auth_html += "</div>"

    return f"""
<aside class="sidebar">
  <div class="brand">
    <div class="brand-mark">{icon('dashboard')}</div>
    <div class="brand-copy"><strong>ChainOps</strong><span>Web3 + AI Control Panel</span></div>
  </div>
  {links_html}
  {auth_html}
  <div class="sidebar-card">
    <p>Upgrade to Pro for multi-chain analytics and team seats.</p>
    <a class="btn btn-primary" href="settings-billing.html">Upgrade Plan</a>
  </div>
</aside>
"""


def shell(title: str, subtitle: str, active: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — ChainOps UI Kit</title>
  <link rel="stylesheet" href="../assets/css/chainops.css" />
</head>
<body>
  <div class="app-shell">
    {sidebar(active)}
    <main class="main">
      <div class="topbar">
        <div class="page-title">
          <h1>{title}</h1>
          <p>{subtitle}</p>
        </div>
        <div class="topbar-actions">
          <label class="search">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3-3"/></svg>
            <input type="search" placeholder="Search nodes, wallets, prompts..." />
          </label>
          <button class="btn btn-secondary">Export</button>
          <div class="avatar">AR</div>
        </div>
      </div>
      {body}
    </main>
  </div>
</body>
</html>
"""


def auth_shell(title: str, subtitle: str, active: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — ChainOps UI Kit</title>
  <link rel="stylesheet" href="../assets/css/chainops.css" />
</head>
<body>
  <div class="auth-layout">
    <section class="auth-hero">
      <div class="brand">
        <div class="brand-mark">{icon('dashboard')}</div>
        <div class="brand-copy"><strong>ChainOps</strong><span>Ship Web3 + AI products faster</span></div>
      </div>
      <div>
        <h1>Operate chains, models, and revenue in one premium dashboard.</h1>
        <p>Investor-ready UI for SaaS founders, agencies, and indie hackers building in Web3 and AI.</p>
      </div>
      <p style="color: var(--text-muted); font-size: 0.85rem;">© ChainOps UI Kit • Commercial license included</p>
    </section>
    <section class="auth-panel">
      <div class="auth-card">
        <h2>{title}</h2>
        <p class="subtitle">{subtitle}</p>
        {body}
      </div>
    </section>
  </div>
</body>
</html>
"""


PAGES = {
    "dashboard-overview.html": shell(
        "Overview",
        "Monitor network health, AI spend, and treasury signals in real time.",
        "dashboard-overview.html",
        """
      <section class="grid-stats">
        <article class="card"><div class="stat-label">Total Volume (24h)</div><div class="stat-value">$1.28M</div><div class="stat-delta up">+12.4% vs yesterday</div></article>
        <article class="card"><div class="stat-label">Active Wallets</div><div class="stat-value">8,942</div><div class="stat-delta up">+4.1% weekly</div></article>
        <article class="card"><div class="stat-label">AI Token Spend</div><div class="stat-value">$3,420</div><div class="stat-delta down">-2.8% optimized</div></article>
        <article class="card"><div class="stat-label">Node Uptime</div><div class="stat-value">99.98%</div><div class="stat-delta up">All regions healthy</div></article>
      </section>
      <section class="grid-2">
        <article class="card">
          <div class="card-header"><div><h2>Network Activity</h2><span>Cross-chain transaction throughput</span></div><span class="badge info">Live</span></div>
          <div class="chart"></div>
        </article>
        <article class="card">
          <div class="card-header"><h2>Recent Alerts</h2></div>
          <div class="table-wrap">
            <table>
              <tbody>
                <tr><td>Gas spike detected</td><td class="mono">Base</td><td><span class="badge warning">Medium</span></td></tr>
                <tr><td>Model latency above SLA</td><td class="mono">GPT-4o</td><td><span class="badge warning">Watch</span></td></tr>
                <tr><td>Treasury rebalance complete</td><td class="mono">Safe</td><td><span class="badge success">Resolved</span></td></tr>
                <tr><td>New validator online</td><td class="mono">Solana</td><td><span class="badge info">Info</span></td></tr>
              </tbody>
            </table>
          </div>
        </article>
      </section>
        """,
    ),
    "web3-wallets.html": shell(
        "Wallets",
        "Track treasury wallets, signers, and chain distribution.",
        "web3-wallets.html",
        """
      <section class="grid-3">
        <article class="card"><div class="stat-label">Treasury Balance</div><div class="stat-value">842.6 ETH</div><div class="stat-delta up">+$128K this week</div></article>
        <article class="card"><div class="stat-label">Multisig Signers</div><div class="stat-value">5 / 9</div><div class="stat-delta up">Quorum ready</div></article>
        <article class="card"><div class="stat-label">Risk Score</div><div class="stat-value">Low</div><div class="stat-delta up">No anomalies</div></article>
      </section>
      <article class="card">
        <div class="card-header"><div><h2>Connected Wallets</h2><p>Production treasury and operational wallets</p></div><button class="btn btn-primary">Add Wallet</button></div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Name</th><th>Address</th><th>Chain</th><th>Balance</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>Treasury Safe</td><td class="mono">0x71C...9Fa2</td><td>Ethereum</td><td>612.4 ETH</td><td><span class="badge success">Active</span></td></tr>
              <tr><td>Ops Hot Wallet</td><td class="mono">0xA13...88B1</td><td>Base</td><td>42.8 ETH</td><td><span class="badge success">Active</span></td></tr>
              <tr><td>Solana Vault</td><td class="mono">9xQe...kLm4</td><td>Solana</td><td>18,420 SOL</td><td><span class="badge info">Synced</span></td></tr>
              <tr><td>Grant Multisig</td><td class="mono">0x55D...C901</td><td>Arbitrum</td><td>96.2 ETH</td><td><span class="badge warning">Review</span></td></tr>
            </tbody>
          </table>
        </div>
      </article>
        """,
    ),
    "web3-transactions.html": shell(
        "Transactions",
        "Audit on-chain activity with filters, labels, and export.",
        "web3-transactions.html",
        """
      <section class="grid-2">
        <article class="card">
          <div class="card-header"><h2>Filter</h2></div>
          <div class="field"><label>Chain</label><select><option>All chains</option><option>Ethereum</option><option>Solana</option></select></div>
          <div class="field"><label>Status</label><select><option>All statuses</option><option>Confirmed</option><option>Pending</option></select></div>
          <div class="field"><label>Min Amount (USD)</label><input type="text" value="1000" /></div>
          <button class="btn btn-primary">Apply Filters</button>
        </article>
        <article class="card">
          <div class="card-header"><h2>24h Summary</h2></div>
          <div class="stat-label">Confirmed Transactions</div><div class="stat-value">1,284</div>
          <div class="progress" style="margin: 16px 0;"><span style="width: 78%;"></span></div>
          <p style="color: var(--text-secondary); margin: 0;">78% matched to treasury policy rules.</p>
        </article>
      </section>
      <article class="card">
        <div class="card-header"><div><h2>Latest Transactions</h2><p>Real-time feed with policy tags</p></div><button class="btn btn-secondary">Download CSV</button></div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Hash</th><th>From</th><th>To</th><th>Amount</th><th>Chain</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td class="mono">0x9f2...11aa</td><td class="mono">Treasury</td><td class="mono">0x44...901</td><td>$42,800</td><td>Ethereum</td><td><span class="badge success">Confirmed</span></td></tr>
              <tr><td class="mono">5kL...9Qm1</td><td class="mono">Ops</td><td class="mono">Jup...Pool</td><td>$8,120</td><td>Solana</td><td><span class="badge success">Confirmed</span></td></tr>
              <tr><td class="mono">0x18a...77fe</td><td class="mono">Grant</td><td class="mono">0x90...221</td><td>$12,000</td><td>Arbitrum</td><td><span class="badge warning">Pending</span></td></tr>
            </tbody>
          </table>
        </div>
      </article>
        """,
    ),
    "ai-prompts.html": shell(
        "Prompt Logs",
        "Inspect prompt history, latency, and safety flags.",
        "ai-prompts.html",
        """
      <section class="grid-stats">
        <article class="card"><div class="stat-label">Requests (24h)</div><div class="stat-value">18,204</div><div class="stat-delta up">+9.2%</div></article>
        <article class="card"><div class="stat-label">Avg Latency</div><div class="stat-value">420ms</div><div class="stat-delta up">-38ms</div></article>
        <article class="card"><div class="stat-label">Safety Flags</div><div class="stat-value">12</div><div class="stat-delta down">Needs review</div></article>
        <article class="card"><div class="stat-label">Success Rate</div><div class="stat-value">99.2%</div><div class="stat-delta up">Stable</div></article>
      </section>
      <article class="card">
        <div class="card-header"><div><h2>Recent Prompts</h2><p>Searchable audit trail for AI operations</p></div><button class="btn btn-secondary">Export Logs</button></div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Timestamp</th><th>Model</th><th>Prompt</th><th>Tokens</th><th>Latency</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td class="mono">2026-06-17 09:14</td><td>GPT-4o</td><td>Summarize treasury rebalance policy...</td><td>842</td><td>380ms</td><td><span class="badge success">OK</span></td></tr>
              <tr><td class="mono">2026-06-17 09:11</td><td>Claude 3.5</td><td>Generate investor update for Q2...</td><td>1,204</td><td>510ms</td><td><span class="badge success">OK</span></td></tr>
              <tr><td class="mono">2026-06-17 09:03</td><td>GPT-4o mini</td><td>Classify wallet risk for 0x55D...</td><td>318</td><td>190ms</td><td><span class="badge warning">Flagged</span></td></tr>
            </tbody>
          </table>
        </div>
      </article>
        """,
    ),
    "ai-usage.html": shell(
        "Model Usage",
        "Track spend, quotas, and model performance by team.",
        "ai-usage.html",
        """
      <section class="grid-2">
        <article class="card">
          <div class="card-header"><div><h2>Spend by Model</h2><span>Current billing cycle</span></div></div>
          <div class="chart"></div>
        </article>
        <article class="card">
          <div class="card-header"><h2>Quota Usage</h2></div>
          <p class="stat-label">GPT-4o</p><div class="progress" style="margin-bottom: 14px;"><span style="width: 72%;"></span></div>
          <p class="stat-label">Claude 3.5</p><div class="progress" style="margin-bottom: 14px;"><span style="width: 54%;"></span></div>
          <p class="stat-label">Embeddings</p><div class="progress"><span style="width: 88%;"></span></div>
        </article>
      </section>
      <section class="grid-3">
        <article class="card"><div class="stat-label">Monthly Budget</div><div class="stat-value">$5,000</div></article>
        <article class="card"><div class="stat-label">Used</div><div class="stat-value">$3,420</div></article>
        <article class="card"><div class="stat-label">Projected</div><div class="stat-value">$4,880</div></article>
      </section>
        """,
    ),
    "settings-profile.html": shell(
        "Profile Settings",
        "Manage identity, security preferences, and API access.",
        "settings-profile.html",
        """
      <section class="grid-2">
        <article class="card">
          <div class="card-header"><h2>Personal Info</h2></div>
          <div class="field"><label>Full Name</label><input type="text" value="Alex Rivera" /></div>
          <div class="field"><label>Work Email</label><input type="email" value="alex@chainops.io" /></div>
          <div class="field"><label>Role</label><input type="text" value="Founder / CTO" /></div>
          <button class="btn btn-primary">Save Changes</button>
        </article>
        <article class="card">
          <div class="card-header"><h2>Security</h2></div>
          <p style="color: var(--text-secondary);">Two-factor authentication is enabled for this workspace.</p>
          <div style="display:flex; gap:12px; margin-top: 18px;">
            <button class="btn btn-secondary">Rotate API Keys</button>
            <button class="btn btn-ghost">View Sessions</button>
          </div>
        </article>
      </section>
        """,
    ),
    "settings-billing.html": shell(
        "Billing",
        "Plans, invoices, and payment methods for your workspace.",
        "settings-billing.html",
        """
      <section class="grid-2">
        <article class="card">
          <div class="card-header"><div><h2>Current Plan</h2><p>Pro • Renews July 12, 2026</p></div><span class="badge purple">Popular</span></div>
          <div class="stat-value">$79<span style="font-size:1rem;color:var(--text-secondary);">/mo</span></div>
          <ul class="feature-list">
            <li>Up to 10 team seats</li>
            <li>Multi-chain analytics</li>
            <li>AI usage guardrails</li>
          </ul>
          <button class="btn btn-primary" style="margin-top:18px;">Manage Subscription</button>
        </article>
        <article class="card">
          <div class="card-header"><h2>Invoices</h2></div>
          <div class="table-wrap">
            <table>
              <thead><tr><th>Date</th><th>Amount</th><th>Status</th></tr></thead>
              <tbody>
                <tr><td>Jun 12, 2026</td><td>$79.00</td><td><span class="badge success">Paid</span></td></tr>
                <tr><td>May 12, 2026</td><td>$79.00</td><td><span class="badge success">Paid</span></td></tr>
                <tr><td>Apr 12, 2026</td><td>$79.00</td><td><span class="badge success">Paid</span></td></tr>
              </tbody>
            </table>
          </div>
        </article>
      </section>
        """,
    ),
    "settings-team.html": shell(
        "Team",
        "Invite collaborators and manage role-based access.",
        "settings-team.html",
        """
      <article class="card">
        <div class="card-header"><div><h2>Team Members</h2><p>5 seats used of 10 available</p></div><button class="btn btn-primary">Invite Member</button></div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Name</th><th>Email</th><th>Role</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>Alex Rivera</td><td>alex@chainops.io</td><td>Owner</td><td><span class="badge success">Active</span></td></tr>
              <tr><td>Maya Chen</td><td>maya@chainops.io</td><td>Admin</td><td><span class="badge success">Active</span></td></tr>
              <tr><td>Jonah Park</td><td>jonah@chainops.io</td><td>Analyst</td><td><span class="badge info">Invited</span></td></tr>
            </tbody>
          </table>
        </div>
      </article>
        """,
    ),
    "marketing-pricing.html": shell(
        "Pricing Page",
        "Marketing-ready pricing layout for your SaaS landing page.",
        "marketing-pricing.html",
        """
      <section class="pricing-grid">
        <article class="card pricing-card">
          <h3>Starter</h3><div class="price">$29</div><p style="color:var(--text-secondary);">For solo founders validating ideas.</p>
          <ul class="feature-list"><li>1 workspace</li><li>Basic analytics</li><li>Email support</li></ul>
          <button class="btn btn-secondary" style="margin-top:18px;width:100%;">Choose Starter</button>
        </article>
        <article class="card pricing-card featured">
          <span class="badge info">Best Value</span>
          <h3>Pro</h3><div class="price">$79</div><p style="color:var(--text-secondary);">For teams shipping Web3 + AI products.</p>
          <ul class="feature-list"><li>10 seats</li><li>Multi-chain ops</li><li>AI guardrails</li><li>Priority support</li></ul>
          <button class="btn btn-primary" style="margin-top:18px;width:100%;">Choose Pro</button>
        </article>
        <article class="card pricing-card">
          <h3>Enterprise</h3><div class="price">Custom</div><p style="color:var(--text-secondary);">For regulated teams and custom SLAs.</p>
          <ul class="feature-list"><li>Unlimited seats</li><li>SSO + audit logs</li><li>Dedicated success</li></ul>
          <button class="btn btn-secondary" style="margin-top:18px;width:100%;">Talk to Sales</button>
        </article>
      </section>
        """,
    ),
    "components.html": shell(
        "Components",
        "Reusable UI building blocks from the ChainOps design system.",
        "components.html",
        """
      <section class="component-grid">
        <article class="card"><div class="card-header"><h3>Buttons</h3></div><div style="display:flex; gap:12px; flex-wrap:wrap;"><button class="btn btn-primary">Primary</button><button class="btn btn-secondary">Secondary</button><button class="btn btn-ghost">Ghost</button></div></article>
        <article class="card"><div class="card-header"><h3>Badges</h3></div><div style="display:flex; gap:10px; flex-wrap:wrap;"><span class="badge success">Success</span><span class="badge warning">Warning</span><span class="badge info">Info</span><span class="badge purple">Purple</span></div></article>
        <article class="card"><div class="card-header"><h3>Form Fields</h3></div><div class="field"><label>Project Name</label><input type="text" placeholder="ChainOps Labs" /></div><div class="field"><label>Plan</label><select><option>Pro</option></select></div></article>
        <article class="card"><div class="card-header"><h3>Stats</h3></div><div class="stat-label">Monthly Recurring Revenue</div><div class="stat-value">$84,200</div><div class="stat-delta up">+18.2% MoM</div></article>
      </section>
        """,
    ),
    "auth-login.html": auth_shell(
        "Welcome back",
        "Sign in to your ChainOps workspace.",
        "auth-login.html",
        """
        <div class="field"><label>Email</label><input type="email" placeholder="you@company.com" /></div>
        <div class="field"><label>Password</label><input type="password" placeholder="••••••••" /></div>
        <button class="btn btn-primary" style="width:100%;">Sign In</button>
        <div class="divider">or continue with</div>
        <button class="btn btn-secondary" style="width:100%;">Connect Wallet</button>
        <p style="margin-top:18px;color:var(--text-secondary);font-size:0.9rem;">No account? <a href="auth-signup.html" style="color:var(--accent-cyan);">Create one</a></p>
        """,
    ),
    "auth-signup.html": auth_shell(
        "Create account",
        "Launch your Web3 + AI control panel in minutes.",
        "auth-signup.html",
        """
        <div class="field"><label>Full Name</label><input type="text" placeholder="Alex Rivera" /></div>
        <div class="field"><label>Work Email</label><input type="email" placeholder="you@company.com" /></div>
        <div class="field"><label>Password</label><input type="password" placeholder="Create a strong password" /></div>
        <button class="btn btn-primary" style="width:100%;">Create Account</button>
        <p style="margin-top:18px;color:var(--text-secondary);font-size:0.9rem;">Already have an account? <a href="auth-login.html" style="color:var(--accent-cyan);">Sign in</a></p>
        """,
    ),
    "auth-wallet.html": auth_shell(
        "Connect wallet",
        "Authenticate with your preferred Web3 wallet provider.",
        "auth-wallet.html",
        """
        <div class="wallet-grid">
          <div class="wallet-option"><strong>MetaMask</strong><p style="margin:8px 0 0;color:var(--text-secondary);font-size:0.85rem;">Browser extension</p></div>
          <div class="wallet-option"><strong>Phantom</strong><p style="margin:8px 0 0;color:var(--text-secondary);font-size:0.85rem;">Solana ecosystem</p></div>
          <div class="wallet-option"><strong>WalletConnect</strong><p style="margin:8px 0 0;color:var(--text-secondary);font-size:0.85rem;">Mobile wallets</p></div>
          <div class="wallet-option"><strong>Coinbase</strong><p style="margin:8px 0 0;color:var(--text-secondary);font-size:0.85rem;">Exchange wallet</p></div>
        </div>
        <button class="btn btn-primary" style="width:100%; margin-top:18px;">Continue</button>
        """,
    ),
}


def hub_page() -> str:
    cards = []
    screens = [
        ("Overview Dashboard", "Operational KPI hub for Web3 + AI teams.", "dashboard-overview.html"),
        ("Wallet Management", "Treasury and signer monitoring.", "web3-wallets.html"),
        ("Transaction Feed", "Audit-ready on-chain activity table.", "web3-transactions.html"),
        ("Prompt Logs", "AI request audit trail.", "ai-prompts.html"),
        ("Model Usage", "Spend and quota analytics.", "ai-usage.html"),
        ("Profile Settings", "Identity and security controls.", "settings-profile.html"),
        ("Billing", "Subscription and invoice management.", "settings-billing.html"),
        ("Team Access", "Roles and invitations.", "settings-team.html"),
        ("Pricing Page", "Marketing-ready SaaS pricing layout.", "marketing-pricing.html"),
        ("Component Library", "Buttons, badges, forms, stats.", "components.html"),
        ("Login", "Auth screen with split hero layout.", "auth-login.html"),
        ("Sign Up", "Registration flow.", "auth-signup.html"),
        ("Wallet Connect", "Web3 wallet picker screen.", "auth-wallet.html"),
    ]
    for title, desc, href in screens:
        cards.append(
            f'<a class="screen-card" href="{href}"><h3>{title}</h3><p>{desc}</p><span class="btn btn-secondary">Open Screen</span></a>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ChainOps UI Kit Preview Hub</title>
  <link rel="stylesheet" href="../assets/css/chainops.css" />
</head>
<body>
  <div class="preview-hub">
    <header>
      <div class="brand" style="justify-content:center; margin-bottom: 18px;">
        <div class="brand-mark">{icon('dashboard')}</div>
        <div class="brand-copy"><strong>ChainOps UI Kit</strong><span>40+ screen system • Web3 + AI SaaS</span></div>
      </div>
      <h1>Premium Dashboard Preview Hub</h1>
      <p>Open any screen below. Every layout is production-ready HTML/CSS with a shared design system, perfect for Gumroad buyers, pitch decks, and rapid product prototyping.</p>
    </header>
    <section class="screen-grid">
      {''.join(cards)}
    </section>
  </div>
</body>
</html>
"""


def main() -> None:
    PREVIEW.mkdir(parents=True, exist_ok=True)
    for filename, html in PAGES.items():
        (PREVIEW / filename).write_text(html, encoding="utf-8")
    (PREVIEW / "index.html").write_text(hub_page(), encoding="utf-8")
    print(f"Generated {len(PAGES) + 1} preview screens in {PREVIEW}")


if __name__ == "__main__":
    main()
