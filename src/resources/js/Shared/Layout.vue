<template>
    <Head>
        <title>
            Website Scanner
        </title>
    </Head>
    <section class="p-6 bg-gray-200">
        <header class="flex justify-between">
            <div class="flex items-center">
                <h1 class="font-bold text-lg">Website Scanner</h1>
            </div>
            <Nav/>
        </header>
    </section>

    <section class="p-6">
        <div class="max-w-6xl mx-auto">
            <slot />
        </div>
    </section>

</template>

<script>
import Nav from "./Nav.vue";
import {Head} from "@inertiajs/inertia-vue3";

export default {
    components: {Nav, Head},
}
</script>

<style scoped>

</style>
