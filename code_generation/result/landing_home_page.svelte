<script>
    import { push } from 'svelte-spa-router';

    function navigateToBlogDetail() {
        push('/blog_detail');
    }

    function navigateToBlogList() {
        push('/blog_list');
    }

    function navigateToEventList() {
        push('/event_list');
    }

    function navigateToHome() {
        push('/landing_home');
    }
</script>

<main>
    <h1>Choose your Coffee & Space</h1>
    <p>"IMA4JI Coffee has been serving 20,000+ cups of coffee and providing a comfortable place for our customers to work since 2010."</p>
    <img src="assets/images/template.png" alt="template" />
    <img src="assets/images/template.png" alt="template" />

    <h2>We Provide Your Space For Your Work or Mini event With Your Favorite coffee.</h2>
    <p>"Our story begins in 2010 with a simple idea from our founder that the most comfortable place to work is anywhere, because ideas are not limited by space and time, and the most comfortable place is in a café where their favorite coffee is available."</p>
    <p>"All the best local coffee bean varieties from throughout Indonesia are available with us. Directly from selected farmers, high-quality beans are processed and roasted to perfection by ourselves, then passed on to our skilled baristas who are passionate about preparing a cup of longed-for happiness from home."</p>
    <img src="assets/images/template.png" alt="template" />
    <img src="assets/images/template.png" alt="template" />
    <img src="assets/images/template.png" alt="template" />
    <img src="assets/images/template.png" alt="template" />

    <h2>Find Your Favorite Menu</h2>
    <img src="assets/images/template.png" alt="template" />
    <h3>RISTRETTO BIANCO</h3>
    <img src="assets/images/template.png" alt="template" />
    <h3>FRENCH TOAST WITH SUGAR</h3>
    <img src="assets/images/template.png" alt="template" />
    <h3>AT HOME HOUSE BLEND</h3>

    <h2>8 Comfy Workspace</h2>
    <p>"We provide many attractive and unique workspaces so you will have no trouble finding a workspace you want."</p>
    <img src="assets/images/template.png" alt="template" />
    <h3>"WHITE WALL Workspace"</h3>
    <img src="assets/images/template.png" alt="template" />
    <h3>"LONG WINDOW Workspace"</h3>
    <img src="assets/images/template.png" alt="template" />
    <h3>GENGS SPACE</h3>
    <p>Workspace</p>

    <h2>We Grow Together With Our Customer</h2>
    <p>"We believe that we are big not because of us but because of them. They are the ones who motivate us to continue to innovate to provide a quality coffee taste and comfortable space that is getting better every day."</p>
    <button on:click={() => navigateToEventList()}>Explore Other Event</button>
    <img src="assets/images/template.png" alt="template" />
    <h3>LATTE ART WORKSHOP</h3>
    <p>20 Feb 2023</p>
    <img src="assets/images/template.png" alt="template" />
    <p>EXHIBITION COFFEE HARDWARE</p>
    
    <div>
    <p>"Imaji Coffee Podcast" label:</p>
    <p>"Podcast player component:"</p>
    </div>

    <h2>Latest News</h2>
    <p>"Get the latest updates and deeper coffee experience from IMA4JI Coffee."</p>
    <img src="assets/images/template.png" alt="template" />
    <p on:click={navigateToBlogDetail}>"Collaboration to develop Coffee and Beverage Industry Expertise in Indonesia"</p>

    <button on:click={navigateToBlogList}>See All News</button>

    <button>Order</button>
    <button>Sign In</button>

    <p>"Terms and Conditions | Privacy Policy"</p>
    <p>© 2023 IMAJI COFFEE, All rights reserved</p>
</main>