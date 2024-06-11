<script>
    // @ts-nocheck

    import Row from "./Row.svelte";
    export let data;
    export let max;
    export let min;

    let xx = [
        {
            average: 1223.0815743684211,
            functionNameClass:
                "Future.sequence(dependent_fields.map).computed_fields_cache.get",
            max: 1641.794196,
            min: 0.0023,
            nbCalls: 342,
            parent: "computedFieldsCacheLoader",
        },
        {
            average: 0.0036,
            functionNameClass: "Context.setCookieMapping",
            max: 0.0036,
            min: 0.0036,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 1912.08741,
            functionNameClass: "root - route took",
            max: 1912.08741,
            min: 1912.08741,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 1.9085800400000008,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.Match node",
            max: 32.964373,
            min: 0.055001,
            nbCalls: 50,
            parent: null,
        },
        {
            average: 8.353964312500006,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.BinaryOperator node",
            max: 117.742917,
            min: 0.144101,
            nbCalls: 160,
            parent: null,
        },
        {
            average: 0.071,
            functionNameClass: "execution_dependecy_graph",
            max: 0.071,
            min: 0.071,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 11.901066692789975,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.AggOperator node",
            max: 171.226497,
            min: 0.160401,
            nbCalls: 319,
            parent: null,
        },
        {
            average: 5.755324215686274,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.Case node",
            max: 33.260074,
            min: 0.190701,
            nbCalls: 51,
            parent: null,
        },
        {
            average: 5.440111636363639,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.Replicate node",
            max: 33.255174,
            min: 0.171001,
            nbCalls: 77,
            parent: null,
        },
        {
            average: 1260.631607225146,
            functionNameClass: "computed_fields_cache",
            max: 1654.789063,
            min: 2.301912,
            nbCalls: 342,
            parent: null,
        },
        {
            average: 3.464918,
            functionNameClass: "hasCycle",
            max: 3.464918,
            min: 3.464918,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 0.9272522384034534,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.FetchSet node",
            max: 33.231074,
            min: 0.0056,
            nbCalls: 927,
            parent: null,
        },
        {
            average: 6.597576600000001,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.Match node",
            max: 33.262774,
            min: 0.268202,
            nbCalls: 50,
            parent: null,
        },
        {
            average: 2.3369894864864853,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.CrossProduct node",
            max: 47.427648,
            min: 0.043101,
            nbCalls: 444,
            parent: null,
        },
        {
            average: 0.7575891328828834,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.CrossProduct node",
            max: 28.733151,
            min: 0.0047,
            nbCalls: 444,
            parent: null,
        },
        {
            average: 1794.608595,
            functionNameClass: "root - computeAllMetrics",
            max: 1794.608595,
            min: 1794.608595,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 2.9099346489028246,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.AggOperator node",
            max: 54.693486,
            min: 0.0253,
            nbCalls: 319,
            parent: null,
        },
        {
            average: 0.0085,
            functionNameClass: "ForecastContext.requestUUIDToPromoIds",
            max: 0.0085,
            min: 0.0085,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 1059.5467975000001,
            functionNameClass:
                "Model name: PromotionMergedDemandRedemption, runner function",
            max: 1071.320109,
            min: 1047.773486,
            nbCalls: 2,
            parent: null,
        },
        {
            average: 1.2186181176470596,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.Case node",
            max: 32.976773,
            min: 0.0094,
            nbCalls: 51,
            parent: null,
        },
        {
            average: 0.0628,
            functionNameClass: "Future of promo_id",
            max: 0.0628,
            min: 0.0628,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 0.251702,
            functionNameClass: "createEntityToForecastFromPromoDetails",
            max: 0.251702,
            min: 0.251702,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 1157.48506,
            functionNameClass:
                "evaluation cache forecast node PromotionMergedDemandRedemptionModels",
            max: 1157.48506,
            min: 1157.48506,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 34.96155500292402,
            functionNameClass: "evaluateField",
            max: 1158.964967,
            min: 0.231201,
            nbCalls: 342,
            parent: "computedFieldsCacheLoader",
        },
        {
            average: 0.6488817391304349,
            functionNameClass:
                "execute function for com.cognira.ppce.Value node",
            max: 4.592924,
            min: 0.0479,
            nbCalls: 23,
            parent: null,
        },
        {
            average: 0.1024,
            functionNameClass: "Future.successful(randomUUID)",
            max: 0.1024,
            min: 0.1024,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 44.628734,
            functionNameClass: "set_promo_details",
            max: 44.628734,
            min: 44.628734,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 1071.54011,
            functionNameClass: "PromotionMergedDemandRedemption - run function",
            max: 1071.54011,
            min: 1071.54011,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 1.98696629239766,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.Assign node",
            max: 41.515418,
            min: 0.0252,
            nbCalls: 342,
            parent: null,
        },
        {
            average: 0.0012,
            functionNameClass: "sharedInterfaces.promo_details",
            max: 0.0012,
            min: 0.0012,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 0.041,
            functionNameClass: "NodesCaches.intializeNodesCaches",
            max: 0.041,
            min: 0.041,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 1152.0778114,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.ForecastNode node",
            max: 1155.893552,
            min: 1147.666108,
            nbCalls: 5,
            parent: null,
        },
        {
            average: 7.555609787685771,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.FetchValues node",
            max: 134.341103,
            min: 0.102101,
            nbCalls: 471,
            parent: null,
        },
        {
            average: 61.46504625,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.PriceCostNode node",
            max: 64.98304,
            min: 53.212478,
            nbCalls: 4,
            parent: null,
        },
        {
            average: 0.001,
            functionNameClass:
                "evaluationCache.computation_id_to_original_id_map",
            max: 0.001,
            min: 0.001,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 12.589865,
            functionNameClass: "computedMetrics case class",
            max: 12.589865,
            min: 12.589865,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 30.071116818713413,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.Assign node",
            max: 1158.894767,
            min: 0.171601,
            nbCalls: 342,
            parent: null,
        },
        {
            average: 44.086731,
            functionNameClass: "logger.info",
            max: 44.086731,
            min: 44.086731,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 0.3019884347826088,
            functionNameClass: "run function for com.cognira.ppce.Value node",
            max: 3.85732,
            min: 0.0345,
            nbCalls: 23,
            parent: null,
        },
        {
            average: 2.160958775,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.BinaryOperator node",
            max: 32.39217,
            min: 0.0255,
            nbCalls: 160,
            parent: null,
        },
        {
            average: 1665.413719,
            functionNameClass: "eval",
            max: 1665.413719,
            min: 1665.413719,
            nbCalls: 1,
            parent: "computeAllMetrics",
        },
        {
            average: 1264.6755510419284,
            functionNameClass: "inner_computed_fields_cache.get",
            max: 1641.765495,
            min: 1.700009,
            nbCalls: 477,
            parent: "computedFieldsCacheLoader",
        },
        {
            average: 1.7217864595469254,
            functionNameClass:
                "execute function for com.cognira.ppce.nodes.FetchSet node",
            max: 33.251174,
            min: 0.0159,
            nbCalls: 927,
            parent: null,
        },
        {
            average: 84.266042,
            functionNameClass: "evaluationCache.entityToForecast",
            max: 84.266042,
            min: 84.266042,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 1.4476748070175434,
            functionNameClass: "evaluateField.execute",
            max: 123.947749,
            min: 0.0073,
            nbCalls: 342,
            parent: "evaluateField",
        },
        {
            average: 5.518553683651802,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.FetchValues node",
            max: 114.131498,
            min: 0.0447,
            nbCalls: 471,
            parent: null,
        },
        {
            average: 0.0023,
            functionNameClass: "evaluationCache.forecastNAmeToCacheMapping",
            max: 0.0023,
            min: 0.0023,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 1.5274989090909092,
            functionNameClass:
                "run function for com.cognira.ppce.nodes.Replicate node",
            max: 33.002473,
            min: 0.064601,
            nbCalls: 77,
            parent: null,
        },
        {
            average: 1259.8691060728847,
            functionNameClass: "computed_fields_cache.get",
            max: 1654.756063,
            min: 1.546608,
            nbCalls: 343,
            parent: "computeAllMetrics",
        },
        {
            average: 68.022656,
            functionNameClass: "promotionDetails.toJson",
            max: 68.022656,
            min: 68.022656,
            nbCalls: 1,
            parent: null,
        },
        {
            average: 30.721461,
            functionNameClass:
                "Deserialization of PromotionToCompute Deserialization",
            max: 30.721461,
            min: 30.721461,
            nbCalls: 1,
            parent: null,
        },
    ];
    import { beforeUpdate } from "svelte";

    // export let data;
    function arrayToTree(array) {
        console.log("Array To Tree");
        let tree = [];
        let lookup = {};
        console.log("BEFORE LENGTH", array.length);
        // handle parents that are not measured
        const parents = new Set(
            array.map((a) => a.parent).filter((a) => a !== null),
        );
        console.log(parents);
        const functionNameClasses = new Set(
            array.map((a) => a.functionNameClass),
        );
        const difference = (a, b) => new Set([...a].filter((x) => !b.has(x)));
        console.log("DIFF ", difference(parents, functionNameClasses));
        for (const it of difference(parents, functionNameClasses)) {
            array.push({
                functionNameClass: it,
                parent: null,
            });
            console.log("+1");
        }
        console.log("AFTER LENGTH", array.length);
        // First map the nodes of the array to an object -> create a hash table.
        for (let i = 0; i < array.length; i++) {
            lookup[array[i].functionNameClass] = array[i];
            array[i].children = [];
        }

        for (let i = 0; i < array.length; i++) {
            if (array[i].parent) {
                lookup[array[i].parent].children.push(array[i]);
            } else {
                // If no parent is specified, add it to the root array
                tree.push(array[i]);
            }
        }
        console.log(tree);
        return tree;
    }

    // beforeUpdate(() => {
    //     data = arrayToTree(data);
    // });
    $: {
        data = arrayToTree(data);
    }
    console.log("ROW: max = ", max);
    console.log("ROW min = ", min);
</script>

<table>
    <thead>
        <tr>
            <th>Function Name</th>
            <th>Nb Calls</th>
            <th>Average</th>
            <th>Min</th>
            <th>Max</th>
            <th>CPU time</th>
        </tr>
    </thead>
    {#each data as item (item.functionNameClass)}
        {#if !item.parent}
            <Row currentItem={item} data={item.children} depth={0} max={max} min={min}/>
        {/if}
    {/each}
</table>

<style>
    table {
        font-family: arial, sans-serif;
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }

    table {
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
</style>
