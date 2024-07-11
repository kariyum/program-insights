/**
 * Compute average for the given list.
 * @param {Array<number>} times_arr
 * @returns {number} - The average
 */
function computeAverage(times_arr) {
    return times_arr.reduce((a, b) => a + b) / times_arr.length;
}

/**
 * Compute min of the metric
 * @param {Array<number>} times_arr
 * @returns {number} - The min
 */
function computeMin(times_arr) {
    return times_arr.reduce((a, b) => (a < b ? a : b));
}

/**
 * Compute max of the metric
 * @param {Array<number>} times_arr
 * @returns {number} - The max
 */
function computeMax(times_arr) {
    return times_arr.reduce((a, b) => (a < b ? b : a));
}

/**
 * @param {Array<number>} arr
 * @returns {number}
 */
function computeNbCalls(arr) {
    return arr.length;
}

/**
 * Computes the average CPU time from an array of start and end times, considering overlapping periods as a single time span.
 * @param {Array<Array<number>>} start_end_times - The Metric object.
 * @returns {number} - The average CPU time.
 */
function computeCpuTime(start_end_times) {
    // Sort the time intervals by start time
    const sortedTimes = start_end_times.sort((a, b) => a[0] - b[0]);

    let total = 0;
    let count = 0;
    let currentEnd = sortedTimes[0][1];

    for (let i = 0; i < sortedTimes.length; i++) {
        const [start, end] = sortedTimes[i];

        // If the current interval does not overlap with the previous one, add the previous interval's length to the total
        if (start > currentEnd) {
            total += currentEnd - sortedTimes[count][0];
            count = i;
        }

        // Update the end of the current interval
        currentEnd = Math.max(currentEnd, end);
    }

    // Add the last interval's length to the total
    total += currentEnd - sortedTimes[count][0];
    // Compute the average
    // const average = total / sortedTimes.length;

    return total;
}

/**
 * 
 * @param {Array<EnhancedMetric>} enchantedMetrics
 * @returns {Array<EnhancedMetric>}
 */
function sortByAverage(enchantedMetrics) {
    return enchantedMetrics.sort((a, b) => b.average - a.average);
}

/**
 * 
 * @param {Array<EnhancedMetric>} array
 * @returns {Array<EnhancedMetric>}
 */
export function computeChildren(array) {
    let tree = [];
    let lookup = {};
    
    // handle parents that are not measured
    const parents = new Set(
        array.map((a) => a.parent).filter((a) => a !== null),
    );
    const functionNameClasses = new Set(
        array.map((a) => a.id),
    );
    const difference = (a, b) => new Set([...a].filter((x) => !b.has(x)));
    for (const it of difference(parents, functionNameClasses)) {
        array.push({
            id: it,
            parent: null,
            average: 0,
            min: 0,
            max: 0,
            nbCalls: 0,
            cpu_time: 0,
            children: []
        });
    }

    // First map the nodes of the array to an object -> create a hash table.
    for (let i = 0; i < array.length; i++) {
        lookup[array[i].id] = array[i];
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
    console.log("Final enhanced metrics are ", tree);
    return tree;
}

/**
 *
 * @param {Array<Metric>} metrics
 * @returns {Array<EnhancedMetric>}
 */
function enhanceData(metrics) {
    const enhancedData = metrics.map((metric) => {
        const durationArray = metric.start_end_times.map(([a, b]) => b - a);
        const newMetric = {
            id: metric.id,
            parent: metric.parent,
            average: computeAverage(durationArray),
            min: computeMin(durationArray),
            max: computeMax(durationArray),
            cpu_time: computeCpuTime(metric.start_end_times),
            nbCalls: computeNbCalls(durationArray),
            children: [],
        };
        return newMetric;
    });
    return enhancedData;
}

/**
 *
 * @param {Array<SingleMetric>} metrics
 * @returns {Array<Metric>}
 */
function groupSingleMetricsIntoMetric(metrics) {
    /**
     * @type {Map<String, Metric>}
     */
    const map = new Map();
    metrics.forEach((metric) => {
        const key = `${metric.id}-${metric.parent}`;
        if (map.has(key)) {
            // console.log("LOGGING METRIC IN GROUPSINGLE", map[key]);
            map.get(key).start_end_times.push(metric.start_end_times);
        } else {
            map.set(key, { ...metric, start_end_times: [metric.start_end_times] });
        }
    });

    return Array.from(map.values());
}

/**
 *
 * @param {Array<SingleMetric>} data
 */
function nanosSecondsToMillis(data) {
    return data.map((singleMetric) => {
        const times = singleMetric.start_end_times.map((n) => n / 1_000_000);
        return {...singleMetric, start_end_times: times};
    });
}

/**
 *
 * @param {Array<SingleMetric>} data
 */
export function processData(data) {
    const millisData = nanosSecondsToMillis(data)
    const metrics = groupSingleMetricsIntoMetric(millisData);
    const enhancedData = enhanceData(metrics);
    const sorted = sortByAverage(enhancedData);
    return sorted;
    // return computeChildren(sorted);
}