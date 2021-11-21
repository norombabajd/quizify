async function convert_data(event){
  fetch("/login").then(res => res.text()).then(text => {
    console.log(text)
  })
}

snippets = snippets.replaceAll("&#34;", "\"")
snippets = snippets.replaceAll("&#39;", "'")
snippets = JSON.parse(snippets)

function run_quiz(event){
  for(let x = 1; x < 31; x++){
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
    let choices = []
    for(let i = 0; i < 4; i++){
      let rand = int(Math.random()* 4)
      
    }

  }
}

