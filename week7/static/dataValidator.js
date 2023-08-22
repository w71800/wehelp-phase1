function formatIsOk(str){
  const regExp = new RegExp("^[a-zA-Z0-9_]+$")
  return regExp.test(str)
}

function hasSpace(str){
  const regExp  = /^\s*$/;
  return regExp.test(str)
}