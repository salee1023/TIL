<template>
  <div id="todo">
      <div>
        <span :class="{ completed: todo.completed }" @click="updateTodoStatus">{{ todo.title }}</span>
        <button @click="deleteTodo">X</button>
      </div>
  </div>
</template>

<script>
export default {
    name: "Todo",
    props: {
        todo: Object,
    },
    methods:{
        deleteTodo: function () {
            this.$store.dispatch('deleteTodo', this.todo)
        },
        updateTodoStatus: function () {
            this.$store.dispatch('updateTodoStatus', this.todo)
        }
    },
}
</script>

<style scoped>
#todo {
    text-align: center;
}
.completed {
    text-decoration: line-through;
}
</style>