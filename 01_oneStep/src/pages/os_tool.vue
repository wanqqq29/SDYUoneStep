<template>
  <div class="q-pa-sm">
    <q-card class="my-card">

      <!-- 教学服务 -->
      <q-card-section>
        <q-chip
          color="primary"
          text-color="white"
          icon="bookmark"
          size="sm"
        >
          教学服务
        </q-chip>
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
              class="row"
              v-if="!recvieApi.jxfw.flag"
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
          </div>
          </q-carousel-slide>
        </q-carousel>
        <q-separator color='primary' />
      </q-card-section>
        <!-- 生活服务 -->
        <q-card-section>
          <q-chip
            color="teal"
            text-color="white"
            icon="bookmark"
            size="sm"
          >
            生活服务
          </q-chip>
          <div class="row">
            <div
              class="col-3"
              v-for="n in recvieApi.shfw.data"
              :key="n"
              style="text-align:center"
            >
              <q-btn
                round
                :color=n.color
                :icon=n.icon
                type="a"
                :href=n.href
              />
              <div><span>{{n.label}}</span></div>
            </div>
          </div>
        </q-card-section>
        <q-separator color="teal" />
        <!-- 吃喝玩乐 -->
        <q-card-section>
          <q-chip
            color="purple"
            text-color="white"
            icon="bookmark"
            size="sm"
          >
            吃喝玩乐
          </q-chip>
          <q-expansion-item
            class="shadow-1 overflow-hidden q-ma-sm"
            style="border-radius: 25px"
            expand-separator
            icon="explore"
            label="餐厅"
            header-class="bg-purple text-white"
            expand-icon-class="text-white"
          >
            <q-card>
              <div class="row r-ma">
                <div
                  class="col-3"
                  v-for="(n,i) in recvieApi.chwl.ct"
                  :key="n"
                  style="text-align:center"
                >
                  <q-btn
                    round
                    :color=n.color
                    :icon=n.icon
                    :to={name:n.href,params:{loc:i}}
                  />
                  <div><span>{{n.label}}</span></div>
                </div>
              </div>
            </q-card>
          </q-expansion-item>
          <q-separator color="purple" />

          <q-expansion-item
            class="shadow-1 overflow-hidden q-ma-sm"
            style="border-radius: 25px"
            expand-separator
            icon="explore"
            label="饮品店"
            header-class="bg-purple text-white"
            expand-icon-class="text-white"
          >
            <q-card>
              <div class="row r-ma">
                <div
                  class="col-3"
                  v-for="n in recvieApi.chwl.yp"
                  :key="n"
                  style="text-align:center"
                >
                  <q-btn
                    round
                    :color=n.color
                    :icon=n.icon
                    type="a"
                    :href=n.href
                  />
                  <div><span>{{n.label}}</span></div>
                </div>
              </div>
            </q-card>
          </q-expansion-item>
          <q-separator color="purple" />

          <q-expansion-item
            class="shadow-1 overflow-hidden q-ma-sm"
            style="border-radius: 25px"
            expand-separator
            icon="explore"
            label="北苑广场"
            header-class="bg-purple text-white"
            expand-icon-class="text-white"
          >
            <q-card>
              <div class="row r-ma">
                <div
                  class="col-3"
                  v-for="n in recvieApi.chwl.gc"
                  :key="n"
                  style="text-align:center"
                >
                  <q-btn
                    round
                    :color=n.color
                    :icon=n.icon
                    type="a"
                    :href=n.href
                  />
                  <div><span>{{n.label}}</span></div>
                </div>
              </div>
            </q-card>
          </q-expansion-item>
        </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { api } from 'boot/axios';
import { ref, reactive, onMounted } from 'vue';
export default {
  setup() {
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

    function loadData() {
      // 教学服务
      api.get('http://127.0.0.1:8000/sJxfwApi/')
        .then((response) => {
          recvieApi.jxfw.data = response['data']['jxfwList']
          recvieApi.jxfw.flag = false
          console.log('jxfwok')
        })
        .catch(error => {
          console.log(error)
        })
      // 生活服务
      api.get('/shfw')
        .then((response) => {
          recvieApi.shfw.data = response['data']['data']
          recvieApi.shfw.flag = false
          console.log('shfwok')
        })
        .catch(error => {
          console.log(error)
        })
      // 吃喝玩乐
      api.get('/chwl')
        .then((response) => {
          recvieApi.chwl.ct = response['data']['ct']
          recvieApi.chwl.yp = response['data']['yp']
          recvieApi.chwl.gc = response['data']['gc']
          recvieApi.chwl.flag = false
          console.log('chwlok')
        })
        .catch(error => {
          console.log(error)
        })
    }
    onMounted(() => {
      loadData()
    })

    return {
      recvieApi,
      jxfwslide: ref('page1'),
    }
  }




}
</script>

<style >
.r-ma {
  margin-top: 5px;
}
.q-carousel__slide,
.q-carousel .q-carousel--padding {
  padding: 0;
}
.q-carousel__next-arrow--horizontal {
  right: -8px;
}
.q-carousel__prev-arrow--horizontal {
  left: -8px;
}
</style>