<script>
  import { route } from '@mateothegreat/svelte5-router';

  const placeholderImg = "https://artistintelligence.org/wp-content/uploads/2015/08/import_placeholder.png";
</script>

<div class="page-container">
  <header>
    <a href="/" use:route class="logo-link">IMAJI Coffee.</a>
    <nav class="desktop-nav">
      <a href="/" use:route>Home</a>
      <a href="#" use:route>Story</a>
      <a href="#" use:route>Menu</a>
      <a href="#" use:route>Space</a>
      <a href="/event_list" use:route>Community</a>
      <a href="/blog_list" use:route>News</a>
    </nav>
    <div class="header-actions">
      <button class="order-button">Order</button>
      <button class="signin-button">Sign In</button>
    </div>
  </header>

  <main>
    <article>
      <h1 class="article-title">Realizing The Mission of Global Expansion, Open its First Cafe in Singapore</h1>
      <p class="article-meta">August 19, 2022</p>
      <img src={placeholderImg} alt="Cafe interior image with menu on the left" class="main-image" />
      <div class="article-content">
        <p>We are a small cafe, with a big dream of becoming a global cafe. We started our operations in Singapore, and we are now expanding to Singapore. We will be opening our first cafe in Beijing soon, and we also plan to open more cafes across the globe. Realizing The Mission of Global Expansion, Open its First Cafe in Singapore</p>
        <p>We are currently running our first pop-up shop at Dempsey Hill which will run until mid-November. Global Expansion Cafe will be open for lunch and dinner on weekdays as well as weekends. Global Expansion Cafe will introduce new tastes and experiences to Singaporeans by introducing international food culture.</p>
        <p>We are currently running our pop-up shop in Singapore, and hope to launch our own café soon. A real estate company is established in Asia that develops communities and provides financial services globally. We believe in love and happiness, a sense of belonging, and the importance of a shared experience. Here you can be yourself, share stories and make friends.</p>
        <p>We partner with companies who LOVE the world. The cafe is a place where people can go to enjoy the food and coffee, but also a place where they can meet new friends. The cafe is located in Pasir Ris. The cafe has a wide variety of menu items to choose from. In addition to the usual coffee and tea, there are also some specialty drinks such as smoothies, milkshakes and frozen yogurt.</p>
        <p>There are many types of food available at the cafe such as sandwiches, soups, salads and desserts. The menu also includes vegetarian options for those who have special dietary needs. People can order their food online via the website or by calling the number given on the website. They will be able to choose their preferred time for pickup so that they don’t miss out on any orders!</p>
      </div>
    </article>

    <section class="other-news-section">
      <h2 class="section-title">Other News</h2>
      <div class="news-grid">
        <div class="news-card-wrapper">
          <a href="/blog_detail" use:route class="news-card-link">
            <img src={placeholderImg} alt="Cafe interior image" class="news-card-image" />
            <h3 class="news-card-title">Collaboration to Develop Coffee and Beverage Industry Expertise in Indonesia</h3>
            <p class="news-card-meta">4 Min • August 19, 2022</p>
          </a>
        </div>
        <div class="news-card-wrapper">
          <a href="/blog_detail" use:route class="news-card-link">
            <img src={placeholderImg} alt="Cafe interior image" class="news-card-image" />
            <h3 class="news-card-title">Collaboration to Develop Coffee and Beverage Industry</h3>
            <p class="news-card-meta">4 Min • August 19, 2022</p>
          </a>
        </div>
      </div>
      <div class="pagination-dots">
        <span class="dot"></span>
        <span class="dot active"></span>
        <span class="dot"></span>
      </div>
    </section>
  </main>

  <footer>
    <div class="footer-container">
      <div class="footer-top">
        <h2 class="footer-heading">Our Location</h2>
        <p>Jl. Bangkaringan No 19, RT.11/RW.2, Kota Surabaya, 60124</p>
        <p>Customer Service +6282-2876-6862</p>
        <p>We Are Open from Sun - Mon 10 AM - 22 PM</p>
      </div>
      <div class="social-icons">
        <a href="#">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
        </a>
        <a href="#">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
        </a>
        <a href="#">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 1.4 3.3 4.9 3.3 9.7C23.3 22 18 24 12 24c-6 0-11.3-2-11.3-7.3 0-4.8 1.7-8.3 3.3-9.7-1.3-1.3-2-3.4-2-3.4s.7-1 .7-1 1.4 1.3 2.8 2.8c2.1-.6 4.4-.6 6.5 0C16.8 6.3 18.2 5 18.2 5s.7 1 .7 1z"/></svg>
        </a>
        <a href="#">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>
        </a>
        <a href="#">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4.01c-1 .49-1.98.689-3 .99-1.121-1.265-2.716-2.011-4.467-2.011-3.371 0-6.103 2.732-6.103 6.102 0 .482.055.952.16 1.405-5.073-.254-9.571-2.688-12.583-6.384-.525.898-.824 1.945-.824 3.049 0 2.116 1.077 3.985 2.712 5.088-.998-.03-1.938-.304-2.766-.764v.077c0 2.955 2.104 5.419 4.898 5.979-.512.139-1.05.214-1.604.214-.393 0-.775-.038-1.15-.114.777 2.422 3.031 4.183 5.703 4.232-2.089 1.637-4.729 2.612-7.59 2.612-.494 0-.982-.028-1.465-.086 2.705 1.736 5.922 2.756 9.356 2.756 11.225 0 17.366-9.302 17.366-17.366 0-.265-.006-.528-.018-.79A12.484 12.484 0 0 0 24 4.01z"/></svg>
        </a>
      </div>
      <hr />
      <div class="footer-bottom">
        <p class="copyright-text">© 2023 IMAJI COFFEE, All rights reserved</p>
        <div class="footer-bottom-right">
          <div class="footer-actions">
            <button class="delivery-button">Delivery Order</button>
            <a href="#"><img src={placeholderImg} alt="Download on the App Store badge" class="app-badge" /></a>
            <a href="#"><img src={placeholderImg} alt="Google Play badge" class="app-badge" /></a>
          </div>
          <div class="legal-links">
            <a href="#">Terms and Conditions</a>
            <a href="#">Privacy Policy</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</div>

