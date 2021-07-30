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

  <q-carousel
    v-model="jxfwslide"
    transition-prev="jump-right"
    transition-next="jump-left"
    swipeable
    arrows
    control-color="primary"
    animated
    height="100%"
  >
    <q-carousel-slide
      v-for="(n,index) in recvieApi.jxfw.data"
      :key="index"
      :name=index
      class="column no-wrap "
    >
      <div
        class="col-3"
        v-for="nn in n "
        :key="nn"
        style="text-align:center"
      >
        <q-btn
          round
          :color=nn.color
          :icon=nn.icon
          type="a"
          :href=nn.href
        />
        <div><span>{{nn.label}}</span></div>
      </div>
    </q-carousel-slide>

  </q-carousel>
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
          recvieApi.jxfw.data = response['data']['jxfwList']
          recvieApi.jxfw.flag = false
          console.log('jxfwok')
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