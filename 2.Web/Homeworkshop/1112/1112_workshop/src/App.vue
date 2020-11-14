<template>
  <div id="app">
    <header>
      <SearchBar 
        @search-input="onSearchInput"
        :videos-length="videos.length"
        />
    </header>
    <section>
      <VideoDetail :video="selectedVideo"/>
      <VideoList :videos="videos" @select-video="selectVideo"/>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

const YOUTUBE_API_URL= 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onSearchInput: function (query) {
      axios.get(YOUTUBE_API_URL, {
        params: {
              key: YOUTUBE_API_KEY,
              part: 'snippet',
              type: 'video',
              q: query,
            }
      })
      .then(res => {
        console.log(res)
        this.videos = res.data.items
        if (!this.selectedVideo) {
          this.selectedVideo = this.videos[0]
        }
      })
      .catch(err => console.log(err))
      console.log(query)
      console.log(YOUTUBE_API_KEY)
    },
    selectVideo: function (video) {
      this.selectedVideo = video
    }
  }

}

</script>

<style>
header,
section {
  width: 80%; /* 너비 80% 만큼 차지 */
  margin: 0 auto; /* 양 옆 마진 똑같이 */
  padding: 1rem 0;
}

section {
  display: flex;
}
</style>
