<script>
  import { push } from 'svelte-spa-router';

  let blogArticles = [
    {
      title: "Collaboration to Develop Coffee and Beverage Industry Expertise in Indonesia",
      image: "assets/images/template.png",
      date: "4 Min - August 19, 2022",
      id: "collaboration"
    },
    {
      title: "Visited Doesoen Sirap Coffee, The Producer of Robusta in Central Java",
      image: "assets/images/template.png",
      date: "4 Min - August 19, 2022",
      id: "doesoen"
    },
    {
      title: "Cold Brew Coffee, How to Drink Cold Coffee is More Enjoyable",
      image: "assets/images/template.png",
      date: "4 Min - August 19, 2022",
      id: "coldbrew"
    },
    {
      title: "Meet Coffee Tonic, the Sensation of Drinking Coffee-Flavored Soda",
      image: "assets/images/template.png",
      date: "4 Min - August 19, 2022",
      id: "coffee tonic"
    },
    {
      title: "Workshop Coffee Sharing Session",
      image: "assets/images/template.png",
      date: "4 Min - August 19, 2022",
      id: "sharing"
    },
    {
      title: "Workshop Coffee Brewing",
      image: "assets/images/template.png",
      date: "4 Min - August 19, 2022",
      id: "brewing"
    }
  ];

  function goToBlogDetail(id) {
    push(`/blog_detail?id=${id}`);
  }

    function goToHome() {
        push(`/landing_home`);
    }

  function navigateTo(route) {
    push(route);
  }

</script>

<style>
  .blog-list {
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
    gap: 10px;
  }

  .blog-article {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
  }

  .blog-article img {
    width: 100%;
    max-height: 200px;
    object-fit: cover;
    margin-bottom: 10px;
  }

  .blog-article a {
    text-decoration: none;
    color: #333;
  }

  .blog-article h3 {
    margin: 0;
  }

  .blog-article p {
    margin: 5px 0;
    font-size: 0.8em;
    color: #777;
  }

  .footer {
    margin-top: 30px;
    text-align: center;
    color: #777;
    font-size: 0.8em;
  }
</style>

<div class="blog-list">
    <div class="header">
         <a href="/" on:click|preventDefault={goToHome}>IMALI Coffee.</a>
        <nav class="nav">
            <a href="/" on:click|preventDefault={goToHome}>Home</a>
            <a href="/">Story</a>
            <a href="/">Menu</a>
            <a href="/">Space</a>
            <a href="/">Community</a>
            <a href="/blog_list">News</a>
            <button>Order</button>
            <button>Sign In</button>
        </nav>
    </div>

    <h1>Our News</h1>
    <p>Get the latest updates and deeper coffee experience from IMAJI Coffee.</p>

    <img src="assets/images/template.png" alt="Coffee shop" />

  {#each blogArticles as article}
    <div class="blog-article">
      <img src={article.image} alt={article.title} />
      <a href="#" on:click|preventDefault={() => goToBlogDetail(article.id)}>
        <h3>{article.title}</h3>
      </a>
      <p>{article.date}</p>
    </div>
  {/each}

  <button>Load More</button>

  <h2>Our Location</h2>
  <p>Jl. Bangkringan No 19, RT.11/RW.2, Kota Surabaya, 60124<br>
    Customer Service +6282-2876-6862<br>
    We Are Open from Sun - Mon 10 AM - 22 PM
  </p>

  <p>© 2023 IMAJI COFFEE, All rights reserved</p>
</div>