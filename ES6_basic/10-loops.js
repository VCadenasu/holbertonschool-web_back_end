export default function appendToEachArrayValue(array, appendString) {
  for (let idx of array) {
    NewArray = appendString + idx;
  }

  return array;
}
