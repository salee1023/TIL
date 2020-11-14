<template>
    <div class="search-bar input-group" :style="{ margin: videosLength ? '0' : '40vh 0' }">
        <input @keypress.enter="onEnter" type="text" class="form-control" placeholder="검색" aria-label="Recipient's username" aria-describedby="button-addon2">
        <div class="input-group-append">
            <button @click="onEnter" class="btn btn-outline-secondary" type="button" id="button-addon2">🔍</button>
        </div>
    </div>  
</template>

<script>
export default {
    name: 'SearchBar',
    props: {
    videosLength: {
      type: Number,
        }
    },
    methods: {
        onEnter: function (event) {
            this.$emit('search-input', event.target.value)
        }
    },
}
</script>

<style>
.search-bar{
    transition: .5s;
}

</style>