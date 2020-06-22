<template>
  <div class="about">
    <h1 id="cost-overhead">Cost Overhead</h1>
    <p>This document will provide transparency on general costs (besides personal computing power / electricity) for Sneakbike.</p>
    <ul>
      <li>
        <a href="#cost-overhead">Cost Overhead</a>
        <ul>
          <li>
            <a href="#aws">AWS</a>
            <ul>
              <li>
                <a href="#ec2">EC2</a>
              </li>
            </ul>
          </li>
          <li>
            <a href="#godaddy">GoDaddy</a>
          </li>
          <li>
            <a href="#digital-ocean">Digital Ocean</a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#approximations">Approximations</a>
      </li>
    </ul>
    <br />
    <br />
    <h2 id="aws">AWS</h2>
    <p>These are costs associated with AWS tools. They are itemized below.</p>
    <h3 id="ec2">EC2</h3>
    <table>
      <thead>
        <tr>
          <th>date</th>
          <th>mins</th>
          <th>viewers</th>
          <th>Instance Type</th>
          <th>cost (usd)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2020-06-20</td>
          <td>90</td>
          <td>~15</td>
          <td>t3a.micro</td>
          <td>$0.31</td>
        </tr>
      </tbody>
    </table>
    <br />
    <br />
    <h2 id="godaddy">GoDaddy</h2>
    <p>These are costs associated with GoDaddy (domains). They are itemized below.</p>
    <table>
      <thead>
        <tr>
          <th>date</th>
          <th>domain</th>
          <th>duration</th>
          <th>cost (usd)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2020-06-20</td>
          <td>sneakbikemysteryrace.com</td>
          <td>3 yrs</td>
          <td>$48.51</td>
        </tr>
      </tbody>
    </table>
    <br />
    <br />
    <h2 id="digital-ocean">Digital Ocean</h2>
    <p>These are costs associated with Digital Ocean (web hosting for dynamic sites). They are itemized below.</p>
    <table>
      <thead>
        <tr>
          <th>start date</th>
          <th>service</th>
          <th>cost (usd)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2020-06-20</td>
          <td>Standard Small Droplet</td>
          <td>$5/mo</td>
        </tr>
      </tbody>
    </table>
    <br />
    <br />
    <h1 id="approximations">Approximations</h1>
    <p>Here we do an approximate calculation for running Sneakbike for a year. We include the yearly price for the domain in this.</p>
    <p>We assume a weekly race about the same time, cost increasing slightly to an average of $0.50.</p>
    <ul>
      <li>Domain: $48.51 / 3 = $16.17</li>
      <li>AWS Costs: $0.50 * 52 = $26.00</li>
      <li>Digital Ocean Costs: $5 * $12 = $60</li>
    </ul>
    <p>
      Giving us a total of
      <code>$102.17/yr</code>.
    </p>
  </div>
</template>

<script>
export default {
  name: "CostOverhead"
};
</script>

<style scoped>
table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}

th,
td {
  padding: 15px;
}
</style>
