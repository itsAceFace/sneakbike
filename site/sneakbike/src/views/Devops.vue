<template>
  <div class="devops">
    <h1 id="devops-documentation-for-sneakbike">Devops Documentation for Sneakbike</h1>
    <br />
    <br />
    <h2 id="general-architecture">General Architecture</h2>
    <img src="@/assets/images/sneakbike_architecture.png" alt="Sneakbike Architecture" />
    <br />
    <br />
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
    <h2 id="setting-up-obs-on-many-runners-computers">Setting up OBS on Many Runners' Computers</h2>
    <p>The most frustrating part without a doubt is getting everyone a similar setup on OBS. We require downloading the latest OBS and have them import both a Profile (to allow us to set resolution) as well as Scene Collections (to allow us to control what things go where, and to not have them confuse it with their own scene collections).</p>
    <p>Due to the nature of OBS's quick-switch for Profiles and Scenes, this works well.</p>

    <h2 id="server-setup-on-aws">Server Setup on AWS with Terraform</h2>

    <p>
      We'll use
      <a href="https://www.terraform.io/intro/index.html">Terraform</a> to build and destroy our RTMP server in AWS. In short, Terraform allows us to easily build simple (and not so simple) AWS structures like our EC2 instance from the commandline.
    </p>
    <p>
      Since their tutorial is great,
      <a
        href="https://learn.hashicorp.com/tutorials/terraform/infrastructure-as-code?in=terraform/aws-get-started"
      >go through the first few of them (it shouldn't take more than 10 minutes)</a>.
    </p>

    <p>
      Once you're done, our tf file is in the
      <b>/scripts/terraform/</b> folder. As per the above, you will need to have set up:
    </p>
    <ul>
      <li>AWS CLI v2</li>
      <li>
        Done
        <b>aws configure</b>
      </li>
      <li>Terraform CLI</li>
      <li>Terraform SSH Key</li>
      <li>
        Run
        <b>terraform init</b> in the folder.
      </li>
    </ul>

    <h2 id="getting-data-from-the-rtmp-server">Getting Data from the RTMP Server</h2>

    <p>
      <b>Note that RTMP always uses port 1935.</b>
    </p>
    <p>
      To pull the streams from the RTMP server you can use VLC or the VLC plugin on OBS: point it to the
      <code>rtmp</code> address above and it should pick up your user correctly. For VLC, the "Network" option is the one you should use.
    </p>
    <p>Again, they will look something like this:</p>
    <pre><code class="lang-bash">rtmp:<span class="hljs-regexp">//</span>public-ip-address-of-ec2:1935<span class="hljs-regexp">/live/</span>secret_key
</code></pre>
  </div>
</template>

<script>
export default {
  name: "Devops",
};
</script>
