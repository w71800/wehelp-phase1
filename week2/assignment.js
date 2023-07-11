let pushedIn = false
const dirPath = pushedIn? "/tasks_javascript" : ""



// node test
// const task1 = require(`.${dirPath}/task1.js`)
// const task2 = require(`.${dirPath}/task2.js`)
// const task3 = require(`.${dirPath}/task3.js`)
// const task4 = require(`.${dirPath}/task4.js`)

// 到時候上機的狀況使用 ESM
import task1 from "./tasks_javascript/task1.js"
import task2 from "./tasks_javascript/task2.js"
import task3 from "./tasks_javascript/task3.js"
import task4 from "./tasks_javascript/task4.js"

const logMsg = `======== task1 ========
符合可能成年資格的：${task1.join("、")}
======== task2 ========
獎金總額為：${task2} NTD
======== task3 ========
${task3.result1} 和 ${task3.result2} 不重複中間字
======== task4 ========
輸入 1 的結果：${task4.resultOf_1} / 輸入 5 的結果：${task4.resultOf_5} / 輸入 10 的結果：${task4.resultOf_10}
======== task5 ========

`
console.log(logMsg);

