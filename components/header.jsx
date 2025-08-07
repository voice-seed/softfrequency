'use client';

import Link from 'next/link';

const navItems = [
  { linkText: 'Home', href: '/' },
  { linkText: 'Shop', href: '/shop' },
  { linkText: 'Blog', href: '/blog' },
  { linkText: 'Rituals', href: '/rituals' },
  { linkText: 'Community', href: '/community' },
  { linkText: 'About', href: '/about' },
  { linkText: 'Contact', href: '/contact' }
];

export function Header() {
  return (
    <header className="w-full border-b border-gray-200 bg-white/90 backdrop-blur-md sticky top-0 z-50">
      <nav className="max-w-7xl mx-auto flex flex-wrap items-center justify-between px-4 py-4 sm:px-8 sm:py-6">
        <Link
          href="/"
          className="text-3xl font-bold tracking-tight text-emerald-700 hover:text-emerald-900 transition-colors"
        >
          Soft<span className="text-gray-500">Frequency</span>
        </Link>

        <ul className="flex flex-wrap items-center justify-end gap-x-5 gap-y-2 text-sm sm:text-base">
          {navItems.map((item) => (
            <li key={item.href}>
              <Link
                href={item.href}
                className="text-gray-700 hover:text-emerald-600 transition-colors px-2 py-1"
              >
                {item.linkText}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
}
