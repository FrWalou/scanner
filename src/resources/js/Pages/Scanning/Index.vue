<template>
    <Head>
        <title>
            Website Scanner - Scanned
        </title>
    </Head>
    <h1 class="text-3xl tracking-wide text-gray-800">Scanned</h1>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 grid-flow-row gap-4">
        <div
            class="relative bg-blue-200 p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer"
            v-for="website in websites"
            :key="website.id"
        >
            <div class="card-image">
                <img
                    src="{{ website.screen_path }}"
                    class="object-cover w-full h-48 rounded-lg"
                />
            </div>
            <div class="card-title">
                <h3 class="text-lg font-medium text-white">{{ website.title }}</h3>
                <h5 class="text-sm font-medium text-blue-600">{{ website.url }}</h5>
            </div>
        </div>
    </div>
    <!--<pagination class="mt-6" :links="websites.links" />-->
</template>
<script>

//import Pagination from "../Shared/Pagination.vue";
export default {
    //components: {Pagination},
    props: {
        websites: Array,
    },
}
</script>
