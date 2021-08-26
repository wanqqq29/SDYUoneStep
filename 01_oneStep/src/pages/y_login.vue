<template>
    <div class="q-pa-sm">
        <q-banner class="bg-blue-3">
            点击下方按钮，登录到统一身份认证
        </q-banner> 
        <q-btn color="blue" push class="loginbtn" type='a' href='http://jw.sdyu.edu.cn/sso/ktiotlogin'>
            <div class="row items-center no-wrap">
              <q-icon left name="map" />
              <div class="text-center logintext">
                登录
              </div>
            </div>
        </q-btn>
        <!-- <q-btn color="blue" push class="loginbtn" @click="dialog = true">
            <div class="row items-center no-wrap">
              <q-icon left name="map" />
              <div class="text-center logintext">
                登录
              </div>
            </div>
        </q-btn>
        <q-dialog v-model="dialog" persistent>
            <q-card>
                <q-card-section>
                    <div class='text'>只作生成Cookies使用，不会保存您的任何个人信息。</div>
                </q-card-section>
              <q-card-section class="row items-center">
                <iframe src="https://jw.sdyu.edu.cn/sso/ktiotlogin" frameborder="0" height="450px"></iframe>
              </q-card-section>
              -->
      
              <!-- Notice v-close-popup -->
              <!-- <q-card-actions align="right">
                <q-btn flat label="完成登录" color="primary" v-close-popup />
              </q-card-actions>
            </q-card>
          </q-dialog> -->
    </div>
</template>
<script>
    import { ref } from 'vue'
    
    export default {
      setup () {
        return {
          dialog: ref(false),
        }
      }
    }
    </script>
<style>
    .text{
        text-align: right;
        font-size:13px;
        justify-content:center;
        margin: 0;

    }
    .loginbtn{
        margin-top: 30px;
        height: 80px;
        width: 100%;
    }
    .logintext{
        font-size: 20px;
    }
</style>