const fs = require('fs');
const path = require('path');

const previewDir = path.join(__dirname, 'preview');
const files = fs.readdirSync(previewDir).filter(f => f.endsWith('.html'));

const dict = {
  // Navigation / Header
  'Dashboard Overview': 'Ringkasan Dasbor',
  'Dashboard': 'Dasbor',
  'Connect Wallet': 'Hubungkan Dompet',
  'Wallet': 'Dompet',
  'Search transactions, wallets...': 'Cari transaksi, dompet...',
  'Search...': 'Cari...',
  'Log out': 'Keluar',
  'Profile': 'Profil',
  'Settings': 'Pengaturan',
  'Pricing': 'Harga',
  
  // Dashboard Overviews
  'Total Revenue': 'Total Pendapatan',
  'Active Users': 'Pengguna Aktif',
  'New Signups': 'Pendaftar Baru',
  'Conversion Rate': 'Tingkat Konversi',
  'Recent Activity': 'Aktivitas Terbaru',
  'Transaction History': 'Riwayat Transaksi',
  'View All': 'Lihat Semua',
  'Status': 'Status',
  'Date': 'Tanggal',
  'Amount': 'Jumlah',
  'Completed': 'Selesai',
  'Pending': 'Tertunda',
  'Failed': 'Gagal',

  // Auth / Login
  'Sign In to ChainOps': 'Masuk ke ChainOps',
  'Sign In': 'Masuk',
  'Sign Up': 'Daftar',
  'Create an account': 'Buat akun',
  'Email Address': 'Alamat Email',
  'Password': 'Kata Sandi',
  'Remember me': 'Ingat saya',
  'Forgot password?': 'Lupa kata sandi?',
  'Or continue with': 'Atau masuk dengan',
  "Don't have an account?": 'Belum punya akun?',
  'Already have an account?': 'Sudah punya akun?',

  // Web3
  'Web3 Transactions': 'Transaksi Web3',
  'Web3 Wallets': 'Dompet Web3',
  'Network': 'Jaringan',
  'Gas Fee': 'Biaya Gas',
  'Smart Contract': 'Kontrak Pintar',
  'Tokens': 'Token',
  
  // Settings
  'Team Settings': 'Pengaturan Tim',
  'Billing': 'Tagihan',
  'Update Profile': 'Perbarui Profil',
  'Save Changes': 'Simpan Perubahan',
  'Current Plan': 'Paket Saat Ini',
  'Upgrade Plan': 'Tingkatkan Paket',
  'Cancel Subscription': 'Batalkan Langganan',
  'Payment Methods': 'Metode Pembayaran',
  'Add new card': 'Tambah kartu baru',
  'Invite Member': 'Undang Anggota',
  'Role': 'Peran',
  'Admin': 'Admin',
  'Member': 'Anggota',

  // AI Prompts
  'AI Usage': 'Penggunaan AI',
  'AI Prompts': 'Prompt AI',
  'Generate': 'Hasilkan',
  'Tokens Used': 'Token Terpakai',
  'Remaining': 'Tersisa',
  'Prompt Library': 'Pustaka Prompt',
  'New Prompt': 'Prompt Baru',
  'Copy': 'Salin',
  
  // Marketing
  'Features': 'Fitur Utama',
  'Preview': 'Pratinjau',
  'Get the Kit': 'Dapatkan Sekarang',
  
  // Generic / Misc
  'Loading...': 'Memuat...',
  'Success': 'Berhasil',
  'Error': 'Terjadi Kesalahan',
  'Cancel': 'Batal',
  'Submit': 'Kirim',
  'Delete': 'Hapus',
  'Edit': 'Ubah',
  'Yes': 'Ya',
  'No': 'Tidak'
};

files.forEach(file => {
  const filePath = path.join(previewDir, file);
  let content = fs.readFileSync(filePath, 'utf8');
  
  for (const [eng, ind] of Object.entries(dict)) {
    // Basic string replace with global flag, preserving case as much as possible where exact match exists.
    // We use a regex for exact word boundary match to avoid partial replacements like "Settingss" -> "Pengaturans"
    const regex = new RegExp(`\\b${eng}\\b`, 'g');
    content = content.replace(regex, ind);
    
    // Also handle cases without boundaries for full phrase matches that might contain symbols
    if (eng.includes(' ')) {
      content = content.split(eng).join(ind);
    }
  }
  
  // Additional manual cleanups for leftover AI-ish/generic terms
  content = content.replace(/>\s*Overview\s*</g, '>Ringkasan<');
  content = content.replace(/>\s*Home\s*</g, '>Beranda<');
  content = content.replace(/>\s*Analytics\s*</g, '>Analitik<');
  
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Translated ${file}`);
});
