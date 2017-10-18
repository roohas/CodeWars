function accum(s) {
	var s_arr=s.split("");
	var ans="";
    var i=0;
    while(i<s_arr.length)
    {
        var mid_ans=s_arr[i].toUpperCase();
        ans+=mid_ans;
        
        var n=i;
        while(n>0)
        {
            ans+=s_arr[i].toLowerCase();
            n--;
        }
        
        if(i!=s_arr.length-1)
        {
            ans+="-";
        }
        
        i++;
    }
    return ans;
}