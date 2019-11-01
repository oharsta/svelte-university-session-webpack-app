import {writable} from 'svelte/store';

export const user = writable({
    name: "John",
    lastName: "Doe",
    attributes: {
        nested: {
            value1: "Nice",
            value2: ""
        },
        l: [1, 2, 3]
    }
});