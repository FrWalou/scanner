<template>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 grid-flow-row gap-4">
        <div
            class="relative bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer"
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
                <h3 class="text-lg font-medium text-gray-900">{{ website.title }}</h3>
                <h5 class="text-lg font-medium text-gray-900">{{ website.url }}</h5>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            websites: Array,
        },
    }
</script>

<style scoped>

</style>
