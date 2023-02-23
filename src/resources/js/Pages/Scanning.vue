<template>
    <Head>
        <title>
            Website Scanner - Scanning
        </title>
    </Head>
    <h1 class="text-3xl tracking-wide text-gray-800">SCANNING</h1>
    <form @submit.prevent="submitForm" method="POST">
        <input
            v-model="form.url"
            type="text"
            placeholder="Enter URL"
            class="w-2/3 px-3 py-2 mr-2 text-gray-700 bg-white rounded-lg shadow-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        >
        <button class="px-4 py-2 text-white bg-blue-500 rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
                type="submit">Submit</button>
    </form>
</template>

<script>
import {Link} from "@inertiajs/inertia-vue3";
import {Inertia} from "@inertiajs/inertia";

export default {
    components: {Link},
    data() {
        return {
            form: {
                url: ''
            },
        }
    },
    methods: {
        submitForm() {
            Inertia.post('/scanning', { url: this.form.url });
            this.form.url = '';
        }
    },
}
</script>
