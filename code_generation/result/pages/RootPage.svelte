<script>
  import { route } from '@mateothegreat/svelte5-router';
</script>

<div class="page-container">
  <header class="main-header">
    <div class="header-content">
      <a href="/" use:route class="logo">IMAJI Coffee.</a>
      <nav class="main-nav">
        <ul>
          <li><a href="/" use:route class="active">Home</a></li>
          <li><a href="#story">Story</a></li>
          <li><a href="#menu">Menu</a></li>
          <li><a href="#space">Space</a></li>
          <li><a href="/event_list" use:route>Community</a></li>
          <li><a href="/blog_list" use:route>News</a></li>
        </ul>
      </nav>
      <div class="header-actions">
        <button class="btn btn-primary">Order</button>
        <button class="btn btn-secondary">Sign In</button>
      </div>
    </div>
  </header>

  <main>
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-text">
        <h1>Choose your Coffee & Space</h1>
        <p>IM4JI Coffee has been serving 20,000+ cups of coffee and providing a comfortable place for our customers to work since 2010.</p>
      </div>
      <div class="hero-images">
        <img src="/cafe-ceiling.jpg" alt="Café interior ceiling view" class="hero-img-1">
        <img src="/cafe-plants.jpg" alt="Café interior with hanging plants" class="hero-img-2">
        <img src="/cafe-counter.jpg" alt="Barista serving a customer at the counter" class="hero-img-3">
      </div>
    </section>

    <!-- Provide Space Section -->
    <section class="provide-space-section">
      <div class="provide-space-text">
        <h2>We Provide Your Space For Your Work or Mini event With Your Favorite coffee.</h2>
        <div class="text-columns">
          <p>Our story begins in 2010 with a simple idea from our founder that the most comfortable place to work is anywhere, because ideas are not limited by space and time, and the most comfortable place is in a café where their favorite coffee is available.</p>
          <p>All the best local coffee bean varieties from throughout Indonesia are available with us. Directly from selected farmers, high-quality beans are processed and roasted to perfection by ourselves, then passed on to our skilled baristas who are passionate about preparing a cup of longed-for happiness from home.</p>
        </div>
      </div>
      <div class="provide-space-images">
        <img src="/cafe-table-window.jpg" alt="Coffee table by a window">
        <img src="/cafe-interior-plants.jpg" alt="Spacious cafe interior with plants">
        <img src="/cafe-interior-lounge.jpg" alt="Lounge area in the cafe with blue accents">
        <img src="/coffee-and-cake.jpg" alt="A cup of coffee, a slice of cake, and a cactus on a table">
      </div>
    </section>

    <!-- Favorite Menu Section -->
    <section id="menu" class="favorite-menu-section">
      <div class="section-header">
        <h2>Find Your Favorite Menu</h2>
        <button class="btn btn-primary">Explore Other Menu</button>
      </div>
      <div class="menu-items">
        <div class="menu-item">
          <img src="/blue-drink-cookies.jpg" alt="A blue drink with cookies">
          <h3>RISTRETTO BIANCO</h3>
          <p class="availability">Available Only at Cafe and Delivery</p>
          <p class="price">$5,00</p>
          <p class="discount">Get 20% Off in App</p>
        </div>
        <div class="menu-item">
          <img src="/blue-french-toast.jpg" alt="French toast with powdered sugar">
          <h3>FRENCH TOAST WITH SUGAR</h3>
          <p class="availability">Available Only at Cafe and Delivery</p>
          <p class="price">$5,00</p>
          <p class="discount">Get 20% Off in App</p>
        </div>
        <div class="menu-item">
          <img src="/imaji-coffee-packaging.jpg" alt="IMaji Coffee House Blend packaging">
          <h3>AT HOME HOUSE BLEND</h3>
          <p class="availability">Available Buy at Website</p>
          <p class="price">$5,00</p>
          <p class="discount">Get 20% Off in App</p>
        </div>
      </div>
    </section>

    <!-- Comfy Workspace Section -->
    <section id="space" class="comfy-workspace-section">
      <h2>8 Comfy Workspace</h2>
      <p>We provide many attractive and unique workspaces so you will have no trouble finding the workspace you want.</p>
      <div class="workspace-carousel">
        <div class="workspace-item">
          <img src="/white-wall-workspace.jpg" alt="Workspace with a white brick wall">
          <div class="workspace-label">
            <h4>WHITE WALL</h4>
            <p>Workspace</p>
          </div>
        </div>
        <div class="workspace-item">
          <img src="/long-window-workspace.jpg" alt="Workspace along a long window">
          <div class="workspace-label">
            <h4>LONG WINDOW</h4>
            <p>Workspace</p>
          </div>
        </div>
        <div class="workspace-item">
          <img src="/gengs-space-workspace.jpg" alt="GENGS SPACE workspace area">
          <div class="workspace-label">
            <h4>GENGS SPACE</h4>
            <p>Workspace</p>
          </div>
        </div>
      </div>
      <div class="carousel-dots">
        <span class="dot"></span>
        <span class="dot active"></span>
        <span class="dot"></span>
      </div>
    </section>

    <!-- Customer Growth Section -->
    <section class="customer-growth-section">
        <h2>We Grow Together With Our Customer</h2>
      <div class="growth-content">
        <div class="growth-text">
            <p>We believe that we are big not because of us but because of them. they are the ones who motivate us to continue to innovate to provide a quality coffee taste and comfortable space that is getting better every day.</p>
            <a href="/event_list" use:route class="btn btn-primary">Explore Other Event</a>
        </div>
        <div class="growth-events">
            <div class="event-card">
                <img src="/latte-art-workshop.jpg" alt="Latte art workshop">
                <p>LATTE ART WORKSHOP</p>
                <span>20 Feb 2023</span>
            </div>
            <div class="event-card">
                <img src="/exhibition-coffee-hardware.jpg" alt="Exhibition of coffee hardware">
                <p>EXHIBITION COFFEE HARDWARE</p>
                <span>20 Mar 2023</span>
            </div>
        </div>
      </div>
       <div class="podcast-player">
          <img src="/imaji-coffee-podcast.png" alt="Imaji Coffee Podcast cover art">
          <div class="podcast-info">
            <h4>Mix The Taste of Indonesian Coffee</h4>
            <p>Feb 2023 . 1 hr 18 min</p>
          </div>
          <div class="podcast-controls">
            <button class="control-btn">10s</button>
            <button class="play-btn"></button>
            <button class="control-btn">10s</button>
          </div>
          <div class="podcast-progress">
             <div class="progress-bar">
                 <div class="progress-filled"></div>
             </div>
             <span>00:03/1:13:56</span>
             <svg class="volume-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"></path></svg>
          </div>
          <a href="#other-episodes" class="other-episodes">Other Episode →</a>
       </div>
    </section>

    <!-- Latest News Section -->
    <section class="latest-news-section">
      <div class="section-header">
        <div>
          <h2>Latest News</h2>
          <p>Get the latest updates and deeper coffee experience from IMAJI Coffee</p>
        </div>
        <a href="/blog_list" use:route class="btn btn-primary">See All News</a>
      </div>
      <a href="/blog_detail" use:route class="news-card">
        <img src="/barista-serving-customers.jpg" alt="Barista serving customers in a busy cafe">
        <div class="news-card-content">
          <h3>Collaboration to Develop Coffee and Beverage Industry Expertise in Indonesia</h3>
          <p>4 Min • August 19, 2022</p>
        </div>
      </a>
    </section>
  </main>

  <footer class="main-footer">
    <div class="footer-content">
      <div class="location-info">
        <h3>Our Location</h3>
        <p>Jl. Bangkringan No 19, RT.11/RW.2, Kota Surabaya, 60124</p>
        <p>Customer Service +6282-2876-6862</p>
        <p>We Are Open from Sun - Mon 10 AM - 22 PM</p>
      </div>
      <hr>
      <div class="footer-bottom">
        <div class="social-links">
           <!-- Placeholder SVGs for social media icons -->
            <svg width="24" height="24" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.85s-.011 3.585-.069 4.85c-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07s-3.585-.012-4.85-.07c-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.85s.012-3.584.07-4.85c.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.85-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948s.014 3.667.072 4.947c.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072s3.667-.014 4.947-.072c4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.947s-.014-3.667-.072-4.947c-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.689-.073-4.948-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4s1.791-4 4-4 4 1.79 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.441 1.441 1.441 1.441-.645 1.441-1.441-.645-1.44-1.441-1.44z"/></svg>
            <svg width="24" height="24" viewBox="0 0 24 24"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>
            <!-- Add other icons -->
        </div>
        <div class="legal-and-store">
          <span>Delivery Order</span>
          <img src="/app-store.png" alt="Download on the App Store" class="store-badge">
          <img src="/google-play.png" alt="Get it on Google Play" class="store-badge">
        </div>
      </div>
      <div class="footer-copyright">
        <p>© 2023 IMAJI COFFEE, All rights reserved</p>
        <div class="legal-links">
          <a href="#terms">Terms and Conditions</a> | <a href="#privacy">Privacy Policy</a>
        </div>
      </div>
    </div>
  </footer>
