<script>
    import {user} from "./store";
    import { title } from './style.js';
</script>

<p class="{ title }">{$user.attributes.nested.value1}</p>
<input bind:value={$user.attributes.nested.value1}>

<p>{$user.attributes.nested.value3 || "Nope"}</p>
<input bind:value={$user.attributes.nested.value3}>
