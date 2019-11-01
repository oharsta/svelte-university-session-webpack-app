<script>
    import {onMount} from "svelte";
    import ToDo from "./ToDo.svelte"
    import Widget from "./Widget.svelte";
    import {user} from "./store";
    import Comp from "./Comp.svelte";

    let todoList = [];
    let counter = 1;

    onMount(async () => {
        const res = await fetch(`/api/todo`);
        todoList = await res.json();
    });
    let description = "";

    // the `$:` means 're-run whenever these values change'
    $: fullName = $user.name + " " + $user.lastName;

    const saveToDo = async () => {
        const newToDo = {description, done: false};
        await fetch(`/api/todo`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(newToDo)
        });
        description = "";
        const res = await fetch(`/api/todo`);
        todoList = await res.json();
    };

    const remove = async (item) => {
        await fetch(`/api/todo/${item._id}`, {method: "DELETE"});
        todoList = todoList.filter(i => i._id !== item._id);
    };

</script>

<style>
    .todo-container {
        display: flex;
        flex-direction: column;
        justify-content: left;
    }

    button {
        display: inline-block;
        margin: 25px;
        padding: 3px 10px;
        color: blue;
    }

    input.new {
        padding: 5px;
        margin-top: 15px;
        max-width: 400px;
    }
</style>

<div class="todo-container">
    {#each todoList as todo}
        <ToDo todo={todo} remove={remove}></ToDo>
    {:else}
    <!-- this block renders when todoList.length === 0 -->
        <p>Loading...</p>
    {/each}

    <input class="new" type="text" bind:value={description} on:keydown={e => e.key === "Enter" && saveToDo()}>

    <form on:submit|preventDefault={saveToDo}>
        <label for="name">Add an item</label>
        <input id="name" type="text" bind:value={description}/>
    </form>
</div>


<Widget>
    <h3 slot="header">Hello</h3>
    <p slot="footer">Copyright (c) 2019 Zilverline</p>
</Widget>

<p>{$user.name}</p>
<input bind:value={$user.name}>
<p>{fullName}</p>

<p>{$user.attributes.nested.value1}</p>
<input bind:value={$user.attributes.nested.value1}>
<p>{$user.attributes.l[1]}</p>
<ul>
    {#each $user.attributes.l as item}
        <li>{item}</li>
    {/each}
</ul>

<button on:click={() => user.update(value => {
    counter = counter + 3;
    value.attributes.l.push(counter);
    console.log(value.attributes.l.length);
    return value;
})}>Add</button>

<p>comp</p>
<Comp/>