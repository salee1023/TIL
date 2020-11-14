<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>전체 일: {{ allTodosCount }}</h2>
    <h2>완료 된 일 : {{ completedTodosCount }}</h2>
    <h2>완료 되지 않은 일 : {{ uncompletedTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm
  },
  computed: {
    // allTodosCount: function () {
    //   return this.$store.getters.allTodosCount
    // },
    // completedTodosCount: function () {
    //   return this.$store.getters.completedTodosCount
    // },
    // uncompletedTodosCount: function () {
    //   return this.$store.getters.uncompletedTodosCount
    // }

    // 1. 첫번째 mapGetters
    // ...mapGetters({
    //   'allTodosCount': 'allTodosCount',
    //   'completedTodosCount': 'completedTodosCount',
    //   'uncompletedTodosCount': 'uncompletedTodosCount',
    // })

    // 2. 두번째 mapGetters
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'uncompletedTodosCount',
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
