<template>
  <div class="resolution-standards">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Resolution Standards</h1>
          <warning-card>Please do not deviate from these resolutions unless you know what you're doing.</warning-card>
          <p>Below are the standard resolutions for our consoles. These can be used for:</p>

          <ul>
            <li>Runner Emulator Display configuration.</li>
            <li>Creation of bounding boxes in overlays.</li>
          </ul>
          <br />
          <v-data-table
            dense
            hide-default-footer
            :headers="headers"
            :items="rows"
            class="elevation-1"
          ></v-data-table>
          <br />
          <info-card>
            The
            <b>Good Starting Size</b> is a nice border size to start with when using Streamelements. You may have to resize it a bit, but it's a good initial size to iterate on.
          </info-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
const headers = [
  {
    text: "Console",
    align: "start",
    sortable: false,
    value: "console",
  },
  {
    text: "Resolution",
    align: "center",
    sortable: false,
    value: "resolution",
  },
  {
    text: "Good Starting Size",
    align: "center",
    sortable: false,
    value: "goodStartingSize",
  },
];

const rows = [
  { console: "NES", resolution: "TODO", goodStartingSize: "TODO" },
  { console: "SNES", resolution: "8:7", goodStartingSize: "544x476" },
  { console: "Genesis", resolution: "TODO", goodStartingSize: "TODO" },
];

export default {
  name: "ResolutionStandards",
  data() {
    return { headers, rows };
  },
};
</script>
