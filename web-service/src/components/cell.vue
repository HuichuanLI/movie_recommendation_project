<template>
  <div class="cell container">
    <img :src="img_url">
    <a :href="'/anime?anime_id=' + id">
      <p>{{ japanese_title }} (TV)</p>
      <p>{{ title }}</p>
    </a>
    <hr>
    <p>{{ genres }}</p>
  </div>
</template>

<script>
export default {
  props: ['id', 'japanese_title', 'title', 'img_url', 'genres'],
  data () {
    return {

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
