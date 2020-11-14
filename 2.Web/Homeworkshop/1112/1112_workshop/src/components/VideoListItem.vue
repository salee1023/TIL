<template>
<div>
    <li @click="selectVideo">
        <div class="video-list-item">
            <img :src="youtubeImageSrc" alt="">
            <p>{{ video.snippet.title | unescape }}</p>
        </div>
    </li>  
    <hr>
</div>
</template>

<script>
import _ from 'lodash'

export default {
    name:'VideoListItem',
    props: {
        video: {
            tpye: Object,
        },
    },
    filters: {
        unescape: function (text) {
            return _.unescape(text)
        }
    },
    computed: {
        youtubeImageSrc: function () {
            return this.video.snippet.thumbnails.default.url
        }
    },
    methods: {
        selectVideo: function () {
            this.$emit('select-video', this.video)
        }
    }

}
</script>

<style>
    .video-list-item {
        display: flex;
        /* align-items: center; */
        margin-bottom: 1rem;
        cursor: pointer;
        height: 90px;
    }
    .video-list-item > img {
        height: fit-content; /* 텍스트 늘어나도 이미지는 원래 사이즈 유지 */
        margin-right: .5rem;
    }
    .video-list-item > p {
        text-overflow: ellipsis;
    }
</style>