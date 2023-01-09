<template>
  <div class="container">
    <button v-on:click="iniciaJogo">Inicia</button>
    <button v-on:click="pausaJogo">Pausar</button>
    <button v-on:click="reiniciaTudo">Resetar</button>
    <tabuleiro-canvas ref="TabuleiroCanvas"></tabuleiro-canvas>
  </div>
</template>

<script>
import TabuleiroCanvas from "./components/TabuleiroCanvas.vue";

export default {
  data() {
    return {
      x: 0,
      y: 0,
      jogando: false,
    };
  },
  components: {
    TabuleiroCanvas,
  },
  methods: {
    localizaMouse(event) {
      if (!this.jogando) {
        const canvas = document.getElementById("canvas");
        const bounding = canvas.getBoundingClientRect();
        this.x = Math.floor((event.clientX - bounding.left) / 50);
        this.y = Math.floor((event.clientY - bounding.top) / 50);
        this.$refs.TabuleiroCanvas.pintaQuadrado(this.x, this.y);
      }
    },
    iniciaJogo() {
      this.jogando = true;
      this.$refs.TabuleiroCanvas.logicaJogo(this.jogando);
    },
    pausaJogo() {
      this.jogando = false;
      this.$refs.TabuleiroCanvas.logicaJogo(this.jogando);
    },
    reiniciaTudo() {
      this.jogando = false;
      this.$refs.TabuleiroCanvas.reseta(true);
    },
  },
  mounted() {
    const canvas = document.getElementById("canvas");
    canvas.addEventListener("click", (event) => this.localizaMouse(event));
  },
};
</script>

<style>
.container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 50px;
}
</style>
