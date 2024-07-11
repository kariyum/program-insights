<script>
  import { spring } from "svelte/motion";
  import Table from "./lib/Table.svelte";
  import { processData, computeChildren } from "./lib/utils.js";
  /**
   * @type {EventSource}
   */
  let eventSource;
  let ip = "10.3.16.105";
  let service = "promotion-planning";
  // const ip = "10.4.48.146";

  /**
   * @type {Array<EnhancedMetric>}
   */
  let enhancedMetrics = [];
  let connected = -1;
  let obsolete = false;

  /**
   * @type {Array<SingleMetric>}
   */
  let metrics = [];
  // let metrics = [
  //   {
  //     "id": "test01",
  //     "parent": null,
  //     "start_end_times": [1 * 1000000, 6 * 1000000]
  //   },
  //   {
  //     "id": "test01",
  //     "parent": null,
  //     "start_end_times": [1 * 1000000, 7 * 1000000]
  //   },
  //   {
  //     "id": "test02",
  //     "parent": "test01",
  //     "start_end_times": [3 * 1000000, 5 * 1000000]
  //   },
  //   {
  //     "id": "test02",
  //     "parent": "test01",
  //     "start_end_times": [4 * 1000000, 6 * 1000000]
  //   }
  // ];

  function connect() {
    if (eventSource) {
      eventSource.close();
      console.log("Closing last connection.");
    }
    eventSource = new EventSource(`http://${ip}/${service}/metrics-stream`);
    eventSource.onerror = (event) => {
      connected = 3;
    };
    eventSource.onopen = (event) => {
      connected = 1;
    };
    eventSource.onmessage = (event) => {
      connected = eventSource.readyState;
      if (event.data) {
        const data = JSON.parse(event.data);
        metrics.push(...data);
        console.log(metrics);
        obsolete = true;
      }
    };
  }

  $: {
    if (eventSource) {
      connected = eventSource.readyState;
      console.log("connected");
    }
  }

  setInterval(() => {
    if (obsolete == true) {
      console.log("UPDATING.", metrics.length);
      let start = performance.now();
      enhancedMetrics = processData(metrics);
      let end = performance.now();
      console.log("TOOK: ", end - start);
      obsolete = false;
    }
  }, 3000);

  let globalMax;
  let globalMin;
  $: {
    if (metrics !== null) {
      globalMax = enhancedMetrics
        .map((a) => a.cpu_time)
        .reduce((pre, curr) => (pre < curr ? curr : pre), 0);
      globalMin = enhancedMetrics
        .map((a) => a.cpu_time)
        .reduce((pre, curr) => (pre < curr ? pre : curr), 0);
    }
  }
  let url = window.location.href.split("/");
  ip = url[url.length - 1];

  function disconnect() {
    if (connected === 1) {
      eventSource.close();
      connected = eventSource.readyState;
      eventSource = null;
    }
  }
</script>

<main>
  <!-- <ExpandableTableRow/> -->
  <h1>Metrics streaming 101 （￣︶￣）</h1>
  <input type="text" bind:value={ip} />
  <input type="text" bind:value={service} />
  <button on:click={connect}>Connect</button>
  <button
    on:click={() => {
      enhancedMetrics = [];
      metrics = [];
    }}>Reset</button
  >
  <button on:click={disconnect}>Disconnect</button>
  <h1>
    {#if connected == 0}
      Connecting... ⌛ to {ip}
    {:else if connected == 1}
      Open ✅ {ip}
    {:else if (connected = 2)}
      Closed
    {:else if connected == 3}
      <span style="color:red;">ERROR</span> 😱😱😱
    {/if}
  </h1>
  <Table
    data={computeChildren(enhancedMetrics)}
    max={globalMax}
    min={globalMin}
  />
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
