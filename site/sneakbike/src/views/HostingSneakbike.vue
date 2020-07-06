<template>
  <div class="hosting-sneakbike">
    <h1 id="hosting-sneakbike">Hosting Sneakbike</h1>
    <p>
      <b>NOT COMPLETE.</b>
    </p>
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
        <v-card-subtitle>
          <span v-html="step" />
        </v-card-subtitle>
        <hr />
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
  "Get an AWS Account. Once you are signed in, find <code>EC2</code> under the <code>Compute</code> heading.",
  "In the upper-right hand corner, make sure your location is set to <code>US East (N. Virginia)</code>.  This is the default location for most AWS things, you'll want to stick here.",
  "In the EC2 dashboard, click <code>Instances</code> on the left side and then <code>Launch Instance</code> in the middle of the screen.",
  "Choose the <code>Ubuntu Server 18.04 LTS (HVM) SSD Volume Type</code>.",
  "Choose to filter by <code>General Purpose</code>, then select the <code>t3a.micro</code> instance which should have 2 vCPUs and 1GiB memory.",
  "Click <code>Configure Instance Details</code> in the lower-right hand corner.",
  "Don't change anything on the next steps until you reach the <code>Configure Security Group</code> screen.",
  "You will need to create a new security group if this is your first time, or use an existing one if you've done it before.  For a new group, add a rule for the following two rules: <br/><br/> <code>SSH - TCP - 22 - Anywhere</code><br/><br/><code>Custom TCP - TCP - 1935 - Anywhere</code>",
  "Click <code>Launch Instance</code>.  We will need to SSH into the machine (to talk to our cloud computer).  It will bring up a key pair dialog which looks like the below figure.  If you've never done this, you can download the key pair; otherwise, you can re-use an old key pair that you've created before.",
  "After you click 'Launch Instance' on your key pair screen, click 'View Instances' to go back to your EC2 dashboard. <br/><br/><b style='color: red;'>NOTE: AT THIS POINT, THE INSTANCE IS LAUNCHED.  AS ABOVE, YOU WILL WANT TO TERMINATE THIS WHEN YOU ARE DONE.  SEE THE LAST STEP BELOW.</b>",
  "At the dashboard, you should see your instance.  The <code>Public IP</code> circled below is what you'll SSH into the EC2 instance with.",
  "At this point, if you're on Windows, you'll need to get an SSH client: the standard client is PuTTY.  The instructions <a href='https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html' alt='aws putty instructions'>at the AWS docs site</a> are great for getting this up and running. You should do the sections up to and including <code>Connecting to your Linux instance</code>.<br/><br/>This is one of those irritating things you have to do to make Windows work with things."
];
export default {
  name: "HostingSneakbike",
  data() {
    return { steps };
  }
};
</script>
