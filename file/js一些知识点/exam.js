function findLongestWordLength(str) {
    let a=0;
    let b=0;
    for(let i=0;i++;i<str.length){
      if(str[i]===' '){
        if(a>b){
          b=a;
        };
        a=0; 
      }
      else{
        a++;
      };
  
    }
    if(a>b){
      b=a;
    };
    return b;
  };
  
 findLongestWordLength("The quick brown fox jumped over the lazy dog");