<script>
    import { beforeUpdate } from "svelte";


    import Row from "./Row.svelte";
    /**
     * @type {Array<EnhancedMetric>}
     */
    export let data;
    export let max;
    export let min;
    beforeUpdate(
        () => {
            console.log("Table data", data);
        }
    )
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
    {#if data}
        {#each data as item (item.id)}
            {#if !item.parent}
                <Row currentItem={item} data={item.children} depth={0} max={max} min={min}/>
            {/if}
        {/each}
    {/if}
</table>

<style>
    table {
        font-family: arial, sans-serif;
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
    }

    /* table {
        white-space: nowrap;
    } */

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
