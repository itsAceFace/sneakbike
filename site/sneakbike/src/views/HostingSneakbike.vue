<template>
  <div class="hosting-sneakbike">
    <h1 id="hosting-sneakbike">Hosting Sneakbike</h1>
    <p>If you'd like to host Sneakbike or something like Sneakbike, you'll need a hosting service (we use AWS) and a broadcasting service (like OBS) to stream. In this tutorial, we'll go over how to host something like Sneakbike on AWS and how to access the RTMP stream locally using VLC. If you'd like to access the stream via OBS, you're in luck: OBS has a built in VLC Capture Source which you can use the same way you use VLC. For this tutorial, therefore, we'll simplify and use VLC.</p>

    <p>
      Since much of this is covered in
      <router-link to="./devops">devops</router-link>we will link to that when appropriate.
    </p>

    <br />
    <br />
    <h2 id="aws">AWS</h2>
    <!-- Todo: finish this -->

    1. get AWS
    2. go to EC2
    3. pick out instance, our EC2 instance is currently an Ubuntu 18.04 t3a.micro
    4. copy the user script (or just upload the file)
    5. make a security group with rtmp
    6. test this thing out
    7. costs and cost explorer
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
export default {
  name: "Devops"
};
</script>
