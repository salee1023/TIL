<template>
  <div id="todoForm">
    <input @keypress.enter="createTodo" v-model.trim="todoTitle" type="text">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    data: function () {
        return {
            todoTitle: '',
        }
    },
    methods: {
        createTodo: function () {

            const todoItem = {
                title: this.todoTitle,
                completed: false,
            }

            this.$store.dispatch('createTodo', todoItem)
            this.todoTitle = ''
            
        }
    }
}
</script>

<style>
#todoForm {
    margin-top: 1rem;
}
</style>