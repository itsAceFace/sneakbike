<template>
  <div class="runner-setup">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Runner Setup</h1>
          <WarningCard>We assume you're running Windows 10. If not, check in with us and we'll get you compatible software.</WarningCard>
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>

    <v-parallax src="@/assets/bkgd_castlevania_intro.png" height="300" />

    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h2>1. Download.</h2>

          <p>In order to be a runner for Sneakbike, you'll need to download a few things.</p>

          <ul>
            <li>
              <a href="https://obsproject.com/">OBS</a>,
            </li>
            <li>
              <a href="https://obsproject.com/">Bizhawk Emulator Prereqs</a>
              <ul>
                <li>Download the bizhawk_prereqs zip file under "Assets", unzip, then install.</li>
              </ul>
            </li>
            <li>
              <a href="https://github.com/TASVideos/BizHawk/releases">Bizhawk</a>
              <ul>
                <li>Download the BizHawk zip file under "Assets" and unzip,</li>
                <li>You'll find the EmuHawk emulator in the unzipped folder; this is the emulator we use.</li>
              </ul>
            </li>
          </ul>

          <h2>2. Backup.</h2>

          <WarningCard>If you don't use OBS regularly for your streams, feel free to skip this part.</WarningCard>

          <p>If you stream with OBS, we're going to be safe and back up your OBS scenes and profile.</p>

          <img src="@/assets/backup_obs.gif" />

          <p>
            Open OBS, go to
            <b>Profile > Export > (Save Somewhere)</b>, then go to
            <b>Profile > Scene Collection > (Save Somewhere)</b>.
          </p>

          <h2>3. Download the Sneakbike Repository.</h2>
          <p>
            <b>TODO</b>
          </p>

          <h2>4. Importing the Sneakbike Profile into OBS.</h2>

          <p>With OBS open:</p>
          <img src="@/assets/obs_import_profile.png" alt="OBS Profile Import" />
          <ol>
            <li>
              Go into
              <code>Profile > Import</code>,
            </li>
            <li>Navigate to the unzipped Sneakbike folder,</li>
            <li>
              Navigate into the
              <code>runner_resources</code> folder,
            </li>
            <li>
              Click the
              <code>Sneakbike_Profile</code> folder and hit "open".
            </li>
            <li>
              In OBS, go into
              <code>Profile</code> again; you should see two profiles at the bottom:
              <code>Untitled</code> and
              <code>Sneakbike</code>.
            </li>
            <li>
              Clicking on
              <code>Sneakbike</code> will bring you to the Sneakbike profile we require.
              <ul>
                <li>
                  You can switch back to
                  <code>Untitled</code> to go back to your normal streaming profile.
                </li>
              </ul>
            </li>
          </ol>

          <h2>5. Set up EmuHawk.</h2>
          <InfoCard>
            For our recommended setups for EmuHawk, check out
            <router-link to="/emulator-setup">our emulator setup page</router-link>.
          </InfoCard>

          <p>Remember to customize the setup for your emulator, including:</p>
          <ul>
            <li>
              Controllers
              <ul>
                <li>
                  To set up controls for a console, open any game from that console and go into
                  <code>Config > Controllers...</code>
                </li>
              </ul>
            </li>
            <li>
              Sound (
              <code>Config > Sound...</code>)
            </li>
            <li>
              Display (
              <code>Config > Display...</code>)
            </li>
            <li>
              Window Size (
              <code>View > Window Size</code>)
            </li>
          </ul>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import WarningCard from "@/components/WarningCard.vue";
import InfoCard from "@/components/InfoCard.vue";
export default {
  name: "RunnerSetup",
  components: { WarningCard, InfoCard },
};
</script>

<style lang="scss">
img {
  max-width: 100%;
  padding-top: 1rem;
  padding-bottom: 1rem;
}
</style>
