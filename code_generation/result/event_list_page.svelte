<script>
  import { push } from 'svelte-spa-router';

  const headerLinks = [
    { text: 'Home', href: '/' },
    { text: 'Story', href: '/story' },
    { text: 'Menu', href: '/menu' },
    { text: 'Space', href: '/space' },
    { text: 'Community', href: '/community' },
    { text: 'News', href: '/news' },
    { text: 'Order', href: '/order' },
  ];

  const upcomingEvents = [
    {
      title: 'Latte Art Workshop',
      date: '20 Feb 2023',
      image: 'assets/images/template.png',
    },
    {
      title: 'Exhibition Coffee Hardware',
      date: '20 Mar 2023',
      image: 'assets/images/template.png',
    },
    {
      title: 'Factory Visit',
      date: '20 Apr 2023',
      image: 'assets/images/template.png',
    },
  ];

  const closedEvents = [
    {
      title: 'Bezzera Latte Art Competition',
      date: '20 Feb 2023',
      image: 'assets/images/template.png',
    },
    {
      title: 'Sensory and Cupping Class',
      date: '20 Mar 2023',
      image: 'assets/images/template.png',
    },
    {
      title: 'Public Cupping',
      date: '20 Feb 2023',
      image: 'assets/images/template.png',
    },
    {
      title: 'Competitions and Showcases',
      date: '20 Mar 2023',
      image: 'assets/images/template.png',
    },
    {
      title: 'Art and Coffee Festival',
      date: '20 Mar 2023',
      image: 'assets/images/template.png',
    },
  ];

  function goToHomePage() {
    push('/');
  }

  function goToLandingHome() {
    push('/landing_home'); //  Navigate to '/landing_home'
  }
</script>

<header>
  <a href="/" on:click|preventDefault={goToHomePage}>
    IMAJI Coffee.
  </a>
  <nav>
    <ul>
      {#each headerLinks as link}
        <li>
          <a href={link.href} on:click|preventDefault={() => push(link.href === '/' ? '/' : link.href.slice(1))}>
            {link.text}
          </a>
        </li>
      {/each}
      <li>
        <button on:click={() => alert('Sign In')}>Sign In</button>
      </li>
    </ul>
  </nav>
</header>

<main>
  <h1>Our Upcoming Events</h1>
  <p>
    We believe that we are big not because of us but because of them. they are the ones who motivate us to continue to innovate to provide a quality coffee taste and comfortable space that is getting better every day.
  </p>

  <section class="upcoming-events">
    {#each upcomingEvents as event}
      <a href="/event/{event.title.toLowerCase().replace(/ /g, '-')}">
        <img src={event.image} alt={event.title} />
        <h3>{event.title}</h3>
        <p>{event.date}</p>
      </a>
    {/each}
  </section>

  <h2>Events Closed</h2>

  <section class="closed-events">
    {#each closedEvents as event}
      <a href="/event/{event.title.toLowerCase().replace(/ /g, '-')}">
        <img src={event.image} alt={event.title} />
        <h3>{event.title}</h3>
        <p>{event.date}</p>
      </a>
    {/each}
  </section>

  <button>Load More</button>
</main>

<footer>
  <section class="location">
    <h2>Our Location</h2>
    <p>Jl. Bangkringan No 19, RT.11/RW.2, Kota Surabaya, 60124</p>
    <p>Customer Service +6282-2876-6862</p>
    <p>We Are Open from Sun - Mon 10 AM - 22 PM</p>
  </section>

  <section class="social-media">
    <a href="/landing_home" on:click|preventDefault={goToLandingHome}>Delivery Order</a>
    <a href="/landing_home" on:click|preventDefault={goToLandingHome}><img src="assets/images/template.png" alt="Apple App Store Button" /></a>
    <a href="/landing_home" on:click|preventDefault={goToLandingHome}><img src="assets/images/template.png" alt="Google Play Store Button" /></a>
  </section>

  <section class="copyright">
    <p>© 2023 IMAJI COFFEE, All rights reserved</p>
    <a href="/landing_home" on:click|preventDefault={goToLandingHome}>Terms and Conditions</a>
    <a href="/landing_home" on:click|preventDefault={goToLandingHome}>Privacy Policy</a>
  </section>
</footer>

<style>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
  }

  header a {
    font-weight: bold;
    text-decoration: none;
    color: black;
  }

  header nav ul {
    list-style: none;
    display: flex;
  }

  header nav ul li {
    margin-left: 20px;
  }

  main {
    padding: 20px;
  }

  h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }

  .upcoming-events,
  .closed-events {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
  }

  .upcoming-events a,
  .closed-events a {
    display: block;
    text-decoration: none;
    color: black;
  }

  .upcoming-events img,
  .closed-events img {
    width: 100%;
    height: auto;
    margin-bottom: 10px;
  }

  footer {
    background-color: #f0f0f0;
    padding: 20px;
  }

  button {
    padding: 10px 20px;
    background-color: #ddd;
    border: none;
    cursor: pointer;
  }
</style>