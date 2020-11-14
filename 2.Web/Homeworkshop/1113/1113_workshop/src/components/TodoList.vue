<template>
  <div>
      <h2>TodoList</h2>
      <Todo
      v-for="(todo, idx) in todos"
      :key="idx"
      :todo="todo"
      />
  </div>
</template>

<script>
import Todo from './Todo'

export default {
    name: 'TodoList',
    components: {
        Todo,
    },
    computed: {
        todos: function () {
            return this.$store.state.todos
        } 
    }
}
</script>

<style>
div > h2 {
    text-align: center;
}
div {
    margin-bottom: 1rem;
}
</style>