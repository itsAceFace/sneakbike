# Runner Setup

This guide should take you through everything you need to do to be a Sneakbike Runner!

- [Runner Setup](#runner-setup)
  - [Step 0: Backing Everything Up For Safety](#step-0--backing-everything-up-for-safety)
  - [Step 1: Necessary Software](#step-1--necessary-software)
  - [Step 2: Install Bizhawk](#step-2--install-bizhawk)
  - [Step 3: Download this Repository](#step-3--download-this-repository)
  - [Step 4. Import things into OBS](#step-4-import-things-into-obs)
    - [Importing a Profile](#importing-a-profile)
    - [Importing Scenes](#importing-scenes)
  - [Emulator Setup](#emulator-setup)
    - [Bizhawk](#bizhawk)

---

---

## Step 0: Backing Everything Up For Safety

_If you're dowloading OBS for the first time, you can skip this section._

If you've already been using OBS, it's better to be safe than sorry. We'll back up your major things:

1. Go to `Profile > Export`. Save your profile in a safe place. It wants you to pick a folder, just pick whatever you want and it'll make its own folder inside of it.

   ![Obs Profile Export](../static/images/obs_export_profile.PNG)

   - You can re-import your profile if something goes wrong.
   - Don't worry, this hasn't happened to me yet.

2. Go to `Scene Collection > Export`. Save your scene collection in a safe place.

   ![Obs Scene Collection Export](../static/images/obs_export_scene_collection.PNG)

   - You can re-import your scenes if something goes wrong.
   - Don't worry, this hasn't happened to me yet either.

---

---

## Step 1: Necessary Software

For a consistent experience, we use the following:

<!-- 1. A recent version of `Retroarch` (currently v1.8.8)

   - [Windows Download](http://buildbot.libretro.com/stable/1.8.8/windows/x86_64/RetroArch-x64-setup.exe)
   - **TODO: Mac**
   - **TODO: Linux**

2. The following `Retroarch cores` by opening Retroarch and clicking `Load Core > Download Core` and picking the following:

   - Nintendo - Game Boy / Color (Gambatte)
   - Nintendo - Game Boy Advance (mGBA)
   - Nintendo - NES / Famicom (Mesen)
   - Nintendo - SNES / SFC (Snes9x)
   - Sega MS/GG/MD/CD (Genesis Plus GX) -->

1. Recent version of Bizhawk and Bizhawk Prereqs.

   - Windows [Bizhawk](https://github.com/TASVideos/BizHawk/releases/download/2.4.2/BizHawk-2.4.2.zip) and [Bizhawk Prereqs](https://github.com/TASVideos/BizHawk-Prereqs/releases/download/2.4.8_1/bizhawk_prereqs_v2.4.8_1.zip)

2. Fairly recent version of `OBS` (currently 25.0.8)
   - [Windows Download](https://cdn-fastly.obsproject.com/downloads/OBS-Studio-25.0.8-Full-Installer-x64.exe)
   - **TODO: Mac**
   - **TODO: Linux**

---

---

## Step 2: Install Bizhawk

1. Unzip Bizhawk and Bizhawk Prereqs folder that you downloaded above.
2. Go into the unzipped Bizhawk Prereqs folder and double-click `bizhawk_prereqs` to run the exe. It should take you to a typical installer. Install the prereqs.
3. Go into the unzipped Bizhawk folder and double-click `EmuHawk` to run the emulator. It should run without error.

That's it for Bizhawk! When running games, you'll need to run `EmuHawk`, the Bizhawk emulator. To set up this emulator to play, read the section below on [Setting Up Your Emulator](#bizhawk).

## Step 3: Download this Repository

1. Go to "Clone or Download" on this webpage and download the zip file of this repository.
2. Unzip it when it's done downloading.

   ![Github Download](../static/images/github_clone.PNG)

---

---

## Step 4. Import things into OBS

There are two things we need to import, Scenes and a Profile.

### Importing a Profile

1. In OBS, go to `Profile > Import`, click the `Sneakbike_Profile` folder from the unzipped repository.

   ![OBS Profile Import](../static/images/obs_import_profile.PNG)

2. If you click `Profile` again, you should see (probably) two profiles at the bottom: `Untitled` and `Sneakbike`. `Untitled` is your default. You can switch back to `Untitled` to go back to your normal streaming profile.

### Importing Scenes

1. In OBS, go to `Scene Collection > Import`, click the `...` button and find the `snakebike_scenes.json` file in the unzipped folder.

   ![OBS Scene Collection Import](../static/images/obs_import_scene_collection.PNG)

2. Click `Import`.
3. If you go into `Scene Collection` again, you should see (probably) two scenes at the bottom: `Untitled` and `Sneakbike`. `Untitled` is your default scenes. You can switch back to `Untitled` to get back to your default scenes.
   - Try switching between the two and you'll get the gist of what's happening.

**We'll be using the `Sneakbike` profile with the `Sneakbike` scenes for these races.**

---

---

## Emulator Setup

For each emulator there are a few nice things to set up.

### Bizhawk

- **IMPORTANT: Disable Start Button for Fast-Forward**: `Config > Configure Hotkeys > Click the box next to "Fast Forward" and hit the Tab keyboard key`.

  - This should change the box to say "Tab", as in the image below.
  - This is important since otherwise the start button will ALSO fast-forward your game.

  ![Bizhawk Hotkey Turbo Fix](../static/images/bizhawk_hotkeys_turbo.PNG)

* **Adjust Volume**: `Config > Sound > Adjust on the left-hand-size`.
* **Controller Setup**:
  - Open a ROM for that system (any game should work) then go to `Config > Controllers`.
  - You should be able to click next to the command and press the associated button on your controller.

---

---

That's all ! Check out the [runner_resources](./runner_resources.md) doc to see what we'll be telling you to do on race day!
