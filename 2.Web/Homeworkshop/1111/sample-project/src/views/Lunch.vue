<template>
    <div>
    <!-- 3. 컴포넌트 보여주기 -->
    <Captain></Captain>
    <h2>점심메뉴</h2>
    <button @click="pickOneInLunchMenu">Pick Lunch</button>
    <p> {{ selectedLunchMenu }} </p>
  </div>
</template>

<script>
import _ from 'lodash'
// 1. 컴포넌트 불러오기
import Captain from '@/components/Captain.vue'

export default {
    name: 'Lunch',
    // 2. 컴포넌트 사용 등록하기
    components: {
        Captain
    },
    data: function () {
        return {
            lunch: ['짬뽕', '짜장면', '탕수육', '햄버거'],
            selectedLunchMenu: '',
        }
    },
    methods : {
        pickOneInLunchMenu: function () {
         const randomIndex = _.random(this.lunch.length-1)
         this.selectedLunchMenu = this.lunch[randomIndex]
        }
    },
}
</script>

<style>

</style>