</div>

<style>
  :root {
    --primary-font: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    --color-background: #fdfaf6;
    --color-text: #1a1a1a;
    --color-text-light: #555;
    --color-primary: #a07455;
    --color-primary-dark: #8c6447;
    --color-secondary: #f0ebe5;
    --color-footer-bg: #111111;
    --color-footer-text: #e0e0e0;
    --container-width: 1200px;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: var(--primary-font);
    background-color: var(--color-background);
    color: var(--color-text);
  }

  .page-container {
    max-width: 100%;
    overflow-x: hidden;
  }
  
  h1, h2, h3, h4 {
    font-weight: 500;
  }

  h1 {
    font-size: clamp(3rem, 10vw, 6rem);
    line-height: 1.1;
  }

  h2 {
    font-size: clamp(2rem, 8vw, 4rem);
    line-height: 1.2;
    margin-bottom: 1.5rem;
  }

  h3 {
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
  }

  p {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--color-text-light);
  }
  
  a {
    color: inherit;
    text-decoration: none;
  }

  .btn {
    padding: 0.75rem 1.5rem;
    border: 1px solid transparent;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 500;
    transition: all 0.2s ease-in-out;
  }

  .btn-primary {
    background-color: var(--color-primary);
    color: white;
  }

  .btn-primary:hover {
    background-color: var(--color-primary-dark);
  }

  .btn-secondary {
    background-color: transparent;
    border-color: var(--color-primary);
    color: var(--color-primary);
  }

  .btn-secondary:hover {
    background-color: var(--color-secondary);
  }

  /* Header */
  .main-header {
    background: var(--color-background);
    padding: 1rem 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: 1px solid #eee;
  }

  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: var(--container-width);
    margin: 0 auto;
  }

  .logo {
    font-weight: bold;
    font-size: 1.5rem;
  }

  .main-nav ul {
    display: flex;
    list-style: none;
    gap: 2rem;
  }
  
  .main-nav a.active {
    font-weight: bold;
    border-bottom: 2px solid var(--color-primary);
    padding-bottom: 4px;
  }

  .header-actions {
    display: flex;
    gap: 1rem;
  }

  /* Main sections */
  main > section {
    padding: 4rem 2rem;
    max-width: var(--container-width);
    margin: 0 auto;
  }

  /* Hero Section */
  .hero-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: center;
  }
  .hero-text p {
    margin-top: 1rem;
    max-width: 450px;
  }
  .hero-images {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto auto;
    gap: 1rem;
  }
  .hero-images img { width: 100%; height: auto; object-fit: cover; }
  .hero-img-1 { grid-column: 1 / 3; }

  /* Provide Space Section */
  .provide-space-text h2 { max-width: 800px; }
  .provide-space-text .text-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin-top: 2rem;
  }
  .provide-space-images {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-top: 3rem;
  }
  .provide-space-images img { width: 100%; height: 250px; object-fit: cover; }
  
  /* Favorite Menu Section */
  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }
  .menu-items {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }
  .menu-item img {
    width: 100%;
    margin-bottom: 1rem;
  }
  .menu-item .availability { font-size: 0.9rem; color: #777; }
  .menu-item .price { font-size: 1.2rem; font-weight: bold; color: var(--color-text); margin: 0.5rem 0; }
  .menu-item .discount { color: var(--color-primary); font-weight: 500; font-size: 0.9rem;}

  /* Comfy Workspace */
  .workspace-carousel {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin-top: 2rem;
  }
  .workspace-item {
    position: relative;
  }
  .workspace-item img { width: 100%; display: block; }
  .workspace-label {
    position: absolute;
    top: 1rem;
    left: 1rem;
    background: rgba(255, 255, 255, 0.8);
    padding: 0.5rem 1rem;
  }
  .workspace-label h4 { font-size: 1.1rem; }
  .workspace-label p { font-size: 0.8rem; color: var(--color-text-light); }
  .carousel-dots { text-align: center; margin-top: 2rem; }
  .dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #ccc; margin: 0 5px; }
  .dot.active { background: var(--color-primary); }

  /* Customer Growth Section */
  .customer-growth-section { background: var(--color-secondary); }
  .growth-content {
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 3rem;
      align-items: flex-start;
  }
  .growth-text .btn { margin-top: 1.5rem; }
  .growth-events {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
  }
  .event-card img { width: 100%; }
  .event-card p { font-weight: bold; color: var(--color-text); margin-top: 0.5rem; }
  .event-card span { font-size: 0.9rem; color: #777; }
  
  .podcast-player {
    display: grid;
    grid-template-columns: auto 1fr auto auto auto;
    align-items: center;
    gap: 1rem;
    background-color: var(--color-primary);
    color: white;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 3rem;
  }
  .podcast-player img { width: 80px; height: 80px; }
  .podcast-info h4 { font-size: 1.2rem; }
  .podcast-info p { font-size: 0.9rem; color: var(--color-secondary); }
  .podcast-controls { display: flex; align-items: center; gap: 0.5rem; }
  .play-btn { width: 40px; height: 40px; border-radius: 50%; border: 2px solid white; background: transparent; }
  .podcast-progress { display: flex; align-items: center; gap: 0.5rem; width: 100%; }
  .progress-bar { flex-grow: 1; height: 4px; background: rgba(255,255,255,0.3); }
  .other-episodes { font-weight: bold; }
  .volume-icon { fill: white; width: 20px; height: 20px; }

  /* Latest News */
  .latest-news-section .section-header p {
      max-width: 400px;
  }
  .news-card {
      display: block;
      margin-top: 2rem;
  }
  .news-card img {
      width: 100%;
      height: 400px;
      object-fit: cover;
      margin-bottom: 1rem;
  }
  .news-card-content h3 { font-size: 1.5rem; }
  .news-card-content p { margin-top: 0.5rem; }

  /* Footer */
  .main-footer {
    background: var(--color-footer-bg);
    color: var(--color-footer-text);
    padding: 4rem 2rem;
  }
  .footer-content {
    max-width: var(--container-width);
    margin: 0 auto;
  }
  .location-info h3 { margin-bottom: 1rem; font-size: 2rem;}
  .location-info p { color: var(--color-footer-text); }
  .main-footer hr { border-color: #444; margin: 2rem 0; }
  .footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .social-links { display: flex; gap: 1rem; }
  .social-links svg { fill: white; }
  .legal-and-store { display: flex; align-items: center; gap: 1rem; }
  .store-badge { height: 40px; }
  .footer-copyright {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
    font-size: 0.9rem;
    color: #aaa;
  }
  
  /* --- Media Queries (Mobile First) --- */

  /* Tablet (e.g., screens >= 768px) */
  @media (max-width: 1024px) {
    .main-nav { display: none; } /* Simplified nav for smaller screens */
    .provide-space-images { grid-template-columns: 1fr 1fr; }
    .workspace-carousel { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
    .growth-content { grid-template-columns: 1fr; }
  }

  /* Mobile (e.g., screens < 768px) */
  @media (max-width: 767px) {
    h1 { font-size: 2.5rem; }
    h2 { font-size: 1.8rem; }
    main > section { padding: 3rem 1rem; }

    .header-content { flex-wrap: wrap; }
    .header-actions {
        order: 3;
        width: 100%;
        margin-top: 1rem;
        justify-content: flex-end;
    }

    .hero-section { grid-template-columns: 1fr; }
    .provide-space-text .text-columns { grid-template-columns: 1fr; }
    .provide-space-images { grid-template-columns: 1fr; }
    
    .section-header { flex-direction: column; align-items: flex-start; gap: 1rem; }
    .menu-items { grid-template-columns: 1fr; }

    .growth-events { grid-template-columns: 1fr; }
    
    .podcast-player { 
        grid-template-columns: 1fr;
        text-align: center;
    }
    .podcast-player img { margin: 0 auto; }
    .podcast-progress { flex-wrap: wrap; justify-content: center; }
    
    .footer-bottom, .footer-copyright {
        flex-direction: column;
        gap: 1.5rem;
        text-align: center;
    }
  }

</style>