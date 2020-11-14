# 1111_practice

- Home.vue

```vue
<template>
  <div class="home">
      <GrandParent/>
  </div>
</template>

<script>
import GrandParent from '@/components/GrandParent.vue'

export default {
    name: 'Home',
    components: {
        GrandParent
    }
}
</script>

<style>

</style>
```

---

- GrandParent.vue

```vue
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
```

---

- Parent.vue

```vue
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
```

---

- Child.vue

```vue
<template>
  <div id='child'>
      <h2>Child</h2>
      <input v-model="childData" @input="onInput" keytype="text">
      <p>grandParentData: {{ grandParentData }}</p>
      <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
    name: 'Child',
    props: {
        grandParentData: {
            type: String,
        },
        parentData: {
            type: String,
        }
    },
    data: function () {
        return {
            childData: '',
        }
    },
    methods: {
        onInput: function () {
            this.$emit('child-input', this.childData)
        }
    }
}
</script>

<style>
#child {
    border: 2px solid darkblue;
    margin: 1rem;
}
</style>
```

---

![image-20201111174619548](1111_workshop.assets/image-20201111174619548.png)

