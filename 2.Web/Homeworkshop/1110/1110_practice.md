# 1110_practice

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>1110_practice</title>
</head>
<body>
  <div id="app">
    <h1>Cat Image</h1>
    <p>{{ catImageSrcSlash }}</p>
    <img :src="catImageSrc" alt="cat Image">
    <button @click="getCatImages">Get Cat</button>
  </div>


  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue ({
      el: "#app",
      data: {
        catImageSrc: '', //
      },
      computed: {
        catImageSrcSlash: function () {
          return this.catImageSrc + '/love'
        }
      },
      watch: {
        catImageSrc: function (value, value2) {
          console.log('watch!')
          console.log(value) //바뀐값
          console.log(value2) //바뀌기전값
        }
      },
      // method에서 this: 자기자신, arrow function에서 this: 상위스코프
      methods: {
        // getCatImages  함수를 실행
        getCatImages: function () {
            const catAPIUrl = 'https://api.thecatapi.com/v1/images/search'
            axios.get(catAPIUrl)
            // 정상적으로 응답이 오면
              .then(res => {
                this.catImageSrc = res.data[0].url
              })
              .catch(err => {
                console.log(err)
              })
        }
      }
    })
  </script>
</body>
</html>
```

