const canSum=(sum,array,map={})=>{
    if (sum in map){
        return map[sum];
    }
    if(sum==0){
        return true;
    }
    if(sum<0){
        return false;
    }
    for (let arr in array){
        const rem =sum-arr;
        if(canSum(rem,array)==true){
            map[sum]=true
            return true;
        }


    }
    map[sum]=false
    return false;


}
console.log(canSum(6, [2, 3]))
console.log(canSum(7, (5, 3, 4, 7)))
console.log(canSum(7, [2, 4]))
console.log(canSum(8, [2, 3, 5]))
console.log(canSum(50, [7, 14]))