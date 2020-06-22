<template>
  <div class="about">
    <h1 id="runner-setup">Runner Setup</h1>
    <p>This guide should take you through everything you need to do to be a Sneakbike Runner!</p>
    <ul>
      <li>
        <a href="#runner-setup">Runner Setup</a>
        <ul>
          <li>
            <a
              href="#step-0--backing-everything-up-for-safety"
            >Step 0: Backing Everything Up For Safety</a>
          </li>
          <li>
            <a href="#step-1--necessary-software">Step 1: Necessary Software</a>
          </li>
          <li>
            <a href="#step-2--install-bizhawk">Step 2: Install Bizhawk</a>
          </li>
          <li>
            <a href="#step-3--download-this-repository">Step 3: Download this Repository</a>
          </li>
          <li>
            <a href="#step-4-import-things-into-obs">Step 4. Import things into OBS</a>
            <ul>
              <li>
                <a href="#importing-a-profile">Importing a Profile</a>
              </li>
              <li>
                <a href="#importing-scenes">Importing Scenes</a>
              </li>
            </ul>
          </li>
          <li>
            <a href="#emulator-setup">Emulator Setup</a>
            <ul>
              <li>
                <a href="#bizhawk">Bizhawk</a>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
    <br />
    <br />
    <h2 id="step-0-backing-everything-up-for-safety">Step 0: Backing Everything Up For Safety</h2>
    <p>
      <em>If you're dowloading OBS for the first time, you can skip this section.</em>
    </p>
    <p>If you've already been using OBS, it's better to be safe than sorry. We'll back up your major things:</p>
    <ol>
      <li>
        <p>
          Go to
          <code>Profile > Export</code>. Save your profile in a safe place. It wants you to pick a folder, just pick whatever you want and it'll make its own folder inside of it.
        </p>
        <p>
          <img src="../static/images/obs_export_profile.png" alt="Obs Profile Export" />
        </p>
        <ul>
          <li>You can re-import your profile if something goes wrong.</li>
          <li>Don't worry, this hasn't happened to me yet.</li>
        </ul>
      </li>
      <li>
        <p>
          Go to
          <code>Scene Collection > Export</code>. Save your scene collection in a safe place.
        </p>
        <p>
          <img
            src="../static/images/obs_export_scene_collection.png"
            alt="Obs Scene Collection Export"
          />
        </p>
        <ul>
          <li>You can re-import your scenes if something goes wrong.</li>
          <li>Don't worry, this hasn't happened to me yet either.</li>
        </ul>
      </li>
    </ol>
    <br />
    <br />
    <h2 id="step-1-necessary-software">Step 1: Necessary Software</h2>
    <p>For a consistent experience, we use the following:</p>
    <ol>
      <li>
        <p>Recent version of Bizhawk and Bizhawk Prereqs.</p>
        <ul>
          <li>
            Windows
            <a
              href="https://github.com/TASVideos/BizHawk/releases/download/2.4.2/BizHawk-2.4.2.zip"
            >Bizhawk</a> and
            <a
              href="https://github.com/TASVideos/BizHawk-Prereqs/releases/download/2.4.8_1/bizhawk_prereqs_v2.4.8_1.zip"
            >Bizhawk Prereqs</a>
          </li>
        </ul>
      </li>
      <li>
        <p>
          Fairly recent version of
          <code>OBS</code> (currently 25.0.8)
        </p>
        <ul>
          <li>
            <a
              href="https://cdn-fastly.obsproject.com/downloads/OBS-Studio-25.0.8-Full-Installer-x64.exe"
            >Windows Download</a>
          </li>
          <li>
            <strong>TODO: Mac</strong>
          </li>
          <li>
            <strong>TODO: Linux</strong>
          </li>
        </ul>
      </li>
    </ol>
    <br />
    <br />
    <h2 id="step-2-install-bizhawk">Step 2: Install Bizhawk</h2>
    <ol>
      <li>Unzip Bizhawk and Bizhawk Prereqs folder that you downloaded above.</li>
      <li>
        Go into the unzipped Bizhawk Prereqs folder and double-click
        <code>bizhawk_prereqs</code> to run the exe. It should take you to a typical installer. Install the prereqs.
      </li>
      <li>
        Go into the unzipped Bizhawk folder and double-click
        <code>EmuHawk</code> to run the emulator. It should run without error.
      </li>
    </ol>
    <p>
      That's it for Bizhawk! When running games, you'll need to run
      <code>EmuHawk</code>, the Bizhawk emulator. To set up this emulator to play, read the section below on
      <a
        href="#bizhawk"
      >Setting Up Your Emulator</a>.
    </p>
    <h2 id="step-3-download-this-repository">Step 3: Download this Repository</h2>
    <ol>
      <li>Go to "Clone or Download" on this webpage and download the zip file of this repository.</li>
      <li>
        <p>Unzip it when it's done downloading.</p>
        <p>
          <img src="../static/images/github_clone.png" alt="Github Download" />
        </p>
      </li>
    </ol>
    <br />
    <br />
    <h2 id="step-4-import-things-into-obs">Step 4. Import things into OBS</h2>
    <p>There are two things we need to import, Scenes and a Profile.</p>
    <h3 id="importing-a-profile">Importing a Profile</h3>
    <ol>
      <li>
        <p>
          In OBS, go to
          <code>Profile > Import</code>, click the
          <code>Sneakbike_Profile</code> folder from the unzipped repository.
        </p>
        <p>
          <img src="../static/images/obs_import_profile.png" alt="OBS Profile Import" />
        </p>
      </li>
      <li>
        <p>
          If you click
          <code>Profile</code> again, you should see (probably) two profiles at the bottom:
          <code>Untitled</code> and
          <code>Sneakbike</code>.
          <code>Untitled</code> is your default. You can switch back to
          <code>Untitled</code> to go back to your normal streaming profile.
        </p>
      </li>
    </ol>
    <h3 id="importing-scenes">Importing Scenes</h3>
    <ol>
      <li>
        <p>
          In OBS, go to
          <code>Scene Collection > Import</code>, click the
          <code>...</code> button and find the
          <code>snakebike_scenes.json</code> file in the unzipped folder.
        </p>
        <p>
          <img
            src="../static/images/obs_import_scene_collection.png"
            alt="OBS Scene Collection Import"
          />
        </p>
      </li>
      <li>
        <p>
          Click
          <code>Import</code>.
        </p>
      </li>
      <li>
        If you go into
        <code>Scene Collection</code> again, you should see (probably) two scenes at the bottom:
        <code>Untitled</code> and
        <code>Sneakbike</code>.
        <code>Untitled</code> is your default scenes. You can switch back to
        <code>Untitled</code> to get back to your default scenes.
        <ul>
          <li>Try switching between the two and you'll get the gist of what's happening.</li>
        </ul>
      </li>
    </ol>
    <p>
      <strong>
        We'll be using the
        <code>Sneakbike</code> profile with the
        <code>Sneakbike</code> scenes for these races.
      </strong>
    </p>
    <br />
    <br />
    <h2 id="emulator-setup">Emulator Setup</h2>
    <p>For each emulator there are a few nice things to set up.</p>
    <h3 id="bizhawk">Bizhawk</h3>
    <ul>
      <li>
        <p>
          <strong>IMPORTANT: Disable Start Button for Fast-Forward</strong>:
          <code>Config > Hotkeys > Click the box next to "Fast Forward" and hit the Tab keyboard key</code>. Click "Save" at the bottom to save.
        </p>
        <ul>
          <li>This should change the box to say "Tab", as in the image below.</li>
          <li>This is important since otherwise the start button will ALSO fast-forward your game.</li>
        </ul>
        <p>
          <img src="../static/images/bizhawk_hotkeys_turbo.png" alt="Bizhawk Hotkey Turbo Fix" />
        </p>
      </li>
      <li>
        <p>
          <strong>Adjust Volume</strong>:
          <code>Config > Sound > Adjust on the left-hand-size</code>.
        </p>
      </li>
      <li>
        <strong>Controller Setup</strong>:
        <ul>
          <li>
            Open a ROM for that system (any game should work) then go to
            <code>Config > Controllers</code>.
          </li>
          <li>You should be able to click next to the command and press the associated button on your controller.</li>
        </ul>
      </li>
      <li>
        <strong>Make the Window Bigger</strong>: Increase the size of the window by going to
        <code>View > Window Size</code> and pick an option.
        <ul>
          <li>I usually play on 3x.</li>
        </ul>
      </li>
    </ul>
    <br />
    <br />
    <p>
      <!-- TODO: Why does this format to no space between > and d? -->
      That's all ! Check out the
      <router-link to="./runner-resources">Runner Resources</router-link>&nbsp;doc to see what we'll be telling you to do on race day!
    </p>
  </div>
</template>

<script>
export default {
  name: "RunnerSetup"
};
</script>
