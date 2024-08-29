/**
 * @typedef {Object} SingleMetric
 * @property {string} id - The id of the object.
 * @property {?string} parent - The parent of the object.
 * @property {Array<number>} start_end_times - An array containing two timestamps representing the start and end times.
 */

/**
 * @typedef {Object} Metric
 * @property {string} id - The id of the object.
 * @property {?string} parent - The parent of the object.
 * @property {Array<Array<number>>} start_end_times - An array of arrays, each containing two timestamps representing the start and end times.
 */

/**
 * @typedef {Object} EnhancedMetric
 * @property {string} id - The id of the object
 * @property {?string} parent - The parent of the object
 * @property {number} average - The average
 * @property {number} min - The min
 * @property {number} max - The max
 * @property {number} nbCalls - Number of calls
 * @property {number} cpu_time - Cpu time
 * @property {Array<EnhancedMetric>} children - Childrens
 */