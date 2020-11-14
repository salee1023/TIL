import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    },
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      if(todoItem.title){
        state.todos.push(todoItem)
      }
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if(todo === todoItem) {
          return {
            title: todo.title,
            completed: !todo.completed
          }
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  modules: {
  }
})
