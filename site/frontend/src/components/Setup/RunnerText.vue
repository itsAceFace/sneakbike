<template>
  <div class="setup-runner-text">
    <h1>Runner Setup</h1>
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

    <h2>(Optional) Backup.</h2>

    <warning-card>If you don't use OBS regularly for your streams, feel free go to Step 1 below.</warning-card>

    <p>
      If you stream with OBS, we're going to be safe and back up your OBS
      scenes and profile.
    </p>

    <img src="@/assets/setup/backup_obs.gif" />

    <p>
      Open OBS, go to
      <code>Profile > Export > (Save Somewhere)</code>, then go to
      <code>Profile > Scene Collection > (Save Somewhere)</code>.
    </p>

    <h2>1. Download Everything.</h2>

    <p>
      In order to be a runner for Sneakbike, you'll need to download a few
      things.
    </p>

    <ul>
      <li>
        <a href="https://obsproject.com/" target="_blank">OBS</a>,
      </li>
      <li>
        <a
          href="https://github.com/TASVideos/BizHawk-Prereqs/releases"
          target="_blank"
        >Bizhawk Emulator Prereqs</a>
        <ul>
          <li>
            Download the bizhawk_prereqs zip file under "Assets", unzip,
            then install.
          </li>
        </ul>
      </li>
      <li>
        <a href="https://github.com/TASVideos/BizHawk/releases" target="_blank">Bizhawk</a>
        <ul>
          <warning-card>
            There is currently an issue where Windows 10 thinks that BizHawk is a virus.
            <b>This is a false positive.</b> Try downloading
            <b>Version 2.4.2</b> if your Windows refuses to let you open the latest.
          </warning-card>
          <li>Download the BizHawk zip file under "Assets" and unzip,</li>
          <li>
            You'll find the EmuHawk emulator in the unzipped folder; this
            is the emulator we use.
          </li>
        </ul>
      </li>
      <li>
        <a
          href="https://drive.google.com/file/d/16uHzUpr4XAinq1Do_KP3-I_ptS1bJCrB/view?usp=sharing"
          target="_blank"
        >Download the Sneakbike Profile for OBS here.</a>
        <ul>
          <li>Once you've downloaded it, unzip it.</li>
        </ul>
      </li>
    </ul>

    <h2>2. Importing the Sneakbike Profile into OBS.</h2>

    <p>With OBS open:</p>
    <img src="@/assets/setup/sneakbike_import_profile.gif" alt="OBS Profile Import" />
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
      If you'd rather see the video of the config, check our
      <a
        href="https://youtu.be/J_WM3zYQVH0"
        target="_blank"
      >video tutorial</a>.
    </info-card>

    <p>We'll need to configure three things in BizHawk.</p>
    <ul>
      <li>Hotkeys</li>
      <li>Display</li>
      <li>Sound</li>
    </ul>

    <p>
      Each of these items can be found in the
      <code>Config</code> menu at
      the top. The screenshots below show you what each screen should look
      like.
      <i>
        For the Sound menu, if you uncheck the box we've circled in red,
        this will mute the emulator.
      </i>
    </p>

    <img src="@/assets/console_config/emuhawk_hotkeys_config.png" />
    <img src="@/assets/console_config/emuhawk_SNES_display_config.png" />
    <img src="@/assets/console_config/emuhawk_sound_config.png" />
  </div>
</template>

<script>
export default {
  name: "SetupRunnerText",
};
</script>