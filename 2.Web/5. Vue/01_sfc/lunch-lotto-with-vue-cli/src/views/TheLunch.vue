<template>
  <div>
    <h2>1. 점심 메뉴 추천</h2>
    <button @click="pickOneInLunchMenu">점심 메뉴 추천 해줘!</button>
    <p>오늘의 점심 메뉴는 {{ selectedLunchMenu }} 입니다!</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'TheLunch',
    data: function () {
        return {
            lunch: ['짬뽕', '짜장면', '탕수육'],
            selectedLunchMenu: '',
        }
    },
    methods: {
        pickOneInLunchMenu: function () {
         const randomIndex = _.random(this.lunch.length-1)
         this.selectedLunchMenu = this.lunch[randomIndex]
        }
    },
}
</script>

<style>

</style>