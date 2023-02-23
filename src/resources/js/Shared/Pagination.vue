<!--<template>
    <div>
        <Component
            :is="link.url ? 'Link' : 'span'"
            v-for="link in links"
            :href="link.url"
            v-html="link.label"
            class="px-1"
            :class="link.url ? '' : 'text-grey-200'"
        />
    </div>
</template>-->
<template>
    <div v-if="links.length > 3">
        <div class="flex flex-wrap -mb-1">
            <template v-for="link in links">
                <div v-if="link.url === null"  class="mr-1 mb-1 px-4 py-3 text-sm leading-4 text-gray-400 border rounded" v-html="link.label" />
                <Link v-else class="mr-1 mb-1 px-4 py-3 text-sm leading-4 border rounded hover:bg-white focus:border-indigo-500 focus:text-indigo-500"
                      :class="{ 'bg-blue-700 text-white': link.active }"
                      :href="link.url"
                      v-html="link.label"
                />
            </template>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        links: Array,
    }
}
</script>
