export function unrefArray(arr: Array<object>) {
  if (arr.length === 0) {
    return arr;
  }
  let result = [];
  for (let item of arr) {
    result.push(item.value);
  }
  return result;
};
export function objectToDictionary(obj) {
  let dict = {};
  for (let prop in obj) {
    dict[prop] = obj[prop];
    console.log(prop);
  }
  return dict;
}
