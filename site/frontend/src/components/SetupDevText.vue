<template>
  <div class="setup-dev-text">
    <h1>Developer Setup</h1>

    <h2>Basic Structure</h2>
    <img src="@/assets/sneakbike_architecture.png" alt="Sneakbike Architecture" />
    <p>
      We broadcast from several OBS applications to an
      <a
        href="https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol"
      >RTMP</a>
      server hosted into an EC2 box which, in turn, broadcasts to the
      Sneakbike OBS (currently running on an actual physical "on-prem"
      machine).
    </p>
    <ul>
      <li>
        Our EC2 instance is currently an Ubuntu 18.04 t3a.micro
        <ul>
          <li>Optimized for network io, not much memory required.</li>
        </ul>
      </li>
      <li>
        We have a host running OBS on their local computers.
        <ul>
          <li>
            A cloud equivalent would allow more than one individual to
            "run" the stream, which is a good bus-clause practice. We
            currently don't have a good way to do this.
          </li>
        </ul>
      </li>
      <li>
        The racers have to stream from their computers as no reasonable
        alternative exists for capturing desktop gameplay and sending it
        to our RTMP.
      </li>
    </ul>

    <h2>Building the Server with Terraform</h2>

    <p>
      <a href="https://www.terraform.io/intro/index.html" target="_blank">Terraform</a>
      allows us to easily build simple (and not so simple) AWS structures
      like the EC2 instance we need from the commandline.
    </p>

    <info-card>
      We
      <b>HIGHLY RECOMMEND</b> reading the
      <a
        href="https://learn.hashicorp.com/collections/terraform/aws-get-started"
        target="_blank"
      >short tutorial</a>
      on Terraform for AWS.
    </info-card>

    <h3>Requirements and Setup</h3>

    <p>To get started, you'll need four things:</p>

    <ul>
      <li>
        An
        <a href="https://aws.amazon.com/account/" target="_blank">AWS account</a>,
      </li>
      <li>A properly configured AWS CLI,</li>
      <li>Terraform CLI,</li>
      <li>An SSH key for the Terraform CLI.</li>
    </ul>

    <p>
      First, get an AWS account. For the remaining three, see the below
      scripts.
    </p>

    <info-card>
      Most of our users will be using Windows, so we include a Powershell
      script below. In order to run this, go to Windows Start, type
      Powershell, then right-click on the Powershell program and choose
      "Run as Administrator".
    </info-card>

    <p>
      We install
      <a href="https://chocolatey.org/" target="_blank">Chocolatey</a>
      first to make the install of AWS and Terraform easier.
    </p>

    <prism language="powershell">{{ snippet1 }}</prism>

    <p>
      Once you do this,
      <b>Exit and Restart Powershell as Admin</b> and
      copy-paste the following:
    </p>

    <prism language="powershell">{{ snippet2 }}</prism>

    <p>
      At this point, you're ready to use Terraform! After you
      <b>init</b> a directory, you can run the following inside that
      directory:
    </p>

    <prism language="powershell">{{ snippet3 }}</prism>

    <p>
      That's it! Now you're ready to have people connect to
      <prism inline language="powershell">rtmp://the_ip:1935/live</prism>,
      making sure to give each person a different key. You can retrieve
      their data via
      <prism inline language="powershell">rtmp://the_ip:1935/live/their_key</prism>.
    </p>

    <warning-card>
      Make sure to destroy the server when you're done otherwise you'll
      incur charges when you're not using the server!
    </warning-card>
  </div>
</template>

<script>
const snippet1 = `# Download Chocolatey Package Manager 
Set-ExecutionPolicy Bypass -Scope Process -Force;
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
iex((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`;

const snippet2 = `# Install the CLIs
choco install git terraform awscli 

# You might need to make this directory; 
# If it says it already exists, skip this step. 
mkdir $HOME/.ssh 

# Generate the SSH Keys. 
ssh-keygen -t rsa -f $HOME/.ssh/terraform 

# Clone Directory 
git clone https://github.com/jsal13/sneakbike.git 

# Go to the terraform folder. 
cd ./sneakbike/terraform 

# Init terraform 
terraform init`;

const snippet3 = `# Build the server...
terraform apply

# And when you're done...
terraform destroy`;

export default {
  name: "SetupDevText",
  data() {
    return { snippet1, snippet2, snippet3 };
  },
};
</script>
