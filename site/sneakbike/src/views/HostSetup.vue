<template>
  <div class="host-setup">
    <v-container>
      <v-row justify="center">
        <v-col cols="2"/>
        <v-col cols="8">
          <h1>Hosting Sneakbike on OBS</h1>

          <p>
            Once the server is set up (see:
            <router-link to="/dev-setup">dev setup</router-link>), you're ready
            to pull data into OBS and start streaming it!
          </p>

          <ol>
            <li>
              Download the
              <a
                href="https://drive.google.com/drive/folders/1VKHZobAXgSsdrHUHxVaAmiPInTEaeO-I?usp=sharing"
                target="_blank"
                ><code>Sneakbike_Ops.zip</code> profile</a
              >.
              <ul>
                <li>
                  Feel free to also download the Scene Collection
                  <code>Sneakbike_Ops.json</code> for examples of scenes.
                </li>
              </ul>
            </li>
            <li>
              Import the Sneakbike_Ops into OBS
              <ul>
                <li>
                  For instructions on importing, see
                  <router-link to="/runner-setup">Runner Setup</router-link>
                </li>
              </ul>
            </li>
            <li>
              To get a runner's RTMP stream, choose the
              <code>VLC Video Source</code>, add their RTMP address, and use
              "Always Play Even When Not Visible"
              <ul>
                <li>
                  The address should look something like
                  <code>rtmp://the_ec2_ip:1935/live/the_runner_key</code>
                </li>
                <li>
                  Sometimes this takes a minute to come up, don't worry if it
                  doesn't start up right away
                </li>
                <li>
                  If things really aren't working, remove the scene and try to
                  add it again
                </li>
              </ul>
            </li>
            <li>
              Create your scene however you'd like with an overlay, background,
              etc.
            </li>
          </ol> </v-col
        ><v-col></v-col></v-row
    ></v-container>
  </div>
</template>

<script>
export default {
  name: "HostSetup",
};
</script>
