<template>
    <nav>
        <ul class="flex space-x-8">
            <li>
                <NavLink href="/" :active="$page.component == 'Home'">Home</NavLink>
            </li>
            <li>
                <NavLink href="/scanned" :active="$page.component == 'Scanned'">Scanned</NavLink>
            </li>
            <li>
                <NavLink href="/scanning" :active="$page.component == 'Scanning'">Scanning</NavLink>
            </li>
        </ul>
    </nav>
</template>

<script>
import NavLink from "./NavLink.vue";
export default {
    components: {NavLink},
}
</script>

<style scoped>

</style>
