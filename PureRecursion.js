const collectOddValues = arr => {
  let newArr = [];

  if (arr.length === 0) {
    return newArr;
  }

  if (arr[0] % 2 !== 0) {
    newArr.push(arr[0]);
  }

  newArr = newArr.concat(collectOddValues(arr.slice(1)));
  //[1].concat(collectOddValues([2, 3, 4, 5]);
  //				[].concat(collectOddValues([3, 4, 5]);
  //					 	[3].concat(collectOddValues([4, 5]);
  //								[].concat(collectOddValues([5]);
  //										[5].concat(collectOddValues([]); 
  //                                                           []

  return newArr;
};

const answer = collectOddValues([1, 2, 3, 4, 5]);

console.log(answer); // [ 1, 3, 5 ]
