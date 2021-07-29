<template>
  <div>
    <h1>test</h1>
    {{weather.temp}}摄氏度，{{weather.text}}
  </div>

  <div
    v-for="n in recvieApi.ct"
    :key="n"
  >
    {{n}}
  </div>
</template>

<script>
import { api } from 'boot/axios';
import { useQuasar } from 'quasar';
import { ref, reactive, onMounted } from 'vue';

export default {
  setup () {
    const $q = useQuasar()
    const weather = reactive({
      temp: '',
      text: '',
    })
    const recvieApi = reactive({
      ct: ''
    })
    function loadData () {
      api.get('https://devapi.qweather.com/v7/weather/now?location=101120101&key=0ff640e9311c4b92b733e2d8c12765c6')
        .then((response) => {
          weather.temp = response['data']['now']['temp']
          weather.text = response['data']['now']['text']


        })
        .catch(error => {
          console.log(error)
          console.log('a')
        })
    }


    function loadData2 () {
      api.get('/ct')
        .then((response) => {
          console.log(response)
          recvieApi.ct = response['data']['ct']
          console.log(recvieApi.ct)
        })
        .catch(error => {
          console.log(error)
        })
    }

    onMounted(() => {
      setTimeout((loadData()), 1000)
      loadData2()
    })

    return { loadData, weather, loadData2, recvieApi }
  }
}
</script>