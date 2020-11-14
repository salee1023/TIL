<template>
  <div id="app">
    <TodoForm/>
    <h4>
      완료: {{ completedTodosCount }} / {{ allTodosCount }}
      미완료: {{ uncompletedTodosCount }} / {{ allTodosCount }}
    </h4>
    <TodoList/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    completedTodosCount: function () {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount: function () {
      return this.$store.getters.uncompletedTodosCount
    },
    allTodosCount: function () {
      return this.$store.getters.allTodosCount
    }
  }
}
</script>

<style>
#app {
  border: 2px solid black;
  width: 60%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
