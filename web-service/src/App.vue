<template>
  <div>
    <div v-if="!animePage">
      <h1>Concrec 动漫推荐系统</h1>
      <h3>猜你喜欢:</h3>
      <button v-on:click="loadItems" type="button" class="btn btn-info">刷新</button>
    </div>

    <div v-else>
      <anime
        :id="currentAnime.anime_id"
        :japanese_title="currentAnime.japanese_title"
        :title="currentAnime.name"
        :img_url="currentAnime.image_url"
        :genres="currentAnime.genre"
        :aired="currentAnime.aired"
        :rating="currentAnime.rating"
        :members="currentAnime.members"
      >
      </anime>
      <br>
      <h3>相似推荐:</h3>
    </div>

    <div class="container cell-grid">

      <div v-for="group in itemsGroup" :key="group" class="row">
        <div v-for="item in group" :key="item" class="col">
          <cell
            :id="item.anime_id"
            :japanese_title="item.anime.japanese_title"
            :title="item.anime.name"
            :img_url="item.anime.image_url"
            :genres="item.anime.genre"
            :ab_recall="item['ab:recall']"
            :ab_rank="item['ab:rank']"
          >
          </cell>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Cell from './components/cell.vue'
import Anime from './components/anime.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'App',
  components: {
    Cell,
    Anime
  },
  data () {
    return {
      items: [],
      currentAnime: {}
    }
  },
  computed: {
    itemsGroup () {
      return _.chunk(this.items, 4)
    },
    animePage () {
      const path = window.location.pathname
      return path === '/anime'
    }
  },
  async created () {
    if (this.animePage) {
      await this.loadCurrentAnime()
    }
    await this.loadItems()
  },
  methods: {
    async loadItems () {
      const userId = this.getUserId()
      const animeId = this.getAnimeId()
      let url = 'http://localhost:15003/'
      if (!this.animePage) {
        url = `${url}?user_id=${userId}`
      } else {
        url = `${url}sim?anime_id=${animeId}`
      }
      const res = await axios.get(url)
      this.items = res.data
    },
    async loadCurrentAnime () {
      const animeId = this.getAnimeId()
      const url = `http://localhost:15003/anime/${animeId}`
      const res = await axios.get(url)
      this.currentAnime = res.data
    },
    getUserId () {
      const params = new URLSearchParams(window.location.search)
      return params.get('user_id')
    },
    getAnimeId () {
      const params = new URLSearchParams(window.location.search)
      return params.get('anime_id')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.cell-grid {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>