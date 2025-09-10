<script>
  import { route } from '@mateothegreat/svelte5-router';

  // Data based on PTG props for event_list page
  let upcomingEvents = [
    { title: 'LATTE ART WORKSHOP', date: '24 JAN 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
    { title: 'EXHIBITION COFFEE HARDWARE', date: '20 MAR 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
    { title: 'FACTORY VISIT', date: '20 APR 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' }
  ];

  let initialClosedEvents = [
    { title: 'BEZZERA LATTE ART COMPETITION', date: '20 FEB 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
    { title: 'SENSORY AND CUPPING CLASS', date: '20 MAR 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
    { title: 'PUBLIC CUPPING', date: '20 FEB 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
    { title: 'COMPETITIONS AND SHOWCASES', date: '20 MAR 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
    { title: 'ART AND COFFEE FESTIVAL', date: '20 MAR 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' }
  ];

  let closedEvents = [...initialClosedEvents];
  let showLoadMore = true;

  // Handles the 'Load More' button click to add more closed events
  function loadMoreEvents() {
    const moreEvents = [
        { title: 'LATTE ART WORKSHOP', date: '20 FEB 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' },
        { title: 'PUBLIC CUPPING', date: '24 JAN 2023', image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png' }
    ];
    closedEvents = [...closedEvents, ...moreEvents];
    showLoadMore = false; // Hides the button after loading once
  }

  let isMobileMenuOpen = false;

  function toggleMobileMenu() {
    isMobileMenuOpen = !isMobileMenuOpen;
  }
</script>

<div class="page-container">
  <!-- Header -->
  <header class="header">
    <div class="header-content">
      <a href="/" use:route class="logo">IMAJI Coffee.</a>
      <nav class="desktop-nav">
        <ul>
          <li><a href="/" use:route>Home</a></li>
          <li><a href="/story" use:route>Story</a></li>
          <li><a href="/menu" use:route>Menu</a></li>
          <li><a href="/space" use:route>Space</a></li>
          <li><a href="/event_list" use:route class="active">Community</a></li>
          <li><a href="/blog_list" use:route>News</a></li>
        </ul>
      </nav>
      <div class="header-actions">
        <button class="order-btn">Order</button>
        <button class="signin-btn">Sign In</button>
      </div>
      <button class="mobile-menu-btn" on:click={toggleMobileMenu} aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
    {#if isMobileMenuOpen}
      <nav class="mobile-nav">
        <ul>
          <li><a href="/" use:route>Home</a></li>
          <li><a href="/story" use:route>Story</a></li>
          <li><a href="/menu" use:route>Menu</a></li>
          <li><a href="/space" use:route>Space</a></li>
          <li><a href="/event_list" use:route class="active">Community</a></li>
          <li><a href="/blog_list" use:route>News</a></li>
        </ul>
      </nav>
    {/if}
  </header>

  <!-- Main Content -->
  <main>
    <section class="hero-section">
      <div class="hero-text">
        <h1 class="page-title">Our Upcoming Events</h1>
        <p class="page-description">
          We believe that we are big not because of us but because of them. they are the ones who motivate us to continue to innovate to provide a quality coffee taste and comfortable space that is getting better every day.
        </p>
      </div>
    </section>

    <section class="events-grid upcoming-events">
      {#each upcomingEvents as event (event.title + event.date)}
        <div class="event-card">
          <img src={event.image} alt={event.title} class="event-image"/>
          <div class="event-info">
            <h3 class="event-title">{event.title}</h3>
            <p class="event-date">{event.date}</p>
          </div>
        </div>
      {/each}
    </section>

    <section class="closed-events-section">
      <h2 class="section-title">Events Closed</h2>
      <div class="events-grid">
        {#each closedEvents as event (event.title + event.date)}
          <div class="event-card">
            <img src={event.image} alt={event.title} class="event-image"/>
            <div class="event-info">
              <h3 class="event-title">{event.title}</h3>
              <p class="event-date">{event.date}</p>
            </div>
          </div>
        {/each}
      </div>
      {#if showLoadMore}
        <button class="load-more-btn" on:click={loadMoreEvents}>Load More</button>
      {/if}
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-content">
      <div class="location-info">
        <h2>Our Location</h2>
        <div class="address-block">
          <p>Jl. Bangkrington No 19, RT.11/RW.2, Kota Surabaya, 60124</p>
          <p><strong>Customer Service</strong> +6282 - 2876 - 6862</p>
          <p><strong>We Are Open from</strong> Sun - Mon 10 AM - 22 PM</p>
        </div>
      </div>
      
      <div class="social-and-apps">
        <div class="social-icons">
          <a href="#" aria-label="Spotify">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
          </a>
          <a href="#" aria-label="Instagram">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          </a>
          <a href="#" aria-label="TikTok">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h-2a4 4 0 0 0-4 4v10a4 4 0 0 0 4 4h2"/><path d="M12 14v-4a4 4 0 0 0-4-4H4"/><circle cx="12" cy="12" r="2"/></svg>
          </a>
          <a href="#" aria-label="YouTube">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>
          </a>
          <a href="#" aria-label="Twitter">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"/></svg>
          </a>
          <a href="#" aria-label="Telegram">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="m22 2-7 20-4-9-9-4 20-7z"/></svg>
          </a>
        </div>
        <div class="footer-actions">
           <button class="delivery-btn">Delivery Order</button>
           <div class="app-links">
             <a href="#" class="app-store-btn"><img src="/app-store.png" alt="Download on the App Store"></a>
             <a href="#" class="google-play-btn"><img src="/google-play.png" alt="Get it on Google Play"></a>
           </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="copyright">© 2023 IMAJI COFFEE, All rights reserved</p>
      <div class="legal-links">
        <a href="#">Terms and Conditions</a>
        <a href="#">Privacy Policy</a>
      </div>
    </div>
  </footer>
</div>

<style>
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: #ffffff;
    color: #1a1a1a;
  }

  .page-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  main {
    flex-grow: 1;
    padding: 2rem 5%;
    max-width: 1400px;
    width: 90%;
    margin: 0 auto;
  }

  /* Header Styles */
  .header {
    padding: 1rem 5%;
    background-color: #fff;
    border-bottom: 1px solid #eee;
  }
  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
  }
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
    color: #333;
  }
  .desktop-nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin: 0;
    padding: 0;
  }
  .desktop-nav a {
    text-decoration: none;
    color: #555;
    font-weight: 500;
    padding-bottom: 0.5rem;
  }
  .desktop-nav a:hover, .desktop-nav a.active {
    color: #000;
    border-bottom: 2px solid #a37d5c;
  }
  .header-actions {
    display: flex;
    gap: 1rem;
  }
  .order-btn, .signin-btn {
    padding: 0.75rem 1.5rem;
    border: 1px solid #ccc;
    background-color: #fff;
    cursor: pointer;
    font-size: 1rem;
    transition: all 0.2s ease-in-out;
  }
  .order-btn {
    background-color: #a37d5c;
    color: white;
    border-color: #a37d5c;
  }
   .order-btn:hover {
    background-color: #8c6a4d;
   }
  .signin-btn:hover {
    background-color: #f0f0f0;
  }
  .mobile-menu-btn { display: none; }
  .mobile-nav { display: none; }

  /* Hero Section */
  .hero-section {
    margin: 2rem auto 4rem auto;
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
    align-items: flex-start;
  }
  .page-title {
    font-size: clamp(2.5rem, 8vw, 4rem);
    font-weight: 800;
    margin: 0 0 1rem 0;
    line-height: 1.1;
  }
  .page-description {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #555;
    max-width: 500px;
  }
  
  /* Events Grid */
  .section-title {
    font-size: clamp(2rem, 6vw, 2.5rem);
    font-weight: 700;
    margin-top: 4rem;
    margin-bottom: 2rem;
    text-align: left;
  }
  .events-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .event-card {
    background: #fff;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    overflow: hidden;
  }
  .event-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  }
  .event-image {
    width: 100%;
    height: 250px;
    object-fit: cover;
    display: block;
  }
  .event-info {
    padding: 1.5rem;
    background-color: #f9f9f9;
  }
  .event-title {
    font-size: 1.2rem;
    margin: 0 0 0.5rem 0;
    font-weight: 600;
    color: #111;
  }
  .event-date {
    color: #777;
    margin: 0;
  }
  .closed-events-section {
    text-align: center;
  }
  .load-more-btn {
    margin-top: 3rem;
    padding: 0.75rem 2.5rem;
    font-size: 1rem;
    cursor: pointer;
    background-color: #fff;
    border: 1px solid #333;
    color: #333;
    transition: background-color 0.2s, color 0.2s;
  }
  .load-more-btn:hover {
    background-color: #333;
    color: #fff;
  }

  /* Footer Styles */
  .footer {
    background-color: #111;
    color: #ccc;
    padding: 4rem 5% 2rem;
    margin-top: 4rem;
  }
  .footer-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 3rem;
    max-width: 1400px;
    margin: 0 auto;
    padding-bottom: 2rem;
    border-bottom: 1px solid #444;
  }
  .location-info h2 {
    font-size: 2.5rem;
    color: white;
    margin-bottom: 1.5rem;
  }
  .address-block p { margin: 0.5rem 0; line-height: 1.6; }
  .address-block strong { color: #fff; }
  .social-icons { display: flex; gap: 1rem; margin-bottom: 2rem; }
  .social-icons a { color: #fff; }
  .footer-actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
  .delivery-btn { background: none; border: 1px solid #ccc; color: #ccc; padding: 0.75rem 1.5rem; cursor: pointer; }
  .app-links { display: flex; gap: 1rem; }
  .app-links img { height: 40px; }
  .footer-bottom { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem; padding-top: 2rem; max-width: 1400px; margin: 0 auto; }
  .copyright { color: #888; }
  .legal-links { display: flex; gap: 1.5rem; }
  .legal-links a { color: #888; text-decoration: none; }

  /* --- Responsive Design (Mobile-First) --- */

  /* Tablet Styles (Breakpoint: 640px) */
  @media (min-width: 640px) {
    .events-grid {
      grid-template-columns: repeat(2, 1fr);
    }
    .hero-section {
      grid-template-columns: 1fr 1fr;
    }
  }

  /* Desktop Styles (Breakpoint: 1024px) */
  @media (min-width: 1024px) {
    .events-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  /* Mobile Navigation Styles (Breakpoint: 768px) */
  @media (max-width: 768px) {
    .desktop-nav, .header-actions {
      display: none;
    }
    .mobile-menu-btn {
      display: flex;
      flex-direction: column;
      gap: 5px;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
    }
    .mobile-menu-btn span {
      display: block;
      width: 25px;
      height: 3px;
      background-color: #333;
    }
    .mobile-nav {
      display: block;
      width: 100%;
      background-color: #fff;
      text-align: center;
      padding-top: 1rem;
    }
    .mobile-nav ul { list-style: none; padding: 0; margin: 0; }
    .mobile-nav li { padding: 1rem 0; border-top: 1px solid #eee; }
    .mobile-nav a { text-decoration: none; color: #333; font-size: 1.2rem; }

    .footer-content { flex-direction: column; }
    .footer-bottom { flex-direction: column; align-items: flex-start; }
  }
</style>