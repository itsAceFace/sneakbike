<template>
  <div class="runner-setup">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Runner Setup</h1>
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>

    <v-parallax src="@/assets/bkgd_castlevania_intro.png" height="300" />

    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <warning-card>
            We assume you're running Windows 10. If not, check in with us and
            we'll get you compatible software.
          </warning-card>

          <info-card>
            If you'd rather see the video tutorial, that's available
            <a
              href="https://www.youtube.com/watch?v=qtB0n4RuBGo"
              target="_blank"
            >here</a>.
          </info-card>

          <h2>0. Backup (OPTIONAL)</h2>

          <warning-card>If you don't use OBS regularly for your streams, feel free go to Step 1 below.</warning-card>

          <p>
            If you stream with OBS, we're going to be safe and back up your OBS
            scenes and profile.
          </p>

          <img src="@/assets/backup_obs.gif" />

          <p>
            Open OBS, go to
            <code>Profile > Export > (Save Somewhere)</code>, then go to
            <code>Profile > Scene Collection > (Save Somewhere)</code>.
          </p>

          <h2>1. Download Everything</h2>

          <p>
            In order to be a runner for Sneakbike, you'll need to download a few
            things.
          </p>

          <ul>
            <li>
              <a href="https://obsproject.com/">OBS</a>,
            </li>
            <li>
              <a
                href="https://github.com/TASVideos/BizHawk-Prereqs/releases"
              >Bizhawk Emulator Prereqs</a>
              <ul>
                <li>
                  Download the bizhawk_prereqs zip file under "Assets", unzip,
                  then install.
                </li>
              </ul>
            </li>
            <li>
              <a href="https://github.com/TASVideos/BizHawk/releases">Bizhawk</a>
              <ul>
                <warning-card>There is currently an issue where Windows 10 thinks that BizHawk is a virus. **This is a false positive.** Try downloading **Version 2.4.2** if your Windows refuses to let you open the latest.</warning-card>
                <li>Download the BizHawk zip file under "Assets" and unzip,</li>
                <li>
                  You'll find the EmuHawk emulator in the unzipped folder; this
                  is the emulator we use.
                </li>
              </ul>
            </li>
            <li>
              <a
                href="https://drive.google.com/drive/folders/1y3iWY7Q2Hr_TE1JLlrjk70V6o3XPnwDA?usp=sharing"
                target="_blank"
              >Download the Sneakbike Profile for OBS here.</a>
              <ul>
                <li>Once you've downloaded it, unzip it.</li>
              </ul>
            </li>
          </ul>

          <h2>2. Importing the Sneakbike Profile into OBS.</h2>

          <p>With OBS open:</p>
          <img src="@/assets/sneakbike_import_profile.gif" alt="OBS Profile Import" />
          <ol>
            <li>
              Go into
              <code>Profile > Import</code>,
            </li>
            <li>Navigate to the unzipped Sneakbike folder,</li>
            <li>
              Click the
              <code>Sneakbike_Profile</code> folder and hit "open".
            </li>
            <li>
              In OBS, go into
              <code>Profile</code> again
              <ul>
                <li>
                  You should see (at least) two profiles at the bottom, including
                  <code>Sneakbike</code>
                </li>
              </ul>
            </li>
            <li>
              Clicking on
              <code>Sneakbike</code> will bring you to the Sneakbike profile we
              require.
              <ul>
                <li>
                  You can switch back to the original Profile (usually called
                  <code>Untitled</code>) to go back to your normal streaming
                  profile.
                </li>
              </ul>
            </li>
          </ol>

          <h2>3. Set up EmuHawk.</h2>
          <info-card>
            For our recommended setups for EmuHawk, check out
            <router-link to="/emulator-setup">our emulator setup page</router-link>.
          </info-card>

          <p>Remember to customize the setup for your emulator, including:</p>
          <ul>
            <li>
              Controllers
              <ul>
                <li>
                  To set up controls for a console, open any game from that
                  console and go into
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
export default {
  name: "RunnerSetup",
};
</script>

<style lang="scss">
img {
  max-width: 100%;
  padding-top: 1rem;
  padding-bottom: 1rem;
}
</style>
