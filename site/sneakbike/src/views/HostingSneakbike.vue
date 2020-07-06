<template>
  <div class="hosting-sneakbike">
    <h1 id="hosting-sneakbike">Hosting Sneakbike</h1>
    <p>If you'd like to host Sneakbike or something like Sneakbike, you'll need a hosting service (we use AWS) and a broadcasting service (like OBS) to stream. In this tutorial, we'll go over how to host something like Sneakbike on AWS and how to access the RTMP stream locally using VLC. If you'd like to access the stream via OBS, you're in luck: OBS has a built in VLC Capture Source which you can use the same way you use VLC. For this tutorial, therefore, we'll simplify and use VLC.</p>

    <p>
      Since much of this is covered in
      <router-link to="./devops">devops</router-link>&nbsp;we will link to that when appropriate.
    </p>

    <br />
    <br />
    <h2 id="aws">AWS</h2>

    <v-alert type="error">
      After spinning up an EC2 instance, remember to
      <b>terminate</b> it when you're done! (We'll cover this below.)
    </v-alert>

    <div v-for="(step, index) in steps" :key="`step-${index}`">
      <v-card class="mx-auto" max-width="600px">
        <v-card-title>Step {{index + 1}}.</v-card-title>
        <v-card-subtitle>{{step}}</v-card-subtitle>
        <v-img
          class="white--text align-end"
          width="600px"
          :src="require(`@/assets/images/hosting_sneakbike_${index + 1}.png`)"
        />
      </v-card>
      <br />
      <br />
    </div>

    <br />
    <br />
    <h2 id="getting-data-from-the-rtmp-server">Getting Data from the RTMP Server</h2>
    <p>
      Since this is nearly identical, see the "Getting Data From the RTMP Server" section in
      <router-link to="./devops">devops</router-link>.
    </p>
  </div>
</template>

<script>
const steps = [
  'Get an AWS Account. Once you are signed in, find "EC2" under the "Compute" heading.',
  "In the upper-right hand corner, make sure your location is set to US East (N. Virginia).  This is the 'default' location for most AWS things, you'll want to stick here.",
  "In the EC2 dashboard, click 'Instances' on the left side and then 'Launch Instance' in the middle of the screen.",
  "Choose the Ubuntu Server 18.04 LTS (HVM) SSD Volume Type.",
  "Choose to filter by 'General Purpose', then select the 't3a.micro' instance which should have 2 vCPUs and 1GiB memory.",
  "Click 'Configure Instance Details' in the lower-right hand corner.",
  "Don't change anything on the next steps until you reach the 'Configure Security Group' screen.",
  "You will need to 'Create a NEW security Group' if this is your first time, or use an existing one if you've done it before.  For a new group, add a rule for 'SSH - TCP - 22 - Anywhere' and 'Custom TCP - TCP - 1935 - Anywhere'.",
  "Click 'Launch Instance'.  We will need to SSH into the machine (to talk to our cloud computer).  It will bring up a key pair dialog which looks like the above figure.  If you've never done this, you can download the key pair; otherwise, you can re-use an old key pair that you've created before."
];
export default {
  name: "HostingSneakbike",
  data() {
    return { steps };
  }
};
</script>
