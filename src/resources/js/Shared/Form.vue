<template>
    <form class="mb-4">
        <div class="flex items-center">
            <input
                v-model="inputUrl"
                type="text"
                placeholder="Enter an url"
                class="w-full px-3 py-2 mr-2 text-gray-700 bg-white rounded-lg shadow-md focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
            <Link
                as="button"
                @click="handleScanButtonClick"
                class="px-4 py-2 text-white bg-blue-500 rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
            >
                Scan
            </Link>
        </div>
    </form>
    <form @submit.prevent="submitForm">
        <input
            v-model="url"
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
            console.log(this.url);
            Inertia.post('/scanning', { url: this.url });
            this.url = '';
        }
    },
}
</script>
