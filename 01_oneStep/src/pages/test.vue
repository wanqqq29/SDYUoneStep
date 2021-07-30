<template>
  <div>
    <h1>test</h1>
    {{weather.temp}}摄氏度，{{weather.text}}
  </div>
  <div
    v-for="n in recvieApi.ct"
    :key="n"
  >
    {{n}}111
  </div>

  <q-card
    v-for="(i,index) in recvieApi.chwl"
    :key="index"
  >
    {{i.label}}
    <q-item
      v-for="(ii,index1) in i.list"
      :key="index1"
    >
      {{ii}}
    </q-item>
  </q-card>
</template>

<script>
import { api } from 'boot/axios';
import { useQuasar } from 'quasar';
import { ref, reactive, onMounted } from 'vue';

export default {
  setup() {
    const $q = useQuasar()
    const weather = reactive({
      temp: '',
      text: '',
    })
    function loadData() {
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

    const aaa = ref('aa')

    const recvieApi = reactive({
      jxfw: {
        data: '',
        flag: true,
      },
      shfw: {
        data: '',
        flag: true,
      },
      chwl: {
        ct: '',
        yp: '',
        gc: '',
        flag: ''
      }
    })
    function loadData2() {
      api.get('http://127.0.0.1:8000/sJxfwApi/')
        .then((response) => {
          recvieApi.chwl = response['data']['chwlList']
          console.log(response['data']['chwlList'])
          console.log(recvieApi.chwl)

        })
        .catch(error => {
          console.log(error)
        })
    }
    onMounted(() => {
      setTimeout((loadData()), 1000)
      loadData2()
    })

    return {
      loadData, weather, loadData2, recvieApi, aaa,
      jxfwslide: ref('page1'),
    }
  }
}
</script>