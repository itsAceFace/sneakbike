<template>
  <div class="sneakbike-info">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <iframe
            src="https://calendar.google.com/calendar/embed?height=400&amp;wkst=1&amp;bgcolor=%233f51b5&amp;ctz=America%2FChicago&amp;src=c25lYWtiaWtlQGdtYWlsLmNvbQ&amp;color=%23039BE5&amp;showNav=1&amp;showDate=1&amp;showPrint=0&amp;showCalendars=1&amp;mode=WEEK"
            style="border-width:0"
            width="600"
            height="400"
            frameborder="0"
            scrolling="no"
          ></iframe>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "SneakbikeInfo",
};
</script>
