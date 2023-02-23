<template>
    <Link
        class="text-black hover:text-blue-700 transition duration-300 transform hover:-translate-y-1 hover:scale-110"
        :class="{'font-bold underline': active}"
    >
        <slot />
    </Link>
</template>

<script>
import { Link } from "@inertiajs/inertia-vue3";

export default {
    props: {
        active: Boolean
    },
    components: { Link }
}
</script>

<style scoped>

</style>
