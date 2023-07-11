function findAndPrint(messages){
  const keywords = [ "18", "college", "legal age", "will vote" ]
  let rawDatas = Object.entries(messages)
  let datas = []
  let results = []

  rawDatas.forEach( data => {
    let obj = {}
    obj.name = data[0]
    obj.msg = data[1]

    datas.push(obj)
  })

  datas.forEach( data => {
    let { name, msg } = data

    for(let word of keywords){
      if (msg.includes(word)){
        results.push(name)
      }
     }
  })
  
  return results
} 

const result = findAndPrint({
  "Bob": "My name is Bob. I'm 18 years old.", 
  "Mary": "Hello, glad to meet you.",
  "Copper": "I'm a college student. Nice to meet you.",
  "Leslie": "I am of legal age in Taiwan.",
  "Vivian": "I will vote for Donald Trump next week",
  "Jenny": "Good morning."
});

// export default result
// test in node
module.exports  = result