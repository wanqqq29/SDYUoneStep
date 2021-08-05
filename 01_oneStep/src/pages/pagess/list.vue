<template>
  <q-page>
    <div class="q-pa-sm">
      <div class="row">
        <div class="col-12">
          <div class="row">
            <div class="col-3">
              <q-tabs
                v-model="tab"
                vertical
                class="text-teal"
              >
                <q-tab
                  v-for="(i,index) in tabpanel.data"
                  :name=i.ckID
                  :key="index"
                  :label=i.label
                />
              </q-tabs>

            </div>

            <div class="col-9">
              <q-tab-panels
                v-model="tab"
                animated
                vertical
                transition-prev="jump-up"
                transition-next="jump-up"
              >
                <q-tab-panel
                  v-for="(i,index) in tabpanel.data"
                  :name=i.ckID
                  :key="index"
                  :label=i.label
                >
                  <q-card>
                    <q-img :src=i.mSrc>
                      <div class="text-h5 absolute-bottom text-right">
                        {{i.label}}
                      </div>
                    </q-img>
                    <q-list>
                      <q-item
                        clickable
                        v-for="ii in card[i.ckID]"
                        :key="ii"
                      >
                        <q-item-section>
                          <q-img :src=ii.imgSrc />
                        </q-item-section>

                        <q-item-section>
                          <q-item-label hreader>{{ii.sName}}</q-item-label>
                          <q-item-label overline>￥{{ii.sPrice}}</q-item-label>
                          <q-item-label caption>{{ii.sDesc}}</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-card>
                </q-tab-panel>
              </q-tab-panels>
            </div>
          </div>
        </div>
      </div>

    </div>
    <q-page-scroller
      position="bottom-right"
      :scroll-offset="10"
      :offset="[18, 18]"
    >
      <q-btn
        fab
        icon="keyboard_arrow_up"
        color="primary"
      />
    </q-page-scroller>
  </q-page>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import { api } from 'boot/axios';


export default {
  setup() {
    const tabpanel = reactive({
      data: ''
    })
    const card = ref([{
      imgSrc: "https://cdn.quasar.dev/img/parallax2.jpg",
      sName: "商品名称",
      sPrince: "0",
      sDesc: "商品描述"
    }])
    const route = useRoute()
    const tab = ref('0')
    const pwd = ''
    // function load (a) {
    //   api.get('/ct_list?loc=' + a)
    //     .then((response) => {
    //       if (response['data']['tab'].flag != '0') {
    //         tabpanel.value = response['data']['tab']
    //         card.value = response['data']['card']
    //       } else {
    //         console.log('null')
    //       }

    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    // }
    function load(a) {
      api.get('/tabpanelApi/?pos=' + a)
        .then((response) => {
          console.log(response['data']['tab'])
          tabpanel.data = response['data']['tab']
          tab.value = response['data']['tab'][0]['ckID']

        })
        .catch(error => {
          console.log(error)
        })

      api.get('/cardApi/')
        .then((response) => {
          card.value = response['data']
          console.log(response['data'])
        })
        .catch(error => {
          console.log(error)
        })
    }


    onMounted(() => {
      load(route.params.pos)
      console.log(route.params.pos, 'pos')
      console.log(route.params.loc, 'loc')
    })

    return {
      splitterModel: 20,
      tabpanel,
      card,
      load,
      tab,
      pwd
    }
  }
}
</script>
