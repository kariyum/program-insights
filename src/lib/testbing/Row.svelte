<script>
	// @ts-nocheck

	export let currentItem;
	export let data;
	export let depth;
	export let min;
	export let max;
	function remainingChildren(data, child) {
		let remaining = [];
		for (const object of data) {
			if (object.parent === child.functionNameClass) {
				remaining.push(object);
			}
		}
		console.log(
			`remaining of ${data.length} ${child.functionNameClass}`,
			remaining,
		);
		return remaining;
	}
	let showChildren = true;
	function toggle() {
		showChildren = !showChildren;
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
	$: children = data;
</script>

{#if currentItem.children.length > 0}
	<tr class="{depth != 0 ? "greyed" : ""} arrow" on:click={() => toggle()}>
		<td
			class={currentItem.parent ? "child" : ""}
			style="--padding: {depth * 20}px;"
		>
			<span class="arrow">{showChildren ? "↓" : "→"}</span>
			{currentItem.functionNameClass}</td
		>
		<td>{currentItem.nbCalls}</td>
		<td>{format(currentItem.average)}</td>
		<td>{format(currentItem.min)}</td>
		<td>{format(currentItem.max)}</td>
		<td class="colored" style="--rowcolor: {currentItem.cpu_time / max}">{format(currentItem.cpu_time)} - {Math.floor(currentItem.cpu_time / max * 100)}%</td>
	</tr>
{:else}
	<tr class="{depth != 0 ? "greyed" : ""}">
		<td
			class={currentItem.parent ? "child" : ""}
			style="--padding: {depth * 20}px;"
		>
			{currentItem.functionNameClass}</td
		>
		<td>{currentItem.nbCalls}</td>
		<td>{format(currentItem.average)}</td>
		<td>{format(currentItem.min)}</td>
		<td>{format(currentItem.max)}</td>
		<td class="colored" style="--rowcolor: {currentItem.cpu_time / max}">{format(currentItem.cpu_time)} - {Math.floor(currentItem.cpu_time / max * 100)}%</td>
	</tr>
{/if}
{#if showChildren && children.length > 0}
	{#each children as item (item.functionNameClass)}
		<svelte:self
			currentItem={item}
			data={item.children}
			depth={depth + 1}
			min={min}
			max={max}
		/>
	{/each}
{/if}

<style>
	tr:hover {
		background-color: rgb(196, 228, 255);
	}
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
	.colored {
		background-color: hsl(25, 100%, 50%, var(--rowcolor));
	}

	.greyed {
		background-color: #f8f8f8;
	}
</style>
