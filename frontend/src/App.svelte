<script>
  import Header from "./components/Header.svelte";
  import Theme from "./components/Theme.svelte";
  import {Content} from "carbon-components-svelte/src/UIShell";

  import Router from "svelte-spa-router";

  import Dashboard from "./pages/Dashboard.svelte"
  import NotFound from "./pages/NotFound.svelte";

  import {theme} from "./stores";

  const routes = {
    "/": Dashboard,
    "*": NotFound,
  }
</script>

<style global lang="scss">
  @import "carbon-components-svelte/css/all";
</style>

<main>
  <Theme bind:theme={$theme} persist>
    <Header/>
    <Content style="background: none; padding: 1rem">
      <Router {routes}/>
    </Content>
  </Theme>
</main>
