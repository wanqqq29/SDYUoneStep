<template>
  <div class="q-pa-sm">
    <q-responsive
      :ratio="2/1"
      style="width:100%;max-height:300px"
    >
      <q-carousel
        animated
        v-model="slide"
        infinite
        :autoplay="autoplay"
        transition-prev="slide-right"
        transition-next="slide-left"
        arrows
      >
        <q-carousel-slide
          v-for="(i,index) in banner.data"
          :key='index'
          :name=index
          :img-src=i.bSrc
        />
      </q-carousel>
    </q-responsive>

  </div>
  <div class="row q-pa-sm">
    <div class="col-6">
      <span
        class="material-icons"
        style="font-size:24px"
      >
        pin_drop
      </span>
      <span>
        济南市:
      </span>
      <span> {{weather.data}}</span>
    </div>
    <div
      class="col-6"
      style="text-align:right"
    >
      {{weather.time}}
    </div>
  </div>
  <hr>
  <div class="row q-pa-md q-px-lg q-pb-md">
    <q-timeline color="secondary">
      <q-timeline-entry
        heading
        body="校园新闻"
      />
      <div
        v-for="(i,index) in news.data"
        :key="index"
      >
      <a class='timeline' :href=i.href>
        <q-timeline-entry
          :title=i.title
          :subtitle=i.subtitle
          :body=i.body
        />
      </a>
      </div>

    </q-timeline>
  </div>
</template>



<script>
import { api } from 'boot/axios';
import { useQuasar, date } from 'quasar';
import { ref, reactive, onMounted } from 'vue';
export default {
  setup() {
    const $q = useQuasar()
    const weather = reactive({
      temp: '',
      text: '',
      data: '',
      time: ''
    })
    const banner = reactive({
      data: '',
    })
    const news = reactive({
      data: ''
    })
    function loadData() {
      api.get('https://devapi.qweather.com/v7/weather/now?location=101120101&key=0ff640e9311c4b92b733e2d8c12765c6')
        .then((response) => {
          weather.temp = response['data']['now']['temp']
          weather.text = response['data']['now']['text']
          weather.data = weather.temp + '℃，' + weather.text
        })
        .catch(error => {
          weather.data = 'NetWorkError'
        })
      let timeStamp = Date.now()
      let formattedString = date.formatDate(timeStamp, 'YYYY-MM-DD 星期d HH:mm')
      weather.time = formattedString


      api.get('/bannerApi/')
        .then((response) => {
          banner.data = response['data']['banner']
          // banner.bSrc = response['data']['bSrc']
        })
        .catch(error => {
          console.log(error)
        })
      api.get('/newsApi/')
        .then((response) => {
          news.data = response['data']['news']
          console.log(news.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
    onMounted(() => {
      loadData()
    })

    return {
      loadData,
      weather,
      slide: ref(0),
      autoplay: true,
      banner,
      news,
    }
  }
}


</script>
<style>
.timeline{
  color:black;
  text-decoration: none;
}
</style>