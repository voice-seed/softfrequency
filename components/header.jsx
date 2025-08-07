'use client';

import Link from 'next/link';

const navItems = [
  { linkText: 'Home', href: '/' },
  { linkText: 'Shop', href: '/shop' },
  { linkText: 'About', href: '/about' },
  { linkText: 'Contact', href: '/contact' }
];

export function Header() {
  return (
    <header className="w-full border-b border-gray-200 pb-6 pt-6 sm:pt-12 md:pb-12">
      <nav className="container mx-auto flex flex-wrap items-center justify-between px-4 sm:px-8">
        <Link
          href="/"
          className="text-2xl font-semibold tracking-tight text-emerald-600 hover:text-emerald-800 transition-colors"
        >
          SoftFrequency
        </Link>

        <ul className="flex flex-wrap gap-x-6 gap-y-2 mt-4 sm:mt-0">
          {navItems.map((item, index) => (
            <li key={index}>
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
