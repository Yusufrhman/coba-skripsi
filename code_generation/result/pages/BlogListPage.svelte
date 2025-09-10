<script>
  import { route } from '@mateothegreat/svelte5-router';

  let menuOpen = false;

  const articles = [
    {
      id: 1,
      title: 'Collaboration to Develop Coffee and Beverage Industry Expertise in Indonesia',
      date: 'August 19, 2022',
      readTime: '4 Min',
      image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png', // Large image of a coffee shop interior
      featured: true,
    },
    {
      id: 2,
      title: 'Visited Doesoen Sirap Coffee, The Producer of Robusta in Central Java',
      date: 'August 19, 2022',
      readTime: '4 Min',
      image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png', // Image of coffee beans being dispensed
      featured: false,
    },
    {
      id: 3,
      title: 'Cold Brew Coffee, How to Drink Cold Coffee is More Enjoyable',
      date: 'August 19, 2022',
      readTime: '4 Min',
      image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png', // Hand pouring liquid into cup
      featured: false,
    },
    {
      id: 4,
      title: 'Meet Coffee Tonic, the Sensation of Drinking Coffee-Flavored Soda',
      date: 'August 19, 2022',
      readTime: '4 Min',
      image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png', // Image of beverage being poured into a small cup
      featured: false,
    },
    {
      id: 5,
      title: 'Workshop Coffee Sharing Session',
      date: 'August 19, 2022',
      readTime: '4 Min',
      image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png', // Barista pouring coffee into pour-over
      featured: false,
    },
    {
      id: 6,
      title: 'Workshop Coffee Brewing',
      date: 'August 19, 2022',
      readTime: '4 Min',
      image: 'https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png', // Image of a person pouring from a kettle into a pour-over coffee setup
      featured: false,
    },
  ];

  const featuredArticle = articles[0];
  const otherArticles = articles.slice(1);

  function handleLoadMore() {
    // In a real app, this would fetch more articles from an API.
    console.log('Loading more articles...');
  }

  function toggleMenu() {
    menuOpen = !menuOpen;
  }
</script>

