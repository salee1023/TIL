<template>
  <div>
    <input @keypress.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)

      // 부모에게 event를 알려준다.(방출한다.) ('커스텀 이벤트', 넘겨줄 데이터)
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>