<script>
	import { spring } from 'svelte/motion';
  let metrics = [{ functionNameClass: "test", nbCalls : 1, min : 1.0, max : 2.0, average : 1.0 }, { functionNameClass: "test2", nbCalls : 1, min : 1.0, max : 2.0, average : 2.0 }];

  const sortByAverage = (data) => data.sort((a, b) => b.average - a.average,);

  function processData(data) {
    // console.log(sortByAverage(data));
    return sortByAverage(data);
  }
  /**
   * @param {number} n
   */
  function format(n) {
    return n.toFixed(3);
  }

  const eventSource = new EventSource("http://10.3.16.105/calc-engine/metrics-stream");
  
  $: connected = eventSource.readyState
  eventSource.onerror = (event) => {
    connected = 2
  }
  eventSource.onopen = (event) => {
    connected = 1
  }
  eventSource.onmessage = (event) => {
    connected = eventSource.readyState
    if (event.data) {
      const data = JSON.parse(event.data);
      metrics = processData(data);
    }
  };
  metrics = processData(metrics)
</script>

<main>
  <h1>Hello world!</h1>
  <h1>
    {#if connected == 0}
      Connecting... ⌛
    {:else if connected == 1}
      Open ✅
    {:else if connected == 2}
      <span style="color:red;">ERROR</span> 😱😱😱
    {/if}
  </h1>
  <table>
    <thead>
      <tr>
        <th>Metric</th>
        <th># Calls</th>
        <th>Average (ms)</th>
        <th>Minimum (ms)</th>
        <th>Maximum (ms)</th>
        <!-- <th>Median (ms)</th> -->
      </tr>
    </thead>
    <tbody>
      {#each metrics as item (item.functionNameClass)}
        <tr>
          <td>{item.functionNameClass}</td>
          <td>{item.nbCalls}</td>
          <td>{format(item.average)}</td>
          <td>{format(item.min)}</td>
          <td>{format(item.max)}</td>
          <!-- <td>{format(median(item.responseTimes))}</td> -->
        </tr>
      {/each}
    </tbody>
  </table>
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
