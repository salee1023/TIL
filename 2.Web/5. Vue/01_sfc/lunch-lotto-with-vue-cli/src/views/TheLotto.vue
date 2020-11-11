<template>
  <div>
    <h1>로또</h1>
    <button @click="pickLotto">Get Lucky Numbers</button>
    <p>{{ Lotto }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'TheLotto',
    data: function () {
        return {
            numbers: _.range(1,46),
            Lotto: '',
        }
    },
    methods: {
        pickLotto: function () {
            const selectedLotto = _.sampleSize(this.numbers, 6)
            const sortedLotto = _.sortBy(selectedLotto)
            this.Lotto = sortedLotto
        } 
    }
}
</script>

<style>

</style>