import '../styles/globals.css';
import { Header } from '../components/header';

export const metadata = {
  title: {
    template: '%s | SoftFrequency',
    default: 'SoftFrequency – Ambient Tech for Resonant Living',
  },
  description: 'Explore solar lanterns, AI-powered diffusers, and ambient tools for modern sanctuary seekers.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.svg" sizes="any" />
      </head>
      <body className="antialiased text-gray-900 bg-[#f3f7f5]">
        <div className="flex flex-col min-h-screen px-6 sm:px-12">
          <div className="flex flex-col w-full max-w-5xl mx-auto grow">
            <Header />
            <main className="grow py-10">{children}</main>
            {/* Footer removed */}
          </div>
        </div>
      </body>
    </html>
  );
}
