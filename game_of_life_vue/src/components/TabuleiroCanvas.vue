<template>
  {{ dias }}
  <canvas id="canvas" width="500" height="500"></canvas>
</template>

<script>
export default {
  data() {
    return {
      jogando: Boolean,
      quadradosPintados: [[], [], [], [], [], [], [], [], [], []],
      vaiMorrer: [[], [], [], [], [], [], [], [], [], []],
      vaiNascer: [[], [], [], [], [], [], [], [], [], []],
      dias: 0,
    };
  },
  methods: {
    logicaJogo(jogando) {
      this.jogando = jogando;
      if (jogando) {
        for (var y in this.quadradosPintados) {
          var linha = Number(y);
          if (this.quadradosPintados[linha].length > 0) {
            for (var x in this.quadradosPintados[linha]) {
              var coluna = this.quadradosPintados[linha][x];
              var vizinhos = this.contaVizinhos(linha, coluna);
              this.verificaSeNasce(linha, coluna);
              if (vizinhos <= 1 || vizinhos >= 4) {
                this.vaiMorrer[linha].push(coluna);
              }
            }
          }
        }
        for (var morre in this.vaiMorrer) {
          if (this.vaiMorrer[morre].length > 0) {
            var linhaMorre = Number(morre);
            for (var z in this.vaiMorrer[morre]) {
              var colunaMorre = this.vaiMorrer[morre][z];
              this.mataCelula(linhaMorre, colunaMorre);
            }
          }
        }
        for (var nasce in this.vaiNascer) {
          if (this.vaiNascer[nasce].length > 0) {
            var linhaNasce = Number(nasce);
            for (var n in this.vaiNascer[nasce]) {
              var colunaNasce = this.vaiNascer[nasce][n];
              this.criaCelula(linhaNasce, colunaNasce);
            }
          }
        }
        console.log(this.quadradosPintados);
        this.reseta(false);
        setTimeout(() => {
          this.logicaJogo(this.jogando);
        }, 1500);
      }
    },
    desenhaTabuleiro() {
      const ctx = document.getElementById("canvas").getContext("2d");
      for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
          ctx.strokeStyle = "rgb(157,157,157, 128)";
          ctx.strokeRect(j * 50, i * 50, 50, 50);
        }
      }
    },
    pintaQuadrado(x, y) {
      if (this.quadradosPintados[x].includes(y)) {
        this.mataCelula(x, y);
      } else {
        this.criaCelula(x, y);
      }
    },
    mataCelula(linha, coluna) {
      const ctx = document.getElementById("canvas").getContext("2d");
      ctx.clearRect(linha * 50, coluna * 50, 50, 50);
      ctx.strokeStyle = "rgb(157, 157, 157, 128)";
      ctx.strokeRect(linha * 50, coluna * 50, 50, 50);
      var indice = this.quadradosPintados[linha].indexOf(coluna);
      this.quadradosPintados[linha].splice(indice, 1);
    },
    criaCelula(linha, coluna) {
      const ctx = document.getElementById("canvas").getContext("2d");
      ctx.fillStyle = "rgb(0, 0, 0, 128)";
      ctx.fillRect(linha * 50, coluna * 50, 50, 50);
      ctx.strokeStyle = "rgb(157,157,157, 128)";
      ctx.strokeRect(linha * 50, coluna * 50, 50, 50);
      this.quadradosPintados[linha].push(coluna);
    },
    contador(linha, coluna, vizinhos) {
      if (this.quadradosPintados[linha].includes(coluna)) {
        vizinhos++;
      }
      return vizinhos;
    },
    contaVizinhos(linha, coluna) {
      var vizinhos = 0;
      vizinhos = this.contador(linha, coluna + 1, vizinhos);
      vizinhos = this.contador(linha, coluna - 1, vizinhos);
      if (linha - 1 < 0) {
        vizinhos = this.contador(linha + 1, coluna + 1, vizinhos);
        vizinhos = this.contador(linha + 1, coluna - 1, vizinhos);
        vizinhos = this.contador(linha + 1, coluna, vizinhos);
      } else if (linha + 1 > 4) {
        vizinhos = this.contador(linha - 1, coluna + 1, vizinhos);
        vizinhos = this.contador(linha - 1, coluna - 1, vizinhos);
        vizinhos = this.contador(linha - 1, coluna, vizinhos);
      } else {
        vizinhos = this.contador(linha + 1, coluna + 1, vizinhos);
        vizinhos = this.contador(linha + 1, coluna - 1, vizinhos);
        vizinhos = this.contador(linha + 1, coluna, vizinhos);
        vizinhos = this.contador(linha - 1, coluna + 1, vizinhos);
        vizinhos = this.contador(linha - 1, coluna - 1, vizinhos);
        vizinhos = this.contador(linha - 1, coluna, vizinhos);
      }
      return vizinhos;
    },
    verificador(linha, coluna) {
      if (!this.quadradosPintados[linha].includes(coluna)) {
        if (this.contaVizinhos(linha, coluna) == 3) {
          this.vaiNascer[linha].push(coluna);
        }
      }
      return;
    },
    verificaSeNasce(linha, coluna) {
      if (linha - 1 < 0) {
        this.verificador(linha + 1, coluna);
        if (coluna + 1 < 4) {
          this.verificador(linha, coluna + 1);
        }
        if (coluna - 1 >= 0) {
          this.verificador(linha, coluna - 1);
          this.verificador(linha + 1, coluna - 1);
        }
      } else if (linha + 1 > 4) {
        this.verificador(linha - 1, coluna);
        if (coluna - 1 >= 0) {
          this.verificador(linha, coluna - 1);
          this.verificador(linha - 1, coluna - 1);
        }
        if (coluna + 1 < 9) {
          this.verificador(linha, coluna + 1);
          this.verificador(linha - 1, coluna + 1);
        }
      } else {
        this.verificador(linha - 1, coluna);
        this.verificador(linha + 1, coluna);
        if (coluna - 1 < 0) {
          this.verificador(linha + 1, coluna + 1);
          this.verificador(linha - 1, coluna + 1);
          this.verificador(linha, coluna + 1);
        } else if (coluna + 1 > 4) {
          this.verificador(linha + 1, coluna - 1);
          this.verificador(linha - 1, coluna - 1);
          this.verificador(linha, coluna - 1);
        } else {
          this.verificador(linha + 1, coluna + 1);
          this.verificador(linha + 1, coluna - 1);
          this.verificador(linha - 1, coluna + 1);
          this.verificador(linha - 1, coluna - 1);
          this.verificador(linha, coluna + 1);
          this.verificador(linha, coluna - 1);
        }
      }
      return;
    },
    reseta(repete) {
      console.log(this.vaiNascer);
      this.vaiMorrer = [[], [], [], [], [], [], [], [], [], []];
      this.vaiNascer = [[], [], [], [], [], [], [], [], [], []];
      this.dias += 1;
      if (repete) {
        this.dias = 0;
        this.quadradosPintados = [[], [], [], [], [], [], [], [], [], []];
        const ctx = document.getElementById("canvas").getContext("2d");
        ctx.reset();
        this.desenhaTabuleiro();
      }
    },
  },
  mounted() {
    this.desenhaTabuleiro();
  },
};
</script>
<style scoped>
canvas {
  border: 1px solid rgb(157, 157, 157, 128);
}
</style>
