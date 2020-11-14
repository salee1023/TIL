<template>
  <div class="video-detail" v-if="video">
    <div class="video-container">
      <iframe :src="videoURI" frameborder="0"></iframe>
    </div>
    <h4>{{ video.snippet.title | unescape }}</h4>
    <p>{{ video.snippet.description | unescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: "VideoDetail",
  props: {
    video: [Object, String]
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    unescape: function (text) {
      return _.unescape(text)
    }
  }
}
</script>

<style>
  .video-detail{
    width: 70%;
    margin-right: 1rem;
  }
  .video-detail > h4 {
    margin-top: 1rem;
  }
  .video-detail > p {
    font-size: 15px;
  }
  .video-container {
    position: relative; /* 기준 위치 잡기 */
    padding-top: 56.25%; /* 비디오 비율 맞추기 */
  }
  .video-container > iframe {
    position: absolute; /* container 기준으로 위치 잡기 */
    top: 0;
    width: 100%;
    height: 100%;
  }
</style>