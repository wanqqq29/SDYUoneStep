<template>
  <ul class="flex">
    <ScrollLetter
      v-for="(num, idx) of numArr.Unum"
      :key="idx"
      as="li"
      :i="num"
      :delay="idx + 1"
    />
  </ul>
</template>

<script>
import ScrollLetter from '../../components/ScrollLetter.vue'
import { ref, onMounted, reactive, onBeforeMount } from 'vue';

export default {
  name: 'App',
  components: { ScrollLetter, },

  setup() {
    const num = 'Hello'
    const numArr = reactive({
      Ustr: [],
      Unum: [],
    })
    const Arry = ref([])
    onMounted(() => {
      InitArry()
      S2U()
    })

    onBeforeMount(() => {

    })

    function InitArry() {
      for (var aa = 65; aa < 122; aa++) {
        Arry.value.push(String.fromCharCode(aa))
      }
    }
    function S2U() {
      for (let i = 0; i < num.length; i++) {
        numArr.Ustr.push(num[i])
        numArr.Unum.push(Arry.value.indexOf(num[i]))
      }
      console.log(numArr)
    }

    return {
      num,
      numArr,
      InitArry,
      S2U,
    }
  }
}
</script>

<style scoped>
.flex {
  display: flex;
  justify-content: center;
  margin-top: 200px;
  margin-bottom: 100px;
}
ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
</style>

