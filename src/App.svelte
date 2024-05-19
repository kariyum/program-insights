<script>
  let metrics = [{ functionNameClass: "test", responseTimes: [1.0, 2.0] }];
  metrics = [
    {
      functionNameClass: "root - computeAllMetrics",
      responseTimes: [
        804.811325, 771.100617, 733.315314, 720.334324, 828.609169, 792.354651,
      ],
      run1: 804.811325,
      run2: 771.100617,
      run3: 733.315314,
      run4: 720.334324,
      run5: 828.609169,
      run6: 792.354651,
    },
    {
      functionNameClass: "eval",
      responseTimes: [
        749.172696, 717.034051, 686.600273, 671.251174, 769.215913, 742.867168,
      ],
      run1: 749.172696,
      run2: 717.034051,
      run3: 686.600273,
      run4: 671.251174,
      run5: 769.215913,
      run6: 742.867168,
    },
    {
      functionNameClass: "logger.info",
      responseTimes: [
        19.515992, 17.247396, 17.572657, 18.206735, 24.600559, 17.61637,
      ],
      run1: 19.515992,
      run2: 17.247396,
      run3: 17.572657,
      run4: 18.206735,
      run5: 24.600559,
      run6: 17.61637,
    },
    {
      functionNameClass: "set_promo_details",
      responseTimes: [
        15.812204, 19.221664, 15.464278, 15.820725, 15.034447, 16.792439,
      ],
      run1: 15.812204,
      run2: 19.221664,
      run3: 15.464278,
      run4: 15.820725,
      run5: 15.034447,
      run6: 16.792439,
    },
    {
      functionNameClass:
        "Deserialization of PromotionToCompute Deserialization",
      responseTimes: [
        13.96331, 12.299124, 12.03115, 11.904646, 11.435393, 13.545215,
      ],
      run1: 13.96331,
      run2: 12.299124,
      run3: 12.03115,
      run4: 11.904646,
      run5: 11.435393,
      run6: 13.545215,
    },
    {
      functionNameClass: "computedMetrics case class",
      responseTimes: [
        10.990059, 10.13205, 6.420803, 7.075724, 11.120978, 6.82696,
      ],
      run1: 10.990059,
      run2: 10.13205,
      run3: 6.420803,
      run4: 7.075724,
      run5: 11.120978,
      run6: 6.82696,
    },
    {
      functionNameClass: "Context.cleanPromotionContext",
      responseTimes: [3.9341, 2.943801, 2.96144, 3.157144, 4.498194, 2.960912],
      run1: 3.9341,
      run2: 2.943801,
      run3: 2.96144,
      run4: 3.157144,
      run5: 4.498194,
      run6: 2.960912,
    },
    {
      functionNameClass: "hasCycle",
      responseTimes: [2.701338, 2.759895, 2.649, 2.912033, 2.681015, 3.66974],
      run1: 2.701338,
      run2: 2.759895,
      run3: 2.649,
      run4: 2.912033,
      run5: 2.681015,
      run6: 3.66974,
    },
    {
      functionNameClass: "NodesCaches.intializeNodesCaches",
      responseTimes: [
        0.840643, 0.054902, 0.045702, 0.050402, 0.049402, 0.050002,
      ],
      run1: 0.840643,
      run2: 0.054902,
      run3: 0.045702,
      run4: 0.050402,
      run5: 0.049402,
      run6: 0.050002,
    },
    {
      functionNameClass: "Context.removeComputationIdToOriginalUUIDMapping",
      responseTimes: [
        0.135907, 0.111404, 0.097505, 0.096704, 0.134806, 0.107204,
      ],
      run1: 0.135907,
      run2: 0.111404,
      run3: 0.097505,
      run4: 0.096704,
      run5: 0.134806,
      run6: 0.107204,
    },
    {
      functionNameClass: "Future(randomUUID)",
      responseTimes: [
        0.106405, 0.109804, 0.105904, 0.094404, 0.105104, 0.101304,
      ],
      run1: 0.106405,
      run2: 0.109804,
      run3: 0.105904,
      run4: 0.094404,
      run5: 0.105104,
      run6: 0.101304,
    },
    {
      functionNameClass: "ComputationCounter.decrementPEFCounter",
      responseTimes: [
        0.104005, 0.113804, 0.102405, 0.080104, 0.101205, 0.097703,
      ],
      run1: 0.104005,
      run2: 0.113804,
      run3: 0.102405,
      run4: 0.080104,
      run5: 0.101205,
      run6: 0.097703,
    },
    {
      functionNameClass: "Future of promo_id",
      responseTimes: [
        0.052703, 0.079603, 0.061502, 0.064203, 0.053903, 0.048402,
      ],
      run1: 0.052703,
      run2: 0.079603,
      run3: 0.061502,
      run4: 0.064203,
      run5: 0.053903,
      run6: 0.048402,
    },
    {
      functionNameClass: "execution_dependecy_graph",
      responseTimes: [
        0.046702, 0.061202, 0.087103, 0.055203, 0.065003, 0.043502,
      ],
      run1: 0.046702,
      run2: 0.061202,
      run3: 0.087103,
      run4: 0.055203,
      run5: 0.065003,
      run6: 0.043502,
    },
    {
      functionNameClass: "NodesCaches.cleanNodesCaches",
      responseTimes: [
        0.051303, 0.044502, 0.040902, 0.043602, 0.050902, 0.054003,
      ],
      run1: 0.051303,
      run2: 0.044502,
      run3: 0.040902,
      run4: 0.043602,
      run5: 0.050902,
      run6: 0.054003,
    },
    {
      functionNameClass: "ForecastContext.cleanForecastContext",
      responseTimes: [0.015601, 0.0136, 0.020801, 0.0115, 0.015301, 0.0125],
      run1: 0.015601,
      run2: 0.0136,
      run3: 0.020801,
      run4: 0.0115,
      run5: 0.015301,
      run6: 0.0125,
    },
    {
      functionNameClass: "Context.setCookieMapping",
      responseTimes: [0.0053, 0.0035, 0.0032, 0.0035, 0.003, 0.0039],
      run1: 0.0053,
      run2: 0.0035,
      run3: 0.0032,
      run4: 0.0035,
      run5: 0.003,
      run6: 0.0039,
    },
    {
      functionNameClass: "Context.removeCookieMapping",
      responseTimes: [0.0028, 0.0026, 0.0017, 0.0019, 0.0022, 0.0019],
      run1: 0.0028,
      run2: 0.0026,
      run3: 0.0017,
      run4: 0.0019,
      run5: 0.0022,
      run6: 0.0019,
    },
  ];
  // metrics = [];
  let runsArray = [];
  function processData(data) {
    const sumResponseTimes = (
      /** @type {{ responseTimes: number[]; }} */ obj,
    ) => obj.responseTimes.reduce((acc, val) => acc + val, 0);
    const sortedArray = data.sort(
      (a, b) => sumResponseTimes(b) - sumResponseTimes(a),
    );
    const mergedArray = sortedArray.map((obj) => {
      const flattenedResponseTimes = obj.responseTimes.reduce(
        (acc, val, index) => {
          acc[`run${index + 1}`] = val;
          return acc;
        },
        {},
      );
      return { ...obj, ...flattenedResponseTimes };
    });
    runsArray = mergedArray[0].responseTimes.map((_, idx) => `Run${idx + 1}`);
    metrics = mergedArray;
    console.log(mergedArray);
  }
  processData(metrics);
  const eventSource = new EventSource("http://localhost:5000/metrics-stream");
  eventSource.onmessage = (event) => {
    if (event.data) {
      const data = JSON.parse(event.data);
      processData(data);
    }
  };
</script>

<main>
  <h1>Hello world!</h1>
  <table>
    <thead>
      <tr>
        <th>Metric</th>
        <th> Response times </th>
        {#each runsArray as run}
          <th>{run}</th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each metrics as item (item.functionNameClass)}
        <tr>
          <td>
            {item.functionNameClass}
          </td>
          <td>
            {item.responseTimes
              .map((x) => x.toString())
              .reduceRight((previous, curr) => previous + ", " + curr)}
          </td>
          {#each item.responseTimes as responseTime}
            <td>
              {responseTime}
            </td>
          {/each}
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
