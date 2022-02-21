<template>
  <div class="cell container">
    <img :src="img_url">
    <a :href="'/anime?anime_id=' + id">
      <p>{{ japanese_title }} (TV)</p>
      <p>{{ title }}</p>
    </a>
    <hr>
    <p>{{ genres }}</p>
    <p>{{ abtests() }}</p>
  </div>
</template>

<script>
export default {
  props: ['id', 'japanese_title', 'title', 'img_url', 'genres', 'ab_recall', 'ab_rank'],
  data () {
    return {
    }
  },
  methods: {
    abtests () {
      return `recall : ${this.ab_recall}, rank : ${this.ab_rank}`
    }
  }
}
</script>

<style>
.cell {
  border: 1px solid pink;
  border-radius: 12px;
  padding: 1em;
  width: 306px;
  height: 528px;
  margin-bottom: 20px;
}
p {
  margin-bottom: 0;
}
img {
  width: 225px;
  height: 320px;
}
</style>
