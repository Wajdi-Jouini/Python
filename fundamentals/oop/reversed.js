var str1="creature";
function reversed(string)
{
    var reserve="";
    for (var i=string.length-1; i>=0; i--)
    {
        reserve +=string[i];
    }console.log(string, reserve);
    return reserve
}
reversed(str1)
