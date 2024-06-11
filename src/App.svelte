<script>
  import { spring } from "svelte/motion";
  import ExpandableTableRow from "./lib/ExpandableTableRow.svelte";
  import Table from "./lib/testbing/Table.svelte";

  let metrics = [
    {
      parent: null,
      functionNameClass: "test",
      nbCalls: 1,
      min: 1.0,
      max: 2.0,
      average: 1.0,
      cpu_time: 1,
    },
    {
      parent: "test",
      functionNameClass: "test2",
      nbCalls: 1,
      min: 1.0,
      max: 2.0,
      average: 2.0,
      cpu_time: 2,
    },
  ];

  const sortByAverage = (data) => data.sort((a, b) => b.average - a.average);

  function processData(data) {
    // console.log(sortByAverage(data));
    return sortByAverage(data);
  }
  /**
   *
   * @param {number} n
   */
  function format(n) {
    try {
      return n.toFixed(3);
    } catch {
      return 0;
    }
  }

  let eventSource;
  let ip = "10.3.16.105";
  let service = "calc-engine";
  // const ip = "10.4.48.146";

  let connected = -1;
  function connect() {
    if (eventSource) {
      eventSource.close();
      console.log("Closing last connection.")
    }
    eventSource = new EventSource(`http://${ip}/${service}/metrics-stream`);
    eventSource.onerror = (event) => {
      connected = 2;
    };
    eventSource.onopen = (event) => {
      connected = 1;
    };
    eventSource.onmessage = (event) => {
      connected = eventSource.readyState;
      if (event.data) {
        const data = JSON.parse(event.data);
        metrics = processData(data);
      }
    };
  }


  $: {
    if (eventSource) {
      connected = eventSource.readyState;
    }
  }

  metrics = processData(metrics);
  let globalMax;
  let globalMin;
  $: {
    globalMax = metrics
      .map((a) => a.cpu_time)
      .reduce((pre, curr) => (pre < curr ? curr : pre));
    globalMin = metrics
      .map((a) => a.cpu_time)
      .reduce((pre, curr) => (pre < curr ? pre : curr));
  }
  let url = window.location.href.split("/")
  ip = url[url.length - 1]
</script>

<main>
  <!-- <ExpandableTableRow/> -->
  <h1>Hello world!</h1>
  <input type="text" bind:value={ip}>
  <input type="text" bind:value={service}>
  <button on:click={connect}>Connect</button>
  <h1>
    {#if connected == 0}
      Connecting... ⌛ to {ip}
    {:else if connected == 1}
      Open ✅ {ip}
    {:else if connected == 2}
      <span style="color:red;">ERROR</span> 😱😱😱
    {/if}
  </h1>
  <Table data={metrics} max={globalMax} min={globalMin} />
</main>

<style>
  table {
    font-family: arial, sans-serif;
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
  }

  table td {
    white-space: nowrap;
  }

  thead {
    position: sticky;
    background: white;
    top: 0;
    padding: 0;
    margin: 0;
  }

  th {
    position: sticky;
    top: 0px;
    border: 1px solid #e3e3e3;
    text-align: left;
    padding: 8px;
  }

  td {
    border: 1px solid #e3e3e3;
    text-align: left;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #f0f0f0;
  }
</style>
