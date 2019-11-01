<script>
    export let todo;
    export let remove;

    const className = todo => todo.done ? "done" : "not-done";

    const update = async () => {
        const toSave = {...todo, done:!todo.done};
        const res = await fetch(`/api/todo`, {method:"PUT", headers: {"Content-Type": "application/json"}, body: JSON.stringify(toSave)});
        todo = await res.json();
    }

</script>

<style>
    label {
        display: inline-block;
    }

    label {
        color: grey;
    }
    label.done {
        color: green;
    }
    span {
        color: red;
        cursor: pointer;
    }

</style>

<div class="todo">
    <input id="{todo._id}" type="checkbox" bind:checked={todo.done} on:click={update}>
    <label for="{todo._id}" class:done={todo.done}>{todo.description}</label>
    <span on:click={() => remove(todo)}>X</span>
</div>
