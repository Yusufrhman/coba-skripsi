<script>
  import { push } from 'svelte-spa-router';

  // Article Content (replace with actual data)
  let articleTitle = "Realizing The Mission of Global Expansion, Open its First Cafe in Singapore";
  let articleDate = "August 19, 2022";
  let articleImage = "assets/images/template.png";
  let articleText = `We are a small cafe, with a big dream of becoming a global cafe. We started our operations in Singapore, and we are now expanding to Singapore. We will be opening our first cafe in Beijing soon, and we also plan to open more cafes across the globe. Realizing The Mission of Global Expansion, Open its First Cafe in Singapore

The cafe is located at Dempsey Hill, one of the most sought-after areas in Singapore. It's a family-friendly neighborhood with a wide range of restaurants and cafes. With a diverse population and many people from different cultures, Global Expansion Cafe aims to bring international food culture to Singaporeans from all walks of life.

We are currently running our first pop-up shop at Dempsey Hill which will run until mid-November. Global Expansion Cafe will be open for lunch and dinner on weekdays as well as weekends. Global Expansion Cafe will introduce new tastes and experiences to Singaporeans by introducing international food culture.

We are currently running our pop-up shop in Singapore, and hope to launch our own café soon. A real estate company is established in Asia that develops communities and provides financial services globally. We believe in love and happiness, a sense of belonging, and the importance of a shared experience. Here you can be yourself, share stories and make friends.

We partner with companies who LOVE the world. The cafe is a place where people can go to enjoy the food and coffee, but also a place where they can meet new friends. The cafe is located in Pasir Ris. The cafe has a wide variety of menu items to choose from. In addition to the usual coffee and tea, there are also some specialty drinks such as smoothies, milkshakes and frozen yogurt.

There are many types of food available at the cafe such as sandwiches, soups, salads and desserts. The menu also includes vegetarian options for those who have special dietary needs. People can order their food online via the website or by calling the number given on the website. They will be able to choose their preferred time for pickup so that they don't miss out on any orders!`;

  function navigateToBlogList() {
    push('/blog_list');
  }

  function navigateToLandingHome() {
    push('/landing_home');
  }
</script>

<style>
  .container {
    font-family: sans-serif;
    padding: 20px;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .nav {
    display: flex;
    gap: 20px;
  }

  .article {
    margin-bottom: 20px;
  }

  .news {
    display: flex;
    flex-direction: column;
  }

  .news-item {
    margin-bottom: 10px;
  }
  .location-footer {
        margin-top: 20px;
        padding: 20px;
        background-color: #f0f0f0;
        text-align: center;
    }
</style>

<div class="container">
  <div class="header">
    <a href="/" on:click|preventDefault={navigateToLandingHome}>IMAIJI Coffee.</a>
    <nav class="nav">
      <a href="/landing_home" on:click|preventDefault={navigateToLandingHome}>Home</a>
      <a href="/story">Story</a>
      <a href="/menu">Menu</a>
      <a href="/space">Space</a>
      <a href="/community">Community</a>
      <a href="/news" on:click|preventDefault={navigateToBlogList}>News</a>
      <button on:click={() => alert('Order functionality not implemented')}>Order</button>
      <a href="/signin">Sign In</a>
    </nav>
  </div>

  <div class="article">
    <h1>{articleTitle}</h1>
    <p>{articleDate}</p>
    <img src={articleImage} alt="Article Image" />
    <p>{articleText}</p>
  </div>

  <h2>Other News</h2>
  <div class="news">
    <a href="/blog_detail" class="news-item" on:click|preventDefault={() => {}}>
      Collaboration to Develop Coffee and Beverage Industry Expertise in Indonesia
    </a>
    <a href="/blog_detail" class="news-item" on:click|preventDefault={() => {}}>
      Collaboration to Develop Coffee and Beverage Industry Expertise in Indonesia
    </a>
  </div>

  <div class="location-footer">
        <p>"J.l Bangkringan No 19, RT.II/RW.2, Kota Surabaya, 60124"</p>
        <p>Customer Service +6282-2876-6862</p>
        <p>We Are Open from Sun - Mon 10 AM - 22 PM</p>
    </div>
  <button on:click={navigateToBlogList}>Go to Blog List</button>
  <button on:click={navigateToLandingHome}>Go to Home Page</button>
</div>