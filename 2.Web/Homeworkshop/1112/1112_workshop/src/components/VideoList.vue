<template>
  <ul class="video-list">
      <VideoListItem 
      v-for="video in videos" 
      :key="video.etag" 
      :video="video"
      @select-video="selectVideo"
      />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
    name: 'VideoList',
    components: {
        VideoListItem,
    },
    props: {
        videos: {
            type: Array,
        }
    },
    methods: {
        selectVideo: function (video) {
            this.$emit('select-video', video)
        }
    }
}
</script>

<style>
    .video-list {
        width: 30%;
        list-style: none;
        /* ul 태그 기본 스타일링 없애기 */
        padding: 0;
        margin: 0;
    }
</style>