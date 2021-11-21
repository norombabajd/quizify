async function convert_data(event){
  fetch("/login").then(res => res.text()).then(text => {
    console.log(text)
  })
}

snippets = snippets.replaceAll("&#34;", "\"")
snippets = snippets.replaceAll("&#39;", "'")
snippets = JSON.parse(snippets)
if(snippets.length > 30):
  snippets = snippets.slice(0,30)
let score = 0
let index = 0
let outof = snippets.length
let snippet = snippets[index][0]
let artist = snippets[index][1]
let choices = [artist]
for(let i = 1; i < 4; i++){
  let rand = Math.floor(Math.random() * 3)
  choices[i] = snippets[rand][1]
}
choices = shuffle_choices(choices)


function shuffle_choices(choices){
  for (var i = choices.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = choices[i];
        choices[i] = choices[j];
        choices[j] = temp;
    }
  return choices
}
function determineWin(choice){
  if 
}
function run_quiz(event){
  for(let x = 1; x < snippets.length; x++){
    let snippet = snippets[x][0]
    let artist = snippets[x][1]
    let answers = []
    for(let j = 0; j < 3; j++){
      let rand = int(Math.random()* 30)
      if(snippets[rand][1] != artist){
        answers[j] = snippets[rand][1]
      }
      else{
        j-=1
      }
    }
    answers[3] = artist
    let choices = []
    for(let i = 0; i < 4; i++){
      let rand = int(Math.random()* 4)
      choices[i] = answers[rand]
      answers.splice(rand, 1)
    }
    number.innerText = str(i) + "/" + str(snippets.length)
    question.innerText = "\"" + snippet + "\""
    song1.innerText = choices[0]
    song2.innerText = choices[1]
    song3.innerText = choices[2]
    song4.innerText = choices[3]
  }
}

