<template>
  <component
    :is="as"
    class="scroll-num"
    :class="{ 'border-animate': showAnimate }"
    :style="{ '--i': i, '--delay': delay }"
    @animationend="showAnimate = false"
  >
    <ul
      ref="ul"
      :class="{ animate: showAnimate }"
    >
      <li
        v-for="item in Arry "
        key="item"
      >
        {{item}}
      </li>
    </ul>

    <svg
      width="0"
      height="0"
    >
      <filter id="blur">
        <feGaussianBlur
          in="SourceGraphic"
          :stdDeviation="`0 ${blur}`"
        />
      </filter>
    </svg>
  </component>
</template>

<script>
import { ref, onMounted, watch, onBeforeUnmount, onBeforeMount } from 'vue';

export default {
  name: 'ScrollLetter',
  props: {
    as: {
      type: String,
      default: 'div'
    },
    L: {
      type: String,
      default: 1,
    },
    i: {
      type: Number,
      default: 1,
    },

    delay: {
      type: Number,
      default: 1
    },
    blur: {
      type: Number,
      default: 2
    }
  },
  setup(props) {
    const timer = ref(null)
    const showAnimate = ref(true)
    const Arry = ref([])
    const ul = ref(null)

    const ua = ref('')
    const isSafari = ref('')


    onBeforeMount(() => {
      InitArry()

    })
    onMounted(() => {
      ua.value = navigator.userAgent.toLowerCase()
      const testUA = regexp => regexp.test(ua)
      isSafari.value = testUA(/safari/g) && !testUA(/chrome/g)

      // Safari浏览器的兼容代码
      isSafari && (timer.value = setTimeout(() => {
        ul.value.setAttribute('style', `
        animation: none;
        transform: translateY(calc(var(--i) * -9.09%))
      `)
      }, props.delay * 1000))
      clear()

    })
    watch: (() => i(), () => {
      showAnimate = true
    })



    function clear() {
      clearTimeout(timer.value)
      return;
    }
    function InitArry() {
      for (var aa = 65; aa < 122; aa++) {
        Arry.value.push(String.fromCharCode(aa))
      }
    }
    return {
      timer,
      showAnimate,
      Arry,
      ul,
      InitArry,
      clear,
    }
  }
}


</script>

<style scoped>
.scroll-num {
  width: var(--width, 20px);
  height: var(--height, calc(var(--width, 20px) * 1.8));
  color: var(--color, #333);
  font-size: var(--height, calc(var(--width, 20px) * 1.1));
  line-height: var(--height, calc(var(--width, 20px) * 1.8));
  text-align: center;
  overflow: hidden;
}

.animate {
  animation: move 0.3s linear infinite,
    bounce-in-down 1s calc(var(--delay) * 1s) forwards;
}
.border-animate {
  animation: enhance-bounce-in-down 1s calc(var(--delay) * 1s) forwards;
}

ul {
  padding: 0;
  margin: 0;
  list-style: none;
  transform: translateY(calc(var(--i) * -1.754%));
}

@keyframes move {
  from {
    transform: translateY(-90%);
    filter: url(#blur);
  }
  to {
    transform: translateY(1%);
    filter: url(#blur);
  }
}

@keyframes bounce-in-down {
  from {
    transform: translateY(calc(var(--i) * -1.754% - 7%));
    filter: none;
  }
  25% {
    transform: translateY(calc(var(--i) * -1.754% + 3%));
  }
  50% {
    transform: translateY(calc(var(--i) * -1.754% - 1%));
  }
  70% {
    transform: translateY(calc(var(--i) * -1.754% + 0.6%));
  }
  85% {
    transform: translateY(calc(var(--i) * -1.754% - 0.3%));
  }
  to {
    transform: translateY(calc(var(--i) * -1.754%));
  }
}

@keyframes enhance-bounce-in-down {
  25% {
    transform: translateY(8%);
  }
  50% {
    transform: translateY(-4%);
  }
  70% {
    transform: translateY(2%);
  }
  85% {
    transform: translateY(-1%);
  }
  to {
    transform: translateY(0);
  }
}
</style>

