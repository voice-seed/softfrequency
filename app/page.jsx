export const metadata = {
  title: "SoftFrequency | Ambient Wellness Technology",
  description: "Discover solar lanterns, smart diffusers, and ambient tools for a soft, resonant future.",
};

export default function Home() {
  return (
    <main style={{
      fontFamily: 'Inter, sans-serif',
      backgroundColor: '#f3f7f5',
      padding: '4rem 2rem',
      color: '#1a1a1a',
      lineHeight: '1.7',
      maxWidth: '1000px',
      margin: '0 auto'
    }}>
      
      {/* 🌿 Hero Section */}
      <section style={{ marginBottom: '4rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '3rem', marginBottom: '1rem' }}>🌿 SoftFrequency</h1>
        <p style={{ fontSize: '1.3rem', color: '#444' }}>
          Ambient products. Natural tech. A future that breathes.
        </p>
        <p style={{ fontStyle: 'italic', color: '#666' }}>
          From solar lanterns to smart diffusers — this is a space for resonance.
        </p>
      </section>

      {/* 🧘‍♀️ About the Mission */}
      <section style={{ marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '2rem' }}>🧘‍♀️ Why SoftFrequency?</h2>
        <p>
          Because modern life is too sharp. Too fast. Too loud. <br />
          SoftFrequency is the answer — a new wave of sustainable, ambient tech designed to
          bring presence, softness, and energy alignment back into your space.
        </p>
      </section>

      {/* 🛒 Featured Products */}
      <section style={{ marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '2rem' }}>🛒 Featured Ritual Tools</h2>
        <ul style={{ listStyle: 'none', padding: 0, marginTop: '1rem' }}>
          <li style={{ marginBottom: '1rem' }}>
            🔥 <strong>Solar Flame Lantern:</strong> Real firelight powered by the sun. Cozy, primal, pure.
          </li>
          <li style={{ marginBottom: '1rem' }}>
            🌬️ <strong>Smart Diffuser:</strong> Controlled by your voice. Aromatherapy, aligned with AI.
          </li>
          <li style={{ marginBottom: '1rem' }}>
            💡 <strong>Glow Cubes:</strong> Minimalist soft light blocks for mindful moments.
          </li>
        </ul>
      </section>

      {/* 🌀 Community Call */}
      <section style={{ marginBottom: '4rem', color: '#555' }}>
        <h2 style={{ fontSize: '2rem' }}>🌀 Join the Resonance</h2>
        <p>
          We’re building more than a store — we’re building a movement. <br />
          Telegram, WhatsApp, Reddit. Decentralized, conscious community.
        </p>
        <p style={{ marginTop: '1rem', fontStyle: 'italic' }}>
          🔮 Coming soon: voice rituals, eco challenges, ambient drops, and group frequency shifts.
        </p>
      </section>

      {/* © Footer */}
      <footer style={{
        borderTop: '1px solid #ddd',
        paddingTop: '2rem',
        fontSize: '0.9rem',
        textAlign: 'center',
        color: '#888'
      }}>
        <p>© 2025 SoftFrequency – A soft place for sharp minds.</p>
        <p>Hand-built with ambient code, solar power, and vision.</p>
      </footer>

    </main>
  );
}
