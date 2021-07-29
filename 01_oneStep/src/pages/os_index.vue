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
          :name="1"
          img-src="../assets/img/banner/1.jpg"
        />
        <q-carousel-slide
          :name="2"
          img-src="../assets/img/banner/2.jpg"
        />
        <q-carousel-slide
          :name="3"
          img-src="../assets/img/banner/1.jpg"
        />
        <q-carousel-slide
          :name="4"
          img-src="../assets/img/banner/2.jpg"
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
        body="Timeline heading"
      />
      <q-timeline-entry
        title="Event Title"
        subtitle="February 22, 1986"
        :body="body"
        to="/test"
      />

      <q-timeline-entry
        title="Event Title"
        subtitle="February 21, 1986"
        :body="body"
      />
    </q-timeline>
  </div>
</template>



<script>
import { api } from 'boot/axios';
import { useQuasar, date } from 'quasar';
import { ref, reactive, onMounted } from 'vue';
export default {
  setup () {
    const $q = useQuasar()
    const weather = reactive({
      temp: '',
      text: '',
      data: '',
      time: ''
    })
    function loadData () {
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
    }
    onMounted(() => {
      loadData()
    })

    return {
      loadData,
      weather,
      slide: ref(1),
      autoplay: true,
      body: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
    }
  }
}


</script>