<style>
  :root {
    --primary-color: #B9926B;
    --text-color: #38220f;
    --background-color: #F9F5F0;
    --footer-background: #1C1C1C;
    --footer-text: #FFFFFF;
  }

  /* Global Styles & Mobile First */
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: var(--background-color);
    color: var(--text-color);
  }

  .page-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  img {
    max-width: 100%;
    height: auto;
    display: block;
  }
  
  hr {
    border: none;
    border-top: 1px solid #444;
    width: 100%;
    margin: 2rem 0;
  }

  /* Header */
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 0;
    flex-wrap: wrap; /* Allow wrapping on small screens */
  }

  .logo-link {
    font-size: 1.8rem;
    font-weight: 500;
  }

  .desktop-nav {
    display: none; /* Hidden on mobile */
  }

  .header-actions {
    display: flex;
    gap: 0.5rem;
  }

  .order-button, .signin-button {
    padding: 0.6rem 1.2rem;
    border-radius: 4px;
    border: 1px solid var(--primary-color);
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.2s ease-in-out;
  }

  .order-button {
    background-color: var(--primary-color);
    color: white;
  }

  .signin-button {
    background-color: transparent;
    color: var(--primary-color);
  }

  .order-button:hover {
      background-color: #a57d56;
  }
  .signin-button:hover {
      background-color: var(--primary-color);
      color: white;
  }
  

  /* Main Article */
  main {
    padding: 2rem 0;
  }

  article {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  
  .article-title {
    font-size: 2.2rem;
    line-height: 1.2;
    margin-bottom: 1rem;
  }

  .article-meta {
    color: #666;
    margin-bottom: 2rem;
  }

  .main-image {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 2.5rem;
  }

  .article-content {
    text-align: left;
    line-height: 1.8;
    color: #444;
  }

  .article-content p {
    margin-bottom: 1.5rem;
  }

  /* Other News Section */
  .other-news-section {
    padding: 4rem 0;
    margin-top: 2rem;
  }

  .section-title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 2.5rem;
  }

  .news-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .news-card-link {
    display: block;
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    transition: transform 0.2s;
  }

  .news-card-link:hover {
    transform: translateY(-5px);
  }
  
  .news-card-image {
    width: 100%;
    height: 220px;
    object-fit: cover;
  }

  .news-card-title {
    font-size: 1.2rem;
    margin: 1rem 1.5rem 0.5rem;
  }

  .news-card-meta {
    font-size: 0.9rem;
    color: #888;
    margin: 0 1.5rem 1.5rem;
  }

  .pagination-dots {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    margin-top: 2.5rem;
  }

  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #D9D9D9;
  }

  .dot.active {
    background-color: var(--primary-color);
  }

  /* Footer */
  footer {
    background-color: var(--footer-background);
    color: var(--footer-text);
    padding: 4rem 1rem;
  }

  .footer-container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .footer-top {
    text-align: center;
    line-height: 1.7;
  }
  
  .footer-heading {
      font-size: 2rem;
      margin-bottom: 1.5rem;
  }

  .footer-top p {
    color: #ccc;
    margin: 0.5rem 0;
  }
  
  .social-icons {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin: 2rem 0;
  }
  .social-icons a svg {
    stroke: #ccc;
    transition: stroke 0.2s;
  }
  .social-icons a:hover svg {
    stroke: var(--footer-text);
  }

  .footer-bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    text-align: center;
  }

  .copyright-text {
    color: #aaa;
    font-size: 0.9rem;
  }

  .footer-bottom-right {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }

  .footer-actions {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .delivery-button {
    background: none;
    border: 1px solid var(--footer-text);
    color: var(--footer-text);
    padding: 0.75rem 1.5rem;
    width: 250px;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .delivery-button:hover {
      background-color: rgba(255,255,255,0.1);
  }

  .app-badge {
    height: 40px;
  }
  
  .legal-links {
    display: flex;
    gap: 1rem;
  }
  
  .legal-links a {
      color: #aaa;
      font-size: 0.9rem;
  }
  
  .legal-links a:hover {
      text-decoration: underline;
  }

  /* Tablet Breakpoint */
  @media (min-width: 768px) {
    .page-container {
      padding: 0 2rem;
    }
    .header-actions {
      gap: 1rem;
    }
    .desktop-nav {
      display: flex;
      gap: 1.5rem;
    }
    .article-title {
        font-size: 2.8rem;
    }
    .news-grid {
      grid-template-columns: 1fr 1fr;
    }
    .footer-actions {
      flex-direction: row;
      align-items: center;
    }
    .footer-bottom {
      flex-direction: row;
      justify-content: space-between;
    }
    .footer-bottom-right {
      align-items: flex-end;
    }
  }

  /* Desktop Breakpoint */
  @media (min-width: 1024px) {
    .desktop-nav {
      gap: 2.5rem;
    }
  }
</style>