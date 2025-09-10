<script>
  import { Router } from "@mateothegreat/svelte5-router";

  // Import page components based on the PTG nodes
  import RootPage from "./pages/RootPage.svelte";
  import BlogListPage from "./pages/BlogListPage.svelte";
  import BlogDetailPage from "./pages/BlogDetailPage.svelte";
  import EventListPage from "./pages/EventListPage.svelte";

  // Configure the routes for the application
  const routes = [
    {
      // The 'root' node is the default route for the path "/"
      component: RootPage,
    },
    {
      // The 'blog_list' node
      path: "/blog",
      component: BlogListPage,
    },
    {
      // The 'blog_detail' node, using a dynamic parameter for the article slug
      path: "/blog/:slug",
      component: BlogDetailPage,
    },
    {
      // The 'event_list' node
      path: "/events",
      component: EventListPage,
    },
  ];
</script>

<main>
  <Router {routes} />
</main>
