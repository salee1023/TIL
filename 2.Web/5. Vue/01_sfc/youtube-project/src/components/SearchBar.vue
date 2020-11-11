<template>
  <div>
    <!-- 1. 검색어를 입력하고 enter를 누르면 'onInputKeyword'라는 메서드가 실행된다. -->
    <input @keypress.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)

      // 2. onInputKeyword 메서드가 실행되면 부모 컴포넌트(App.vue)로 'input-change'라는 커스텀 이벤트와 데이터가 올라간다.
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>