<div class="page-container">
  <!-- Header -->
  <header class="header">
    <div class="header-content">
      <a href="/" use:route class="logo">IMAJI Coffee.</a>
      <nav class="desktop-nav">
        <a href="/" use:route>Home</a>
        <a href="/story" use:route>Story</a>
        <a href="/menu" use:route>Menu</a>
        <a href="/space" use:route>Space</a>
        <a href="/event_list" use:route>Community</a>
        <a href="/blog_list" use:route class="active">News</a>
      </nav>
      <div class="header-actions">
        <button class="order-btn">Order</button>
        <button class="signin-btn">Sign In</button>
      </div>
      <button class="hamburger-btn" on:click={toggleMenu}>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
    {#if menuOpen}
      <nav class="mobile-nav">
        <a href="/" use:route>Home</a>
        <a href="/story" use:route>Story</a>
        <a href="/menu" use:route>Menu</a>
        <a href="/space" use:route>Space</a>
        <a href="/event_list" use:route>Community</a>
        <a href="/blog_list" use:route class="active">News</a>
        <button class="order-btn-mobile">Order</button>
        <button class="signin-btn-mobile">Sign In</button>
      </nav>
    {/if}
  </header>

  <!-- Main Content -->
  <main class="main-content">
    <div class="news-header">
      <h1>Our News</h1>
      <p>Get the latest updates and deeper coffee experience from IMAJI Coffee</p>
    </div>

    <!-- Featured Article -->
    <a href="/blog_detail" use:route class="featured-article-link">
      <article class="featured-article">
        <img src={featuredArticle.image} alt="Large image of a coffee shop interior with baristas and customers">
        <div class="article-text">
          <h2>{featuredArticle.title}</h2>
          <p class="article-meta">{featuredArticle.readTime} • {featuredArticle.date}</p>
        </div>
      </article>
    </a>

    <!-- Articles List -->
    <div class="articles-list">
      {#each otherArticles as article (article.id)}
        <a href="/blog_detail" use:route class="article-link">
          <article class="article-item">
            <img src={article.image} alt={article.title} class="article-image">
            <div class="article-text">
              <h3>{article.title}</h3>
              <p class="article-meta">{article.readTime} • {article.date}</p>
            </div>
          </article>
        </a>
      {/each}
    </div>

    <div class="load-more-container">
      <button class="load-more-btn" on:click={handleLoadMore}>Load More</button>
    </div>

  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-content">
      <div class="location-section">
        <h2>Our Location</h2>
        <p>Jl. Bangkringan No 19, RT.11/RW.2, Kota Surabaya, 60124</p>
        <p>Customer Service +6282-2876-6862</p>
        <p>We Are Open from Sun - Mon 10 AM - 22 PM</p>
      </div>

      <div class="footer-bottom">
         <div class="social-links">
            <!-- Icons would be SVGs or icon font in a real app -->
            <a href="#"><img src="/instagram-icon.png" alt="Instagram"></a>
            <a href="#"><img src="/tiktok-icon.png" alt="TikTok icon"></a>
            <a href="#"><img src="/youtube-icon.png" alt="Youtube"></a>
            <a href="#"><img src="/twitter-icon.png" alt="Twitter"></a>
            <a href="#" aria-label="Paper airplane icon"><img src="/telegram-icon.png" alt="Paper airplane icon"></a>
         </div>
         <div class="app-links-wrapper">
            <button class="delivery-order-btn">Delivery Order</button>
            <div class="app-links">
                <a href="#"><img src="/app-store-badge.png" alt="Download on the App Store button/logo"></a>
                <a href="#"><img src="/google-play-badge.png" alt="Google Play button/logo"></a>
            </div>
        </div>
      </div>
      
      <div class="footer-legal">
        <p>© 2023 IMAJI COFFEE, All rights reserved</p>
        <div class="legal-links">
          <a href="#">Terms and Conditions</a>
          <span>|</span>
          <a href="#">Privacy Policy</a>
        </div>
      </div>
    </div>
  </footer>
</div>

<style>
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: #F9F5F0; /* Light beige background */
    color: #333;
  }

  .page-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  /* Header Styles */
  .header {
    background-color: #F9F5F0;
    padding: 1rem 2rem;
    border-bottom: 1px solid #e5e5e5;
    position: sticky;
    top: 0;
    z-index: 10;
  }

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: #5D4037; /* Brown color for logo */
    text-decoration: none;
  }

  .desktop-nav {
    display: none; /* Hidden on mobile by default */
    gap: 2rem;
  }

  .desktop-nav a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
  }
   .desktop-nav a.active {
    color: #5D4037;
    font-weight: bold;
  }

  .header-actions {
    display: none; /* Hidden on mobile by default */
    gap: 1rem;
  }
  
  .order-btn {
    background-color: #A1887F; /* Muted brown */
    color: white;
    border: none;
    padding: 0.5rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
  }

  .signin-btn {
    background-color: transparent;
    color: #5D4037;
    border: 1px solid #5D4037;
    padding: 0.5rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
  }

  .hamburger-btn {
    background: none;
    border: none;
    cursor: pointer;
    display: block; /* Shown on mobile */
  }
  
  .mobile-nav {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
    text-align: center;
  }
  
  .mobile-nav a {
    text-decoration: none;
    color: #333;
    padding: 0.5rem;
  }
   .mobile-nav a.active {
    color: #5D4037;
    font-weight: bold;
  }

  .order-btn-mobile, .signin-btn-mobile {
      margin: 0.5rem auto;
      width: 80%;
      padding: 0.75rem;
      border-radius: 4px;
      font-weight: bold;
  }
  .order-btn-mobile {
      background-color: #A1887F;
      color: white;
      border: none;
  }
  .signin-btn-mobile {
      background-color: transparent;
      color: #5D4037;
      border: 1px solid #5D4037;
  }


  /* Main Content Styles */
  .main-content {
    flex-grow: 1;
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 1rem;
    width: 100%;
    box-sizing: border-box;
  }
  
  .news-header {
    text-align: center;
    margin-bottom: 3rem;
  }

  .news-header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    font-weight: bold;
  }

  .news-header p {
    font-size: 1.1rem;
    color: #666;
  }

  .featured-article-link, .article-link {
    text-decoration: none;
    color: inherit;
    display: block;
    margin-bottom: 2rem;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 2rem;
  }
  
  .featured-article img {
    width: 100%;
    height: auto;
    object-fit: cover;
    margin-bottom: 1rem;
  }

  .featured-article h2 {
    font-size: 2rem;
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: 0.5rem;
  }

  .article-meta {
    color: #888;
    font-size: 0.9rem;
  }
  
  .articles-list {
    display: flex;
    flex-direction: column;
  }

  .article-item {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    align-items: flex-start;
  }

  .article-image {
    width: 100%;
    height: auto;
    object-fit: cover;
  }

  .article-item h3 {
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.4;
    margin: 0 0 0.5rem 0;
  }

  .load-more-container {
    text-align: center;
    margin-top: 1rem;
  }

  .load-more-btn {
    background-color: transparent;
    color: #5D4037;
    border: 1px solid #5D4037;
    padding: 0.75rem 2rem;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
    font-size: 1rem;
  }

  /* Footer Styles */
  .footer {
    background-color: #1a1a1a;
    color: white;
    padding: 3rem 1rem;
  }
  
  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
  
  .location-section h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  .location-section p {
    margin: 0.5rem 0;
    line-height: 1.6;
    color: #ccc;
  }

  .footer-bottom {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    border-top: 1px solid #444;
    padding-top: 2rem;
  }
  
  .social-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    justify-content: center;
  }
  
  .social-links img {
    width: 24px;
    height: 24px;
    filter: invert(1);
  }

  .app-links-wrapper {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      align-items: center;
  }
  
  .delivery-order-btn {
      background: none;
      border: 1px solid white;
      color: white;
      padding: 0.5rem 1.5rem;
      border-radius: 4px;
      font-size: 1rem;
  }

  .app-links {
    display: flex;
    gap: 1rem;
    align-items: center;
  }

  .app-links img {
    height: 40px;
  }

  .footer-legal {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    text-align: center;
    color: #aaa;
    font-size: 0.9rem;
    border-top: 1px solid #444;
    padding-top: 2rem;
  }
  
  .legal-links {
    display: flex;
    gap: 0.5rem;
  }
  
  .legal-links a {
    color: #aaa;
    text-decoration: none;
  }
  .legal-links span {
    margin: 0 0.5rem;
  }


  /* --- Breakpoints for Responsiveness --- */

  /* Tablet (md) */
  @media (min-width: 768px) {
    .header-content {
      padding: 1rem 0;
    }
    .desktop-nav, .header-actions {
      display: flex;
    }
    .hamburger-btn, .mobile-nav {
      display: none;
    }
    
    .news-header h1 {
        font-size: 4rem;
    }

    .article-item {
      flex-direction: row;
      align-items: center;
    }

    .article-image {
      width: 200px;
      height: 130px;
      flex-shrink: 0;
    }

    .footer-bottom {
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
    }
    
    .social-links, .app-links-wrapper {
      justify-content: flex-start;
    }

    .app-links-wrapper {
        flex-direction: row;
    }

    .footer-legal {
        flex-direction: row;
        justify-content: space-between;
    }
  }

  /* Desktop (lg) */
  @media (min-width: 1024px) {
     .main-content {
        padding: 4rem 2rem;
     }

     .featured-article h2 {
        font-size: 2.5rem;
     }
  }

</style>