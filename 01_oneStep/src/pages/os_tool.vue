<template>
  <div class="q-pa-sm">
    <q-banner class="bg-grey-3">
      系统正在维护,某些功能不可用
    </q-banner>
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
      </q-card-section>
        <q-separator color='primary' />

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
        <div
          v-for="(i,index) in recvieApi.chwl"
          :key="index"
        >
          <q-expansion-item
            class="shadow-1 overflow-hidden q-ma-sm"
            style="border-radius: 25px"
            expand-separator
            icon="explore"
            :label=i.label
            header-class="bg-purple text-white"
            expand-icon-class="text-white"
          >
            <q-card>
              <div class="row r-ma">
                <div
                  class="col-3"
                  v-for="(n,index) in i.list"
                  :key="index"
                  style="text-align:center"
                >
                  <q-btn
                    round
                    :color=n.color
                    :icon=n.icon
                    :to={name:n.href,params:{loc:index,pos:n.label}}
                  />
                    <!-- loc店铺位置，pos餐厅位置；pos南一，loc南一窗口1 -->

                  <div><span>{{n.label}}
                    </span></div>
                </div>
              </div>
            </q-card>
          </q-expansion-item>
        </div>

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
      }
    })

    function loadData() {
      // 教学服务
      api.get('/sJxfwApi/')
        .then((response) => {
          recvieApi.jxfw.data = response['data']['jxfwList']
          recvieApi.jxfw.flag = false
          console.log('jxfwok')
          recvieApi.shfw.data = response['data']['shfwList']['data']
          console.log('shfwok')
          recvieApi.shfw.flag = false
          recvieApi.chwl = response['data']['chwlList']
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