<template>
  <div id="grand-parent">
      <h2>GrandParent</h2>
      <input v-model="grandParentData" type="text">
      <p>parentData: {{ parentData }}</p>
      <p>childData: {{ childData }}</p>
      <Parent 
        :grandParentData="grandParentData" 
        @child-input="onChildInput"
        @parent-input="onParentInput"
        />
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'

export default {
    name: 'GrandParent',
    components: {
        Parent,
    },
    data: function () {
        return {
            grandParentData: '',
            childData: '',
            parentData: '',
        }
    },
    methods: {
        onChildInput: function (text) {
            this.childData = text
        },
        onParentInput: function (text) {
            this.parentData = text
        }
    },
}
</script>

<style>
#grand-parent {
    border: 2px solid black;
}
</style>