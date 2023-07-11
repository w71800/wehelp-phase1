import task1 from "./tasks_javascript/task1.js"
import task2 from "./tasks_javascript/task2.js"
import task3 from "./tasks_javascript/task3.js"
import task4 from "./tasks_javascript/task4.js"
import task5 from "./tasks_javascript/task5.js"

const logMsg = `======== task1 ========
符合可能成年資格的：${task1.join("、")}
======== task2 ========
獎金總額為：${task2} NTD
======== task3 ========
${task3.result1} 和 ${task3.result2} 不重複中間字，但 result3 ${task3.result3} 
======== task4 ========
輸入 1 的結果：${task4.resultOf_1}、輸入 5 的結果：${task4.resultOf_5}、輸入 10 的結果：${task4.resultOf_10}
======== task5 ========
訂位結果：${task5}（如未訂到則顯示 -1）

// `
console.log(logMsg);
