<script>
  import {
    SkipToContent,
    Header,
    HeaderUtilities,
    HeaderGlobalAction,
  } from "carbon-components-svelte";
  import Notification20 from "carbon-icons-svelte/lib/Notification20";
  import UserAvatar20 from "carbon-icons-svelte/lib/UserAvatar20";
  import AppSwitcher20 from "carbon-icons-svelte/lib/AppSwitcher20";
  import { getContext } from "svelte";

  const ctx = getContext("Theme");

  $: if (ctx) {
    ctx.dark.subscribe((value) => {
      console.log("dark mode?", value);
    });
    ctx.light.subscribe((value) => {
      console.log("light mode?", value);
    });
    ctx.updateVar("--cds-productive-heading-06-font-size", "4rem");
  }
</script>

<Header company="PeerlockDB" platformName="Peerlock Information Database" href="/">
  <div slot="skip-to-content">
    <SkipToContent />
  </div>
  <HeaderUtilities>
    <HeaderGlobalAction aria-label="Login" icon="{UserAvatar20}" on:click={() => window.location = "__apiRoute__/login"}/>
  </HeaderUtilities>
</Header>
