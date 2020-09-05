<template>
  <div class="emulator-setup">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>BizHawk Emulator Config</h1>
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>

    <v-parallax src="@/assets/bkgd_excitebike_cropped.jpg" height="250" />

    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <info-card
            >If you'd rather see the video of the config, check our
            <a href="https://youtu.be/J_WM3zYQVH0">video tutorial</a
            >.</info-card
          >

          <p>We'll need to configure three things in BizHawk.</p>
          <ul>
            <li>Hotkeys</li>
            <li>Display</li>
            <li>Sound</li>
          </ul>

          <p>
            Each of these items can be found in the <code>Config</code> menu at
            the top. The screenshots below show you what each screen should look
            like.
            <i
              >For the Sound menu, if you uncheck the box we've circled in red,
              this will mute the emulator.</i
            >
          </p>

          <img src="@/assets/console_config/emuhawk_hotkeys_config.png" />
          <img src="@/assets/console_config/emuhawk_SNES_display_config.png" />
          <img src="@/assets/console_config/emuhawk_sound_config.png" />
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "EmulatorSetup",
};
</script>
