<template>
  <div class="resolution-standards">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Resolution Standards</h1>

          <h2>Sneakbike Standard Aspect Ratio</h2>
          <p>
            <b>
              <span
                style="font-size: 1.2rem; color: red;"
              >ALL SNEAKBIKE GAMES SHOULD BE RUN AT 8:7 ASPECT RATIO.</span>
            </b>
          </p>

          <p>
            The size of the screen may vary, but the runners can use
            <b>544x476</b> as a starting point.
          </p>

          <info-card>
            This is due to the ease of setting a standard
            <b>aspect ratio</b> (AR) on a number of emulators, and because our overlays often have static sizes, we prefer to set all of our games, if possible, to the same AR.
          </info-card>

          <h2>Standard Resolution Reference.</h2>

          <v-btn depressed @click="showReference = !showReference">Show/Hide Reference</v-btn>

          <div v-show="showReference">
            <warning-card>
              These resolutions are simply for reference and NOT to be used unless the above does not work for some reason. You should have a
              <i>very good reason</i> to deviate from the standard resolution above.
            </warning-card>

            <p>
              Below are the standard resolutions for our consoles. These can be
              used for:
            </p>

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
              <b>Good Starting Size</b> is a nice border size to start with when
              using Streamelements. You may have to resize it a bit, but it's a
              good initial size to iterate on.
            </info-card>

            <warning-card>
              N64 games tend to have different resolutions, these should probably
              be looked at individually.
            </warning-card>
          </div>
        </v-col>
        <v-col />
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
  { console: "NES", resolution: "16:15", goodStartingSize: "512x480" },
  { console: "SNES", resolution: "8:7", goodStartingSize: "544x476" },
  { console: "Genesis", resolution: "10:7", goodStartingSize: "640x448" },
  { console: "N64", resolution: "17:12*", goodStartingSize: "680x480*" },
];

export default {
  name: "ResolutionStandards",
  data() {
    return { headers, rows, showReference: false };
  },
};
</script>
