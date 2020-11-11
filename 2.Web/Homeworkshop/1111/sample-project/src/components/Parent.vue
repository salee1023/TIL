<template>
  <div id='parent'>
      <h2>Parent</h2>
      <input v-model="parentData" @input="onParentInput" type="text">
      <p>grandParentData: {{ grandParentData }}</p>
      <p>childData: {{ childData }}</p>
      <Child 
        :grandParentData="grandParentData" 
        :parentData="parentData"
        @child-input="onChildInput"/>
  </div>
</template>

<script>
import Child from '@/components/Child.vue'

export default {
    name: 'Parent',
    components: {
        Child
    },
    data: function () {
        return {
            parentData:'',
            childData: '',
        }
    },
    props: {
        grandParentData: {
            type: String,
        },

    },
    methods: {
        onChildInput: function (text) {
            this.childData = text
            this.$emit('child-input', this.childData)
        },
        onParentInput: function () {
            this.$emit('parent-input', this.parentData)
        }
    },
}
</script>

<style>
#parent {
    border: 2px solid crimson;
    margin: 1rem;
}
</style>