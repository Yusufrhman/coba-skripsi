<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte'
  import BlogList from './routes/BlogList.svelte'
  import BlogDetail from './routes/BlogDetail.svelte'
  import EventList from './routes/EventList.svelte'

  const routes = {
    '/': Home,
    '/home': Home,
    '/blog': BlogList,
    '/blog/:id': BlogDetail,
    '/events': EventList,
  }
</script>

<main>
  <h1>Coffee Company</h1>
  <Router {routes} />
</main>

<style>
  main {
    padding: 1rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  h1 {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
  }
</style>