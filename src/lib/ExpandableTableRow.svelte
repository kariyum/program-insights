<script>
  
  function addDepth(data) {
    let depthMap = {};
    for (let item of data) {
      if (item.parent === null) {
        item.depth = 0;
      } else {
        item.depth = depthMap[item.parent] + 1;
      }
      depthMap[item.functionNameClass] = item.depth;
    }
  }
  let data = [
    {
      parent: null,
      average: 7.0786059600000035,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.Match node",
      max: 49.68431,
      min: 0.239701,
      nbCalls: 50,
    },
    {
      parent: "execute function for com.cognira.ppce.nodes.Match node",
      average: 0.6754327751351366,
      functionNameClass:
        "run function for com.cognira.ppce.nodes.FetchSet node",
      max: 28.823022,
      min: 0.0105,
      nbCalls: 925,
    },
    {
      parent: "run function for com.cognira.ppce.nodes.FetchSet node",
      average: 0.276702,
      functionNameClass: "createEntityToForecastFromPromoDetails",
      max: 0.276702,
      min: 0.276702,
      nbCalls: 1,
    },
    {
      average: 1.89757752173913,
      functionNameClass: "execute function for com.cognira.ppce.Value node",
      max: 16.153368,
      min: 0.062901,
      nbCalls: 23,
    },
    {
      average: 1563.9038501690952,
      functionNameClass: "computed_fields_cache.get",
      max: 2046.41236,
      min: 15.342065,
      nbCalls: 343,
    },
    {
      average: 0.449802,
      functionNameClass: "NodesCaches.intializeNodesCaches",
      max: 0.449802,
      min: 0.449802,
      nbCalls: 1,
    },
    {
      average: 0.0667,
      functionNameClass: "ForecastContext.cleanForecastContext",
      max: 0.0667,
      min: 0.0667,
      nbCalls: 1,
    },
    {
      average: 0.1215,
      functionNameClass: "execution_dependecy_graph",
      max: 0.1215,
      min: 0.1215,
      nbCalls: 1,
    },
    {
      average: 0.0025,
      functionNameClass: "evaluationCache.forecastNAmeToCacheMapping",
      max: 0.0025,
      min: 0.0025,
      nbCalls: 1,
    },
    {
      average: 6.7454285,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.Case node",
      max: 48.951207,
      min: 0.164,
      nbCalls: 50,
    },
    {
      average: 2.6530424155844154,
      functionNameClass:
        "run function for com.cognira.ppce.nodes.Replicate node",
      max: 23.053698,
      min: 0.0825,
      nbCalls: 77,
    },
    {
      average: 0.15769068,
      functionNameClass: "run function for com.cognira.ppce.nodes.Case node",
      max: 2.524911,
      min: 0.0086,
      nbCalls: 50,
    },
    {
      average: 0.0789,
      functionNameClass: "NodesCaches.cleanNodesCaches",
      max: 0.0789,
      min: 0.0789,
      nbCalls: 1,
    },
    {
      average: 0.556502,
      functionNameClass: "Context.removeComputationIdToOriginalUUIDMapping",
      max: 0.556502,
      min: 0.556502,
      nbCalls: 1,
    },
    {
      average: 1392.4313121999999,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.ForecastNode node",
      max: 1431.656958,
      min: 1373.250212,
      nbCalls: 5,
    },
    {
      average: 0.028,
      functionNameClass: "Future of promo_id",
      max: 0.028,
      min: 0.028,
      nbCalls: 1,
    },
    {
      average: 2.32502863322884,
      functionNameClass:
        "run function for com.cognira.ppce.nodes.AggOperator node",
      max: 53.805828,
      min: 0.0419,
      nbCalls: 319,
    },
    {
      average: 4.74402,
      functionNameClass: "hasCycle",
      max: 4.74402,
      min: 4.74402,
      nbCalls: 1,
    },
    {
      average: 2.596806699774263,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.CrossProduct node",
      max: 50.919715,
      min: 0.0881,
      nbCalls: 443,
    },
    {
      average: 5.761729253191494,
      functionNameClass:
        "run function for com.cognira.ppce.nodes.FetchValues node",
      max: 118.545002,
      min: 0.0951,
      nbCalls: 470,
    },
    {
      average: 7.348955792207794,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.Replicate node",
      max: 50.582214,
      min: 0.15,
      nbCalls: 77,
    },
    {
      average: 0.0019,
      functionNameClass: "sharedInterfaces.promo_details",
      max: 0.0019,
      min: 0.0019,
      nbCalls: 1,
    },
    {
      average: 0.0069,
      functionNameClass: "Context.removeCookieMapping",
      max: 0.0069,
      min: 0.0069,
      nbCalls: 1,
    },
    {
      average: 36.69539301169592,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.Assign node",
      max: 1431.716258,
      min: 0.309101,
      nbCalls: 342,
    },
    {
      average: 1512.6736328684208,
      functionNameClass:
        "Future.sequence(dependent_fields.map).computed_fields_cache.get",
      max: 2038.759428,
      min: 0.0034,
      nbCalls: 342,
    },
    {
      average: 0.315901,
      functionNameClass: "ComputationCounter.decrementPEFCounter",
      max: 0.315901,
      min: 0.315901,
      nbCalls: 1,
    },
    {
      average: 8.345898693617022,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.FetchValues node",
      max: 152.607946,
      min: 0.1682,
      nbCalls: 470,
    },
    {
      average: 0.22494004347826083,
      functionNameClass: "run function for com.cognira.ppce.Value node",
      max: 2.092709,
      min: 0.0174,
      nbCalls: 23,
    },
    {
      average: 2077.390591,
      functionNameClass: "eval",
      max: 2077.390591,
      min: 2077.390591,
      nbCalls: 1,
    },
    {
      average: 14.539548072100333,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.AggOperator node",
      max: 192.668215,
      min: 0.256801,
      nbCalls: 319,
    },
    {
      average: 42.386058336257264,
      functionNameClass: "computed_fields_cache.evaluation",
      max: 1431.791959,
      min: 0.542803,
      nbCalls: 342,
    },
    {
      average: 1431.605158,
      functionNameClass:
        "evaluation cache forecast node PromotionMergedDemandRedemptionModels",
      max: 1431.605158,
      min: 1431.605158,
      nbCalls: 1,
    },
    {
      average: 2234.986958,
      functionNameClass: "root - computeAllMetrics",
      max: 2234.986958,
      min: 2234.986958,
      nbCalls: 1,
    },
    {
      average: 1564.135738076023,
      functionNameClass: "computing value for computed_fields_cache",
      max: 2046.41266,
      min: 15.359365,
      nbCalls: 342,
    },
    {
      average: 25.799609,
      functionNameClass: "set_promo_details",
      max: 25.799609,
      min: 25.799609,
      nbCalls: 1,
    },
    {
      average: 68.48819,
      functionNameClass: "evaluationCache.entityToForecast",
      max: 68.48819,
      min: 68.48819,
      nbCalls: 1,
    },
    {
      average: 0.42730784000000005,
      functionNameClass: "run function for com.cognira.ppce.nodes.Match node",
      max: 10.534444,
      min: 0.041901,
      nbCalls: 50,
    },
    {
      average: 4.042954618750001,
      functionNameClass:
        "run function for com.cognira.ppce.nodes.BinaryOperator node",
      max: 52.776823,
      min: 0.058201,
      nbCalls: 160,
    },
    {
      average: 121.73916474999999,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.PriceCostNode node",
      max: 147.503024,
      min: 91.497087,
      nbCalls: 4,
    },
    {
      average: 1.6164439329729732,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.FetchSet node",
      max: 50.678214,
      min: 0.0313,
      nbCalls: 925,
    },
    {
      average: 0.0048,
      functionNameClass: "Context.setCookieMapping",
      max: 0.0048,
      min: 0.0048,
      nbCalls: 1,
    },
    {
      average: 2429.051979,
      functionNameClass: "root - route took",
      max: 2429.051979,
      min: 2429.051979,
      nbCalls: 1,
    },
    {
      average: 1.4702831403508778,
      functionNameClass: "run function for com.cognira.ppce.nodes.Assign node",
      max: 47.702802,
      min: 0.0341,
      nbCalls: 342,
    },
    {
      average: 14.21446,
      functionNameClass: "Context.cleanPromotionContext",
      max: 14.21446,
      min: 14.21446,
      nbCalls: 1,
    },
    {
      average: 1363.004668,
      functionNameClass: "PromotionMergedDemandRedemption - run function",
      max: 1363.004668,
      min: 1363.004668,
      nbCalls: 1,
    },
    {
      average: 11.386888868750004,
      functionNameClass:
        "execute function for com.cognira.ppce.nodes.BinaryOperator node",
      max: 151.911643,
      min: 0.292701,
      nbCalls: 160,
    },
    {
      average: 0.4712350438596493,
      functionNameClass: "evaluateField.execute",
      max: 69.419394,
      min: 0.014,
      nbCalls: 342,
    },
    {
      average: 51.588718,
      functionNameClass: "computedMetrics case class",
      max: 51.588718,
      min: 51.588718,
      nbCalls: 1,
    },
    {
      average: 0.0076,
      functionNameClass: "ForecastContext.requestUUIDToPromoIds",
      max: 0.0076,
      min: 0.0076,
      nbCalls: 1,
    },
    {
      average: 0.0012,
      functionNameClass: "evaluationCache.computation_id_to_original_id_map",
      max: 0.0012,
      min: 0.0012,
      nbCalls: 1,
    },
    {
      average: 53.592827,
      functionNameClass: "promotionDetails.toJson",
      max: 53.592827,
      min: 53.592827,
      nbCalls: 1,
    },
    {
      average: 0.6885523544018057,
      functionNameClass:
        "run function for com.cognira.ppce.nodes.CrossProduct node",
      max: 32.059036,
      min: 0.0055,
      nbCalls: 443,
    },
    {
      average: 1357.2806435,
      functionNameClass:
        "Model name: PromotionMergedDemandRedemption, runner function",
      max: 1361.977963,
      min: 1352.583324,
      nbCalls: 2,
    },
    {
      average: 1567.7527411153033,
      functionNameClass: "inner_computed_fields_cache.get",
      max: 2038.741328,
      min: 9.005638,
      nbCalls: 477,
    },
    {
      average: 53.777128,
      functionNameClass: "logger.info",
      max: 53.777128,
      min: 53.777128,
      nbCalls: 1,
    },
    {
      average: 0.218701,
      functionNameClass: "Future.successful(randomUUID)",
      max: 0.218701,
      min: 0.218701,
      nbCalls: 1,
    },
    {
      average: 47.1944,
      functionNameClass:
        "Deserialization of PromotionToCompute Deserialization",
      max: 47.1944,
      min: 47.1944,
      nbCalls: 1,
    },
  ];
  addDepth(data);
  let expanded = {};

  function toggle(item) {
    if (expanded[item.functionNameClass]) {
      for (let child of data) {
        if (child.parent === item.functionNameClass) {
          expanded[child.functionNameClass] = false;
        }
      }
      expanded[item.functionNameClass] = false;
    } else {
      expanded[item.functionNameClass] = true;
    }
  }
</script>

<table>
  <tr>
    <th>Function Name</th>
    <th>Nb Calls</th>
    <th>Min</th>
    <th>Max</th>
    <th>Average</th>
  </tr>
  {#each data as item (item.functionNameClass)}
    <tr
      class={item.parent && !expanded[item.parent] ? "hidden" : ""}
      on:click={() => toggle(item)}
    >
      <td
        class={item.parent ? "child" : ""}
        style="--padding: {item.depth * 20}px;"
        ><span class="arrow"
          >{expanded[item.functionNameClass] ? "v" : ">"}</span
        >
        {item.functionNameClass}</td
      >
      <td>{item.nbCalls}</td>
      <td>{item.min}</td>
      <td>{item.max}</td>
      <td>{item.average}</td>
    </tr>
  {/each}
</table>

<style>
  .hidden {
    display: none;
  }

  .child {
    padding-left: var(--padding);
  }

  .arrow {
    cursor: pointer;
  }

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
