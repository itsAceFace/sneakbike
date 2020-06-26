<template>
  <div class="devops">
    <h1 id="devops-documentation-for-sneakbike">Devops Documentation for Sneakbike</h1>
    <br />
    <br />
    <h2 id="general-architecture">General Architecture</h2>
    <img src="../static/images/sneakbike_architecture.png" alt="Sneakbike Architecture" />

    <p>
      We broadcast from several OBS applications to an
      <a
        href="https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol"
      >RTMP</a> server hosted into an EC2 box which, in turn, broadcasts to the Sneakbike OBS (currently running on an actual physical "on-prem" machine).
    </p>
    <ul>
      <li>
        Our EC2 instance is currently an Ubuntu 18.04 t3a.micro
        <ul>
          <li>Optimized for network io, not much memory required.</li>
        </ul>
      </li>
      <li>
        Our on-prem OBS for Sneakbike should be replaced by a cloud equivalent
        <ul>
          <li>(Currently researching, but it works for now)</li>
          <li>A cloud equivalent would allow more than one individual to "run" the stream, which is a good bus-clause practice.</li>
        </ul>
      </li>
      <li>The racers have to stream from their computers as no reasonable alternative exists for capturing desktop gameplay and sending it to our RTMP.</li>
    </ul>
    <br />
    <br />
    <h2 id="setting-up-obs-on-many-runners-computers">Setting up OBS on Many Runners' Computers</h2>
    <p>The most frustrating part without a doubt is getting everyone a similar setup on OBS. We require downloading the latest OBS and have them import both a Profile (to allow us to set resolution) as well as Scene Collections (to allow us to control what things go where, and to not have them confuse it with their own scene collections).</p>
    <p>Due to the nature of OBS's quick-switch for Profiles and Scenes, this works well.</p>
    <br />
    <br />
    <h2 id="server-setup-on-aws">Server Setup on AWS</h2>
    <p>
      Included in the
      <code>/scripts</code> folder is the shell file
      <code>server_setup.sh</code> which can be used as the startup script on an Ubuntu 18.04 instance.
    </p>
    <p>The tl;dr is that it installs nginx and an RTMP add-on for nginx. It is extremely lightweight and fairly configurable depending on what you need.</p>
    <p>Note the nginx config at the bottom: here we have four different ports open that users can use. The addresses will look like this:</p>
    <pre><code class="lang-bash">rtmp:<span class="hljs-regexp">//</span>public-ip-address-of-ec2:port<span class="hljs-regexp">/live/</span>secret_key
</code></pre>
    <p>Here, the ports go from 1935 (standard RTMP port) to 1938. The secret key doesn't matter and you can give it to your users in private for safety.</p>
    <br />
    <br />
    <h2 id="getting-data-from-the-rtmp-server">Getting Data from the RTMP Server</h2>
    <p>
      To pull the streams from the RTMP server you can use VLC or the VLC plugin on OBS: point it to the
      <code>rtmp</code> address above and it should pick up your user correctly. For VLC, the "Network" option is the one you should use.
    </p>
    <p>Again, they will look something like this:</p>
    <pre><code class="lang-bash">rtmp:<span class="hljs-regexp">//</span>public-ip-address-of-ec2:port<span class="hljs-regexp">/live/</span>secret_key
</code></pre>
  </div>
</template>

<script>
export default {
  name: "Devops"
};
</script